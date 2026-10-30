import numpy as np
import pandas as pd
import joblib
import os
from typing import Dict, Any, List

try:
    from app.llm_collaborator import LLMCollaborator
except ImportError:
    from llm_collaborator import LLMCollaborator

class VeriKlaimEngine:
    """
    VeriKlaim Core Detection Engine v2.0
    Mengimplementasikan 6 Klaster Variabel Sesuai Laporan Rencana Peningkatan Model:
    - Klaster 1: Top-Up Tarif Khusus (Special CMGs SP, RR, SI, SD - FKL33 s.d. FKL46)
    - Klaster 2: Disparitas Diagnosis Masuk vs Keluar (FKL15A vs FKL17A - Coding Drift)
    - Klaster 3: Intensitas Biaya per Hari Rawat (Cost Velocity Ratio - FKL47 / LOS_HARI)
    - Klaster 4: Integritas Rujukan Berjenjang (FKP02 - Bypassing Referral)
    - Klaster 5: Multi-Komorbiditas Sekunder (CC/MCC Matrix & Diagnosis Padding)
    - Klaster 6: Kesesuaian Profil Faskes & Hak Kelas Rawat (Hospital Capability Mismatch)
    - Explainable AI: Integrasi TreeSHAP-Inspired Feature Contribution
    """

    def __init__(self, model_path: str = None):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(base_dir)
        if model_path is None:
            model_path = os.path.join(root_dir, "models", "real_veriklaim_model.joblib")
            if not os.path.exists(model_path):
                model_path = os.path.join(root_dir, "models", "veriklaim_model.joblib")
            if not os.path.exists(model_path):
                model_path = os.path.join(base_dir, "real_veriklaim_model.joblib")

        self.model_path = model_path
        self.artifacts = joblib.load(self.model_path) if os.path.exists(self.model_path) else None
        self.llm = LLMCollaborator()
        print(f"[VeriKlaimEngine] Initialized v2.0 with model: {self.model_path} (In-Memory)")

    def audit_single_claim(self, claim: Dict[str, Any]) -> Dict[str, Any]:
        """
        Audit klaim individual secara komprehensif melalui 6 Klaster Deteksi Fraud & Kaidah Permenkes
        """
        no_sep = claim.get("no_sep", "SEP-UNKNOWN")
        id_peserta = claim.get("id_peserta", "PST-UNKNOWN")
        tipe_faskes = claim.get("tipe_faskes", "RS Kelas C")
        jenis_faskes = claim.get("jenis_faskes", "RS Umum")
        pelayanan = str(claim.get("pelayanan", "RITL")).upper() # RITL / RJTL
        diagnosa_icd10 = claim.get("kode_icd10", "J18.9")
        nama_diagnosa = claim.get("nama_diagnosa", "Pneumonia Tidak Spesifik")
        diag_masuk_icd10 = claim.get("diag_masuk_icd10") or claim.get("kode_icd10_masuk")
        komorbid_icd10 = claim.get("kode_komorbid", "-")
        prosedur_icd9 = claim.get("kode_icd9", "-")
        kode_inacbg = claim.get("kode_inacbg", "J-4-16-III")
        nama_inacbg = claim.get("nama_inacbg", "INFEKSI SALURAN PERNAPASAN")
        severity_level = int(claim.get("severity_level", 3))
        los_hari = int(claim.get("los_hari", 2))
        biaya_tagih = float(claim.get("biaya_tagih", 17400000.0))
        biaya_riil = float(claim.get("biaya_riil", 3400000.0))
        tarif_standar = float(claim.get("tarif_standar", biaya_tagih))

        # Parameter 6 Klaster Tambahan
        topup_special_cmg = str(claim.get("topup_special_cmg", "-")).strip()
        biaya_topup = float(claim.get("biaya_topup", 0.0))
        custom_cost_velocity = claim.get("cost_velocity_ratio")
        fkp02_rujukan = claim.get("fkp02_rujukan")
        is_unreferral = bool(claim.get("is_unreferral", False))

        # Clinical & Context Flags (Edge Case & CC/MCC handling)
        status_pulang = str(claim.get("status_pulang", "SEMBUH")).strip().upper()
        cara_pulang = str(claim.get("cara_pulang", "")).strip().upper()
        is_deceased = (
            "MENINGGAL" in status_pulang or "WAFAT" in status_pulang or 
            cara_pulang in ["4", "MENINGGAL", "WAFAT"]
        )
        is_emergency = bool(claim.get("is_emergency", False)) or str(claim.get("alasan_kunjungan", "")).strip().upper() == "DARURAT"
        has_valid_mcc = claim.get("has_valid_mcc", None)
        is_same_organ = bool(claim.get("is_same_organ", True))

        # Evaluasi 6 Klaster:
        # Klaster 1: Top-Up Tarif Khusus (Special CMGs SP, RR, SI, SD)
        topup_score, topup_reasons, topup_regulasi, topup_recomms, topup_saving = self._check_special_cmg_topup(
            prosedur_icd9, topup_special_cmg, biaya_topup
        )

        # Klaster 2: Disparitas Diagnosis Masuk vs Keluar (Coding Drift / Gaming)
        drift_score, drift_reasons, drift_regulasi, drift_recomms = self._check_coding_drift(
            diag_masuk_icd10, diagnosa_icd10, prosedur_icd9, los_hari
        )

        # Klaster 3: Intensitas Biaya per Hari Rawat (Cost Velocity Ratio)
        velocity_score, velocity_ratio, velocity_reasons, velocity_regulasi, velocity_recomms = self._check_cost_velocity(
            tipe_faskes, pelayanan, los_hari, biaya_tagih, prosedur_icd9, custom_cost_velocity
        )

        # Klaster 4: Integritas Rujukan Berjenjang (Bypassing Referral)
        referral_score, referral_reasons, referral_regulasi, referral_recomms = self._check_referral_integrity(
            pelayanan, diagnosa_icd10, is_unreferral, fkp02_rujukan, is_emergency
        )

        # Klaster 5: Multi-Komorbiditas Sekunder (CC/MCC Matrix & Upcoding)
        upcoding_score, upcoding_reasons = self._check_upcoding(
            severity_level, los_hari, prosedur_icd9, komorbid_icd10, biaya_tagih, biaya_riil, has_valid_mcc, is_deceased
        )

        # Klaster 6: Kesesuaian Profil Faskes & Hak Kelas Rawat (Hospital Capability Mismatch)
        capability_score, capability_reasons, capability_regulasi, capability_recomms = self._check_hospital_capability(
            tipe_faskes, jenis_faskes, prosedur_icd9
        )

        # Evaluasi Modul Unbundling & Phantom Billing Standar
        unbundling_score, unbundling_reasons = self._check_unbundling(
            pelayanan, los_hari, prosedur_icd9, claim.get("kunjungan_terakhir_hari", 999), is_emergency, is_same_organ
        )
        phantom_score, phantom_reasons = self._check_phantom_billing(
            pelayanan, los_hari, biaya_riil, biaya_tagih, is_deceased
        )

        # Agregasi Skor per Modul Komposit
        composite_upcoding = max(upcoding_score, drift_score)
        composite_phantom = max(phantom_score, topup_score, capability_score)
        composite_unbundling = max(unbundling_score, referral_score)
        
        # Skor Maksimum
        all_scores = {
            "UPCODING": composite_upcoding,
            "UNBUNDLING": composite_unbundling,
            "PHANTOM_BILLING": composite_phantom,
            "COST_VELOCITY": velocity_score
        }
        max_fraud_type = max(all_scores, key=all_scores.get)
        max_score = all_scores[max_fraud_type]
        is_fraud = 1 if max_score >= 0.65 else 0

        fraud_type = "NORMAL"
        primary_reasons = []
        regulasi_dasar = []
        rekomendasi_verifikator = []
        potensi_penghematan = 0.0

        if is_fraud:
            if max_fraud_type == "UPCODING":
                fraud_type = "UPCODING"
                primary_reasons = drift_reasons if drift_score >= upcoding_score else upcoding_reasons
                regulasi_dasar = drift_regulasi if drift_score >= upcoding_score else [
                    "Permenkes No. 26 Tahun 2021 Pasal 14: Penetapan Severity Level III wajib didukung bukti penanganan komplikasi berat dan penggunaan sumber daya klinis intensif.",
                    "Petunjuk Teknis INA-CBG: Koding komorbiditas sekunder tanpa tindakan terapi spesifik dari DPJP dilarang dijadikan dasar penagihan level berat."
                ]
                rekomendasi_verifikator = drift_recomms if drift_score >= upcoding_score else [
                    "Koreksi klaim: Turunkan Severity Level dari III ke Level I / II sesuai resume medis riil.",
                    "Verifikasi berkas: Minta catatan lembar instruksi DPJP dan hasil pemeriksaan penunjang (laboratorium/radiologi).",
                    "Rekomendasi sistem VClaim: Tahan persetujuan otomatis, alihkan ke verifikasi paska-klaim (AUDIA)."
                ]
                potensi_penghematan = max(0.0, biaya_tagih - biaya_riil) if biaya_riil > 0 else (biaya_tagih * 0.5)
            elif max_fraud_type == "UNBUNDLING":
                fraud_type = "UNBUNDLING"
                primary_reasons = referral_reasons if referral_score >= unbundling_score else unbundling_reasons
                regulasi_dasar = referral_regulasi if referral_score >= unbundling_score else [
                    "Permenkes No. 26 Tahun 2021: Prosedur penanganan episode perawatan berkesinambungan merupakan satu kesatuan paket klaim INA-CBG.",
                    "SE Dirjen Pelayanan Kesehatan HK.02.02/I/1811/2022: Larangan memecah episode tindakan medis berulang dalam jangka waktu < 30 hari untuk diagnosa serumpun."
                ]
                rekomendasi_verifikator = referral_recomms if referral_score >= unbundling_score else [
                    "Konsolidasi berkas klaim: Gabungkan episode kunjungan terpisah menjadi 1 nomor SEP utama.",
                    "Batalkan klaim tambahan untuk prosedur penunjang yang telah tercakup dalam tarif paket utama.",
                    "Kirimkan notifikasi kepatuhan faskes melalui aplikasi HFIS / Dashboard Verifikator."
                ]
                potensi_penghematan = biaya_tagih if referral_score >= unbundling_score else max(0.0, biaya_tagih - biaya_riil)
            elif max_fraud_type == "PHANTOM_BILLING":
                fraud_type = "PHANTOM_BILLING"
                if topup_score >= phantom_score and topup_score >= capability_score:
                    primary_reasons = topup_reasons
                    regulasi_dasar = topup_regulasi
                    rekomendasi_verifikator = topup_recomms
                    potensi_penghematan = topup_saving if topup_saving > 0 else max(0.0, biaya_tagih - biaya_riil)
                elif capability_score >= phantom_score:
                    primary_reasons = capability_reasons
                    regulasi_dasar = capability_regulasi
                    rekomendasi_verifikator = capability_recomms
                    potensi_penghematan = biaya_tagih
                else:
                    primary_reasons = phantom_reasons
                    regulasi_dasar = [
                        "Permenkes No. 16 Tahun 2019 Pasal 4 Ayat 1: Tindakan penagihan atas pelayanan atau tindakan yang tidak pernah diberikan merupakan tindak kecurangan (Fraud).",
                        "Pedoman Audit Medik BPJS Kesehatan: Pelayanan rawat inap dengan LOS 0 hari tanpa indikasi darurat atau rujukan khusus harus ditagihkan sebagai Rawat Jalan (RJTL)."
                    ]
                    rekomendasi_verifikator = [
                        "BLOKIR SEMENTARA: Tolak pengajuan klaim pada sistem VClaim.",
                        "Laporkan ke Satgas Anti-Fraud BPJS Kesehatan / Tim SIGAP untuk audit forensik rekam medis RS.",
                        "Lakukan verifikasi silang absensi pasien di faskes pada tanggal SEP bersangkutan."
                    ]
                    potensi_penghematan = max(0.0, biaya_tagih - biaya_riil)
            else: # COST_VELOCITY
                fraud_type = "UPCODING"
                primary_reasons = velocity_reasons
                regulasi_dasar = velocity_regulasi
                rekomendasi_verifikator = velocity_recomms
                potensi_penghematan = max(0.0, biaya_tagih - (2500000.0 * max(1, los_hari)))
        else:
            primary_reasons = [
                "Koherensi klinis terverifikasi: Diagnosa, lama rawat, dan tindakan selaras dengan standar INA-CBG.",
                "Rasio pembiayaan wajar dan memenuhi ketentuan tarif regional BPJS Kesehatan."
            ]
            regulasi_dasar = [
                "Permenkes No. 26 Tahun 2021: Klaim memenuhi syarat verifikasi administrasi dan klinis JKN."
            ]
            rekomendasi_verifikator = [
                "Lolos verifikasi: Setujui klaim untuk penerbitan FPK (Formulir Pengajuan Klaim) otomatis."
            ]
            potensi_penghematan = 0.0

        # Explainable AI: SHAP-inspired Feature Contribution Breakdown (%)
        shap_contributions = self._calculate_shap_contributions({
            "upcoding_matrix": composite_upcoding,
            "coding_drift": drift_score,
            "cost_velocity": velocity_score,
            "special_cmg_topup": topup_score,
            "referral_integrity": referral_score,
            "hospital_capability": capability_score,
            "unbundling_temporal": unbundling_score,
            "phantom_los": phantom_score
        }, is_fraud=is_fraud)

        # Fitur 02 & Fitur 04: Kolaborasi ML + LLM dengan Graceful Fallback & Manual Toggle
        force_mode = claim.get("force_mode") or claim.get("force_llm_mode")
        llm_response = self.llm.generate_clinical_narrative(
            claim,
            {
                "is_fraud": is_fraud,
                "fraud_type": fraud_type,
                "status_label": "KLAIM DITAHAN — ANOMALI" if is_fraud else "KLAIM LOLOS — WAJAR",
                "risk_score": round(max_score * 100, 1),
                "audit_findings": primary_reasons,
                "topup_flag": bool(topup_score > 0),
                "coding_drift_flag": bool(drift_score > 0),
                "cost_velocity_ratio": velocity_ratio,
                "unreferral_flag": bool(referral_score > 0),
                "capability_mismatch": bool(capability_score > 0)
            },
            force_mode=force_mode
        )

        return {
            "no_sep": no_sep,
            "id_peserta": id_peserta,
            "tipe_faskes": tipe_faskes,
            "jenis_faskes": jenis_faskes,
            "pelayanan": pelayanan,
            "diagnosa": f"{nama_diagnosa} ({diagnosa_icd10})",
            "inacbg": f"{kode_inacbg} - {nama_inacbg}",
            "severity_level": severity_level,
            "los_hari": los_hari,
            "biaya_tagih_idr": int(biaya_tagih),
            "biaya_riil_idr": int(biaya_riil),
            "potensi_hemat_idr": int(potensi_penghematan),
            "is_fraud": is_fraud,
            "fraud_type": fraud_type,
            "status_label": "KLAIM DITAHAN — ANOMALI" if is_fraud else "KLAIM LOLOS — WAJAR",
            "risk_score": round(max_score * 100, 1),
            "module_scores": {
                "upcoding_score": round(composite_upcoding * 100, 1),
                "unbundling_score": round(composite_unbundling * 100, 1),
                "phantom_score": round(composite_phantom * 100, 1)
            },
            "cluster_breakdown": {
                "klaster_1_special_cmg_topup": round(topup_score * 100, 1),
                "klaster_2_coding_drift": round(drift_score * 100, 1),
                "klaster_3_cost_velocity": round(velocity_score * 100, 1),
                "klaster_4_bypassing_referral": round(referral_score * 100, 1),
                "klaster_5_comorbid_padding": round(upcoding_score * 100, 1),
                "klaster_6_hospital_capability": round(capability_score * 100, 1)
            },
            "cost_velocity_ratio": round(velocity_ratio, 2),
            "shap_feature_importance": shap_contributions,
            "audit_findings": primary_reasons,
            "dasar_regulasi": regulasi_dasar,
            "rekomendasi_verifikator": rekomendasi_verifikator,
            "clinical_narrative": llm_response.get("narrative", ""),
            "llm_metadata": {
                "provider": llm_response.get("provider"),
                "status_badge": llm_response.get("status_badge"),
                "is_fallback": llm_response.get("is_fallback", True),
                "latency_ms": llm_response.get("latency_ms", 0.0)
            }
        }

    # =========================================================================
    # KLASTER 1: Top-Up Tarif Khusus (Special CMGs SP, RR, SI, SD)
    # =========================================================================
    def _check_special_cmg_topup(self, proc: str, topup_type: str, biaya_topup: float):
        score = 0.0
        reasons = []
        regulasi = []
        recomms = []
        saving = 0.0

        proc_str = str(proc).strip().lower()
        topup_str = str(topup_type).strip().upper()

        has_topup = (biaya_topup > 0) or (topup_str not in ["-", "", "NONE", "TIDAK ADA", "NAN"])
        if not has_topup:
            return 0.0, [], [], [], 0.0

        # Special Prosthesis (RR - Implan / Ring Stent / Platina)
        is_rr = ("RR" in topup_str or "IMPLAN" in topup_str or "PROSTHESIS" in topup_str or "PLATINA" in topup_str or "STENT" in topup_str)
        has_surgery_proc = any(p in proc_str for p in ["79.", "78.", "81.", "36.0", "orif", "fiksasi", "reduksi", "artroplasti", "stent", "graft"])

        # Special Drugs (SD - Hemofilia / Kanker / Obat Kronis)
        is_sd = ("SD" in topup_str or "OBAT" in topup_str or "HEMOFILIA" in topup_str or "KEMO" in topup_str)
        has_drug_proc = any(p in proc_str for p in ["99.25", "kemo", "infus faktor", "hemofilia", "transfusi"])

        # Special Investigation (SI - MRI / Kateterisasi Canggih)
        is_si = ("SI" in topup_str or "INVESTIGASI" in topup_str or "MRI" in topup_str or "CATH" in topup_str)
        has_investigation_proc = any(p in proc_str for p in ["88.9", "37.2", "mri", "kateter", "angiografi", "endoskopi"])

        # Special Procedures (SP)
        is_sp = ("SP" in topup_str or "PROSEDUR KHUSUS" in topup_str)
        has_sp_proc = (proc_str not in ["-", "", "nan"])

        is_mismatch = False
        if is_rr and not has_surgery_proc:
            is_mismatch = True
            reasons.append("Penagihan Top-Up Special Prosthesis (RR - Implan Platina/Stent) diajukan tanpa adanya prosedur operasi bedah / reduksi terbuka (ORIF) pada rekam tindakan.")
        elif is_sd and not has_drug_proc and proc_str in ["-", "", "nan"]:
            is_mismatch = True
            reasons.append("Penagihan Top-Up Special Drugs (SD - Obat Khusus/Hemofilia) tanpa adanya catatan prosedur pemberian protokol terapi khusus.")
        elif is_si and not has_investigation_proc:
            is_mismatch = True
            reasons.append("Penagihan Top-Up Special Investigation (SI) tanpa adanya bukti tindakan penunjang canggih pada lembar tindakan.")
        elif is_sp and not has_sp_proc:
            is_mismatch = True
            reasons.append("Penagihan Top-Up Special Procedures (SP) tanpa tercatatnya prosedur spesifik di berkas tindakan ICD-9-CM.")

        if is_mismatch:
            score = 0.90
            saving = biaya_topup if biaya_topup > 0 else 15000000.0
            reasons.append(f"Variabel TOPUP_WITHOUT_PROCEDURE_FLAG = 1: Indikasi Phantom Top-Up Special CMG senilai Rp {int(saving):,}.")
            regulasi = [
                "Permenkes No. 26 Tahun 2021 Pasal 16 & Lampiran Bab IV: Pengajuan Special CMG hanya sah apabila tindakan khusus/implan benar-benar diberikan sesuai indikasi klinis.",
                "Permenkes No. 3 Tahun 2023 Pasal 22 s.d. 25: Standar tarif pelayanan kesehatan dan daftar restriksi Special CMG.",
                "Permenkes No. 16 Tahun 2019 Pasal 4 Ayat 1 Huruf d: Tindak kecurangan atas penagihan bahan medis habis pakai/implan yang tidak diberikan."
            ]
            recomms = [
                "Batalkan komponen klaim Special CMG dan kembalikan ke tarif paket dasar INA-CBG.",
                "Lakukan audit silang nomor seri implan/faktur farmasi rumah sakit.",
                "Minta lembar laporan operasi (surgical report) dari dokter penanggung jawab (DPJP)."
            ]

        return score, reasons, regulasi, recomms, saving

    # =========================================================================
    # KLASTER 2: Disparitas Diagnosis Masuk vs Keluar (Coding Drift / Gaming)
    # =========================================================================
    def _check_coding_drift(self, diag_masuk: str, diag_keluar: str, proc: str, los: int):
        score = 0.0
        reasons = []
        regulasi = []
        recomms = []

        if not diag_masuk:
            return 0.0, [], [], []

        masuk = str(diag_masuk).strip().upper()
        keluar = str(diag_keluar).strip().upper()
        proc_str = str(proc).strip().lower()

        # Daftar Gejala Ringan Masuk IGD/Poli
        light_entry = any(masuk.startswith(c) for c in ["K30", "R10", "J06", "A09", "R05", "R50", "R51", "R07", "K52.9"])
        # Daftar Penyakit Katastropik / Akut Berat saat Keluar
        severe_exit = any(keluar.startswith(c) for c in ["K25.0", "K25", "K35", "J18", "I21", "I63", "A91", "K26"])

        # Bukti penunjang / tindakan diagnostik objektif
        has_diagnostic_proof = any(p in proc_str for p in ["44.1", "endoskopi", "88.0", "ct scan", "87.4", "usg", "47.0", "laparatomi"])

        if light_entry and severe_exit and (not has_diagnostic_proof or los <= 2):
            score = 0.85
            reasons.append(
                f"Lompatan Diagnosis (Coding Drift): Pasien masuk dengan gejala ringan ({masuk}) namun diagnosis primer saat tagihan diubah menjadi penyakit akut berat ({keluar}) "
                f"tanpa bukti tindakan penunjang konfirmatif atau endoskopi/radiologi."
            )
            reasons.append("Variabel DIAG_SHIFT_SEVERITY_GAP = 1: Terindikasi manipulasi koding administrasi (Coding Gaming) untuk mendongkrak tarif INA-CBG.")
            regulasi = [
                "Permenkes No. 26 Tahun 2021 Pasal 14 Ayat (1) dan (2): Penetapan Diagnosis Utama wajib merujuk pada resume medis otentik yang ditandatangani DPJP.",
                "Permenkes No. 16 Tahun 2019 Pasal 4 Ayat (1) Huruf a: Penyesuaian koding diagnosis menjadi lebih tinggi dari riil pasien dikualifikasikan sebagai Upcoding."
            ]
            recomms = [
                "Kembalikan koding diagnosis utama ke diagnosis awal sesuai catatan IGD / resume medis asli DPJP.",
                "Klarifikasi dokter spesialis DPJP mengenai bukti hasil pemeriksaan penunjang penegak diagnosis.",
                "Tahan pengajuan klaim dan alihkan ke verifikasi paska-klaim tim AUDIA BPJS."
            ]

        return score, reasons, regulasi, recomms

    # =========================================================================
    # KLASTER 3: Intensitas Biaya per Hari Rawat (Cost Velocity Ratio)
    # =========================================================================
    def _check_cost_velocity(self, tipe_rs: str, pelayanan: str, los: int, tagih: float, proc: str, custom_ratio: float = None):
        score = 0.0
        reasons = []
        regulasi = []
        recomms = []

        if pelayanan != "RITL":
            return 0.0, 1.0, [], [], []

        effective_los = max(1, los)
        daily_cost = tagih / effective_los

        # Batas wajar harian peer RS sekelas (Permenkes 3/2023)
        peer_benchmarks = {
            "RS Kelas A": 4500000.0,
            "RS Kelas B": 3500000.0,
            "RS Kelas C": 2500000.0,
            "RS Kelas D": 1800000.0
        }
        baseline = peer_benchmarks.get(tipe_rs, 2500000.0)
        ratio = float(custom_ratio) if custom_ratio is not None else (daily_cost / baseline)

        proc_str = str(proc).strip().lower()
        is_intensive = any(p in proc_str for p in ["ventilator", "icu", "kraniotomi", "laparatomi", "orif", "36.0", "bypass", "resusitasi"])

        if ratio >= 3.0 and not is_intensive:
            score = 0.80 if ratio >= 5.0 else 0.70
            reasons.append(
                f"Anomali Intensitas Biaya (Cost Velocity Ratio = {ratio:.1f}x): Biaya harian mencapai Rp {int(daily_cost):,}/hari "
                f"({ratio:.1f}x di atas ambang wajar {tipe_rs}) dengan lama rawat singkat ({los} hari) tanpa prosedur intensif/ICU."
            )
            regulasi = [
                "Permenkes No. 26 Tahun 2021 Pasal 15: Lama hari rawat dan intensitas biaya harus sesuai Clinical Pathway faskes yang disetujui komite medik.",
                "Permenkes No. 3 Tahun 2023 Pasal 14 & Lampiran Tarif Regional: Tarif paket INA-CBG telah memperhitungkan rata-rata lama hari rawat wajar."
            ]
            recomms = [
                "Lakukan audit rincian billing farmasi dan penggunaan BHP per hari perawatan.",
                "Minta lembar Clinical Pathway dan catatan asuhan keperawatan terintegrasi (CPPT).",
                "Koreksi kelebihan penagihan harian yang tidak sesuai tarif regional."
            ]

        return score, ratio, reasons, regulasi, recomms

    # =========================================================================
    # KLASTER 4: Integritas Rujukan Berjenjang (Bypassing Referral)
    # =========================================================================
    def _check_referral_integrity(self, pelayanan: str, diag_kode: str, is_unreferral: bool, fkp02: str, is_emergency: bool):
        score = 0.0
        reasons = []
        regulasi = []
        recomms = []

        if pelayanan != "RJTL" or is_emergency:
            return 0.0, [], [], []

        diag_upper = str(diag_kode).strip().upper()
        # Kasus kompetensi primer FKTP (non-spesialistik)
        is_primary_care_case = any(diag_upper.startswith(c) for c in ["H52", "K30", "L20", "L30", "J00", "H10", "A09"])

        fkp_str = str(fkp02).strip().upper() if fkp02 else ""
        is_explicit_bypass = is_unreferral or (fkp_str in ["NON_RUJUKAN", "BYPASS", "0", "TANPA_RUJUKAN"])

        if is_explicit_bypass:
            score = 0.85
            reasons.append(
                f"Pelanggaran Sistem Rujukan Berjenjang (Bypassing Referral): Pelayanan Rawat Jalan di RS untuk diagnosa {diag_kode} "
                f"diajukan tanpa adanya surat rujukan FKTP yang sah (kolom FKP02 kosong/tidak valid) untuk kasus non-darurat."
            )
            reasons.append("Variabel IS_UNREFERRAL_OUTPATIENT = 1: Kasus merupakan kompetensi fasilitas kesehatan primer (FKTP).")
            regulasi = [
                "Permenkes No. 001 Tahun 2012 Pasal 4 s.d. 8: Kewajiban sistem rujukan pelayanan kesehatan perorangan secara berjenjang.",
                "Permenkes No. 3 Tahun 2023 Pasal 6: Pelayanan rujukan tingkat lanjutan hanya dapat diberikan atas dasar rujukan FKTP, kecuali gawat darurat.",
                "Peraturan BPJS Kesehatan No. 1 Tahun 2014 Pasal 62: Penolakan klaim rawat jalan rumah sakit yang tidak disertai nomor rujukan FKTP sah."
            ]
            recomms = [
                "Tolak penagihan klaim rawat jalan (Klaim Non-Eligible).",
                "Arahkan peserta untuk memanfaatkan faskes tingkat pertama (FKTP) terdaftar sesuai alur berjenjang JKN.",
                "Tegur faskes rujukan atas penerbitan SEP tanpa surat rujukan melalui sistem HFIS."
            ]

        return score, reasons, regulasi, recomms

    # =========================================================================
    # KLASTER 5: Multi-Komorbiditas Sekunder (CC/MCC Matrix & Upcoding)
    # =========================================================================
    def _check_upcoding(self, severity: int, los: int, proc: str, comorbid: str, tagih: float, riil: float, has_valid_mcc: bool = None, is_deceased: bool = False):
        score = 0.0
        reasons = []

        if is_deceased and riil > 0 and (riil / (tagih + 1.0)) >= 0.35:
            return 0.0, []

        proc_str = str(proc).strip().lower()
        comorbid_str = str(comorbid).strip().lower()
        is_intensive_proc = any(p in proc_str for p in ["96.7", "99.6", "39.95", "ventilator", "icu", "orif", "kraniotomi", "laparatomi"])
        minor_padding = any(c in comorbid_str for c in ["k30", "d64.9", "r05", "o13", "e11.9", "dispepsia", "anemia ringan", "batuk"])

        if severity == 3:
            if has_valid_mcc is True and (is_intensive_proc or los >= 3):
                return 0.0, []

            if has_valid_mcc is False or (minor_padding and not is_intensive_proc):
                score += 0.85
                reasons.append("Klaster Multi-Komorbiditas: Diagnosis sekunder terindikasi 'Diagnosis Padding' (Non-CC / komorbiditas ringan) yang tidak memenuhi syarat mengatrol klaim ke Severity Level III merujuk Permenkes No. 26/2021 Pasal 14.")
            elif los <= 2 and (proc in ["-", "", "nan"] or not is_intensive_proc):
                score += 0.70
                reasons.append(f"Klaim diajukan pada Severity Level 3 (Kategori Berat) namun lama rawat hanya {los} hari tanpa adanya prosedur bedah / tindakan intensif ICD-9-CM pendukung.")

            if riil > 0 and (riil / (tagih + 1.0)) < 0.35:
                score += 0.25
                reasons.append(f"Beban biaya riil fasilitas kesehatan sangat rendah ({riil / tagih * 100:.1f}% dari nilai tagihan klaim), mengindikasikan ketiadaan intervensi intensif.")
        elif severity == 2 and los <= 1 and proc in ["-", "", "nan"] and has_valid_mcc is not True:
            score += 0.45
            reasons.append(f"Severity Level 2 diajukan dengan lama rawat inap singkat ({los} hari) tanpa prosedur medis penunjang.")

        return min(1.0, score), reasons

    # =========================================================================
    # KLASTER 6: Kesesuaian Profil Faskes & Hak Kelas Rawat (Hospital Capability)
    # =========================================================================
    def _check_hospital_capability(self, tipe_rs: str, jenis_rs: str, proc: str):
        score = 0.0
        reasons = []
        regulasi = []
        recomms = []

        proc_str = str(proc).strip().lower()
        jenis_upper = str(jenis_rs).strip().upper()
        tipe_upper = str(tipe_rs).strip().upper()

        # Prosedur subspesialistik canggih bedah saraf / jantung
        is_neurosurgery = any(p in proc_str for p in ["01.24", "01.2", "kraniotomi", "trepanasi", "bedah saraf kepala"])
        is_cardio_advanced = any(p in proc_str for p in ["36.1", "35.", "36.06", "kateterisasi jantung", "cabg", "bedah jantung terbuka"])

        is_restricted_hospital = (
            "BERSALIN" in jenis_upper or "RSIA" in jenis_upper or "IBU DAN ANAK" in jenis_upper or
            "JIWA" in jenis_upper or "MATA" in jenis_upper or "KLINIK" in jenis_upper or "KELAS D" in tipe_upper
        )

        if (is_neurosurgery or is_cardio_advanced) and is_restricted_hospital:
            score = 0.95
            reasons.append(
                f"Ketidaksesuaian Kewenangan Sarana Faskes: Penagihan tindakan bedah canggih ({proc}) di faskes tipe '{tipe_rs} / {jenis_rs}' "
                f"yang tidak memiliki izin sarana kamar operasi steril bertekanan negatif atau dokter sub-spesialis terkait."
            )
            reasons.append("Variabel DIAG_HOSPITAL_TYPE_MISMATCH = 1: Melanggar batas izin operasional dan kompetensi kelas faskes.")
            regulasi = [
                "Permenkes No. 3 Tahun 2020 Pasal 7 s.d. 18: Standar klasifikasi rumah sakit, perizinan kamar operasi, dan ketenagaan medis sub-spesialis.",
                "Permenkes No. 16 Tahun 2019 Pasal 4 Ayat (1) Huruf d: Penagihan klaim atas pelayanan yang tidak memenuhi syarat kompetensi atau izin sarana."
            ]
            recomms = [
                "BLOKIR KLAIM SECARA PERMANEN pada sistem VClaim.",
                "Terbitkan Berita Acara Pemeriksaan (BAP) dan alihkan ke Tim SIGAP / Satgas Anti-Fraud BPJS Kesehatan.",
                "Lakukan audit investigasi fisik terhadap fasilitas kamar operasi dan lisensi SIP dokter DPJP bersangkutan."
            ]

        return score, reasons, regulasi, recomms

    # =========================================================================
    # MODUL DETEKSI TEMPORAL & SPATIAL (Unbundling & Phantom)
    # =========================================================================
    def _check_unbundling(self, pelayanan: str, los: int, proc: str, hari_sejak_kunjungan: int, is_emergency: bool = False, is_same_organ: bool = True):
        score = 0.0
        reasons = []

        if is_emergency or not is_same_organ:
            return 0.0, []

        if hari_sejak_kunjungan <= 2 and hari_sejak_kunjungan > 0:
            score += 0.75
            reasons.append(f"Terdeteksi kunjungan berulang untuk pasien yang sama dalam interval {hari_sejak_kunjungan} hari (< 48 jam) untuk episode perawatan serumpun.")
            if proc not in ["-", "", "nan"]:
                reasons.append(f"Prosedur {proc} seharusnya digabungkan dalam satu paket episode rawat terpadu.")
        elif hari_sejak_kunjungan <= 7 and los <= 1:
            score += 0.50
            reasons.append(f"Pola kunjungan berulang singkat ({hari_sejak_kunjungan} hari) terindikasi sebagai pemecahan siklus terapi rawat jalan/inap.")

        return min(1.0, score), reasons

    def _check_phantom_billing(self, pelayanan: str, los: int, riil: float, tagih: float, is_deceased: bool = False):
        score = 0.0
        reasons = []

        if is_deceased:
            return 0.0, []

        if pelayanan == "RITL" and los == 0:
            score += 0.85
            reasons.append("Klaim diajukan sebagai Rawat Inap Tingkat Lanjut (RITL) namun lama rawat tercatat 0 Hari (pulang di hari yang sama tanpa alasan medis darurat).")
            if riil == 0 or riil < 500000:
                score += 0.15
                reasons.append(f"Biaya riil obat/tindakan faskes tercatat sangat minim atau Rp {int(riil):,}, mengindikasikan pelayanan rawat inap fiktif / tagihan administratif semu.")
        elif tagih > 10000000 and riil == 0:
            score += 0.90
            reasons.append("Tagihan klaim bernilai tinggi namun rincian pengeluaran riil faskes bernilai Rp 0.")

        return min(1.0, score), reasons

    # =========================================================================
    # EXPLAINABLE AI: TreeSHAP-Inspired Feature Contribution Breakdown
    # =========================================================================
    def _calculate_shap_contributions(self, feature_scores: Dict[str, float], is_fraud: int = 1) -> List[Dict[str, Any]]:
        labels_map = {
            "special_cmg_topup": "Top-Up Special CMG (SP/RR/SI/SD)",
            "coding_drift": "Disparitas Diagnosis IGD vs Pulang",
            "cost_velocity": "Cost Velocity Ratio per Hari",
            "referral_integrity": "Integritas Rujukan Berjenjang",
            "hospital_capability": "Kesesuaian Tipe & Sarana Faskes",
            "comorbid_padding": "Validasi CC/MCC & Padding",
            "upcoding_matrix": "Severity Level vs Tindakan",
            "unbundling_temporal": "Interval Kunjungan Berulang",
            "phantom_los": "Kesesuaian Lama Rawat (LOS 0 Hari)"
        }

        active_items = {k: v for k, v in feature_scores.items() if v > 0}
        total_sum = sum(active_items.values())

        contributions = []
        if total_sum > 0:
            for k, val in sorted(active_items.items(), key=lambda x: x[1], reverse=True):
                pct = round((val / total_sum) * 100, 1)
                contributions.append({
                    "feature_key": k,
                    "feature_name": labels_map.get(k, k),
                    "raw_score": round(val, 3),
                    "contribution_pct": pct,
                    "impact": "HIGH" if pct >= 30 else ("MEDIUM" if pct >= 15 else "LOW")
                })
        else:
            contributions.append({
                "feature_key": "clinical_coherence",
                "feature_name": "Koherensi Klinis & Kepatuhan INA-CBG",
                "raw_score": 0.0,
                "contribution_pct": 100.0,
                "impact": "NORMAL"
            })

        return contributions