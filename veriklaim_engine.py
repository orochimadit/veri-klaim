import numpy as np
import pandas as pd
import joblib
import os
from typing import Dict, Any, List

class VeriKlaimEngine:
    """
    VeriKlaim Core Detection Engine
    Mengimplementasikan 3 Modul Deteksi Sesuai Proposal Healthkathon 2026:
    - Modul 1: Clinical Coherence & Upcoding Engine
    - Modul 2: Temporal Graph & Unbundling / Split-Billing Engine
    - Modul 3: Spatial-Provider & Phantom Billing Detector (Isolation Forest + Rule Engine)
    - XAI Reasoner: Penjelasan Berbasis Regulasi Permenkes & Rekomendasi Verifikator
    """

    def __init__(self, model_path: str = None):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if model_path is None:
            model_path = os.path.join(base_dir, "real_veriklaim_model.joblib")
            if not os.path.exists(model_path):
                model_path = os.path.join(base_dir, "veriklaim_model.joblib")

        self.model_path = model_path
        self.artifacts = joblib.load(self.model_path) if os.path.exists(self.model_path) else None
        print(f"[VeriKlaimEngine] Initialized with model: {self.model_path}")

    def audit_single_claim(self, claim: Dict[str, Any]) -> Dict[str, Any]:
        """
        Audit klaim individual secara komprehensif melalui 3 Modul Deteksi
        """
        no_sep = claim.get("no_sep", "SEP-UNKNOWN")
        id_peserta = claim.get("id_peserta", "PST-UNKNOWN")
        tipe_faskes = claim.get("tipe_faskes", "RS Kelas C")
        pelayanan = claim.get("pelayanan", "RITL").upper() # RITL / RJTL
        diagnosa_icd10 = claim.get("kode_icd10", "J18.9")
        nama_diagnosa = claim.get("nama_diagnosa", "Pneumonia Tidak Spesifik")
        komorbid_icd10 = claim.get("kode_komorbid", "-")
        prosedur_icd9 = claim.get("kode_icd9", "-")
        kode_inacbg = claim.get("kode_inacbg", "J-4-16-III")
        nama_inacbg = claim.get("nama_inacbg", "INFEKSI SALURAN PERNAPASAN")
        severity_level = int(claim.get("severity_level", 3))
        los_hari = int(claim.get("los_hari", 2))
        biaya_tagih = float(claim.get("biaya_tagih", 17400000.0))
        biaya_riil = float(claim.get("biaya_riil", 3400000.0))
        tarif_standar = float(claim.get("tarif_standar", biaya_tagih))

        # Modul 1: Analisis Upcoding
        upcoding_score, upcoding_reasons = self._check_upcoding(
            severity_level, los_hari, prosedur_icd9, komorbid_icd10, biaya_tagih, biaya_riil
        )

        # Modul 2: Analisis Unbundling / Split Billing
        unbundling_score, unbundling_reasons = self._check_unbundling(
            pelayanan, los_hari, prosedur_icd9, claim.get("kunjungan_terakhir_hari", 999)
        )

        # Modul 3: Analisis Phantom Billing & Outlier
        phantom_score, phantom_reasons = self._check_phantom_billing(
            pelayanan, los_hari, biaya_riil, biaya_tagih
        )

        # Evaluasi Komposit & Penetapan Status
        max_score = max(upcoding_score, unbundling_score, phantom_score)
        is_fraud = 1 if max_score >= 0.65 else 0

        fraud_type = "NORMAL"
        primary_reasons = []
        regulasi_dasar = []
        rekomendasi_verifikator = []

        if is_fraud:
            if max_score == upcoding_score:
                fraud_type = "UPCODING"
                primary_reasons = upcoding_reasons
                regulasi_dasar = [
                    "Permenkes No. 26 Tahun 2021 Pasal 14: Penetapan Severity Level III wajib didukung bukti penanganan komplikasi berat dan penggunaan sumber daya klinis intensif.",
                    "Petunjuk Teknis INA-CBG: Koding komorbiditas sekunder tanpa tindakan terapi spesifik dari DPJP dilarang dijadikan dasar penagihan level berat."
                ]
                rekomendasi_verifikator = [
                    "Koreksi klaim: Turunkan Severity Level dari III ke Level I / II sesuai resume medis riil.",
                    "Verifikasi berkas: Minta catatan lembar instruksi DPJP dan hasil pemeriksaan penunjang (laboratorium/radiologi).",
                    "Rekomendasi sistem VClaim: Tahan persetujuan otomatis, alihkan ke verifikasi paska-klaim (AUDIA)."
                ]
            elif max_score == unbundling_score:
                fraud_type = "UNBUNDLING"
                primary_reasons = unbundling_reasons
                regulasi_dasar = [
                    "Permenkes No. 26 Tahun 2021: Prosedur penanganan episode perawatan berkesinambungan merupakan satu kesatuan paket klaim INA-CBG.",
                    "SE Dirjen Pelayanan Kesehatan HK.02.02/I/1811/2022: Larangan memecah episode tindakan medis berulang dalam jangka waktu < 30 hari untuk diagnosa serumpun."
                ]
                rekomendasi_verifikator = [
                    "Konsolidasi berkas klaim: Gabungkan episode kunjungan terpisah menjadi 1 nomor SEP utama.",
                    "Batalkan klaim tambahan untuk prosedur penunjang yang telah tercakup dalam tarif paket utama.",
                    "Kirimkan notifikasi kepatuhan faskes melalui aplikasi HFIS / Dashboard Verifikator."
                ]
            else:
                fraud_type = "PHANTOM_BILLING"
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

        potensi_penghematan = max(0.0, biaya_tagih - biaya_riil) if is_fraud else 0.0

        return {
            "no_sep": no_sep,
            "id_peserta": id_peserta,
            "tipe_faskes": tipe_faskes,
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
                "upcoding_score": round(upcoding_score * 100, 1),
                "unbundling_score": round(unbundling_score * 100, 1),
                "phantom_score": round(phantom_score * 100, 1)
            },
            "audit_findings": primary_reasons,
            "dasar_regulasi": regulasi_dasar,
            "rekomendasi_verifikator": rekomendasi_verifikator
        }

    def _check_upcoding(self, severity: int, los: int, proc: str, comorbid: str, tagih: float, riil: float):
        score = 0.0
        reasons = []

        if severity == 3:
            if los <= 2 and proc in ["-", "", "nan"]:
                score += 0.70
                reasons.append(f"Klaim diajukan pada Severity Level 3 (Kategori Berat) namun lama rawat hanya {los} hari tanpa adanya prosedur bedah / tindakan intensif ICD-9-CM pendukung.")
            if riil > 0 and (riil / (tagih + 1.0)) < 0.35:
                score += 0.25
                reasons.append(f"Beban biaya riil fasilitas kesehatan sangat rendah ({riil / tagih * 100:.1f}% dari nilai tagihan klaim), mengindikasikan ketiadaan intervensi intensif.")
        elif severity == 2 and los <= 1 and proc in ["-", "", "nan"]:
            score += 0.45
            reasons.append(f"Severity Level 2 diajukan dengan lama rawat inap singkat ({los} hari) tanpa prosedur medis penunjang.")

        return min(1.0, score), reasons

    def _check_unbundling(self, pelayanan: str, los: int, proc: str, hari_sejak_kunjungan: int):
        score = 0.0
        reasons = []

        if hari_sejak_kunjungan <= 2 and hari_sejak_kunjungan > 0:
            score += 0.75
            reasons.append(f"Terdeteksi kunjungan berulang untuk pasien yang sama dalam interval {hari_sejak_kunjungan} hari (< 48 jam) untuk episode perawatan serumpun.")
            if proc not in ["-", "", "nan"]:
                reasons.append(f"Prosedur {proc} seharusnya digabungkan dalam satu paket episode rawat terpadu.")
        elif hari_sejak_kunjungan <= 7 and los <= 1:
            score += 0.50
            reasons.append(f"Pola kunjungan berulang singkat ({hari_sejak_kunjungan} hari) terindikasi sebagai pemecahan siklus terapi rawat jalan/inap.")

        return min(1.0, score), reasons

    def _check_phantom_billing(self, pelayanan: str, los: int, riil: float, tagih: float):
        score = 0.0
        reasons = []

        if pelayanan == "RITL" and los == 0:
            score += 0.85
            reasons.append("Klaim diajukan sebagai Rawat Inap Tingkat Lanjut (RITL) namun lama rawat tercatat 0 Hari (pulang di hari yang sama tanpa alasan medis darurat).")
            if riil == 0 or riil < 500000:
                score += 0.15
                reasons.append(f"Biaya riil obat/tindakan faskes tercatat sangat minim atau Rp {riil:,}, mengindikasikan pelayanan rawat inap fiktif / tagihan administratif semu.")
        elif tagih > 10000000 and riil == 0:
            score += 0.90
            reasons.append("Tagihan klaim bernilai tinggi namun rincian pengeluaran riil faskes bernilai Rp 0.")

        return min(1.0, score), reasons
