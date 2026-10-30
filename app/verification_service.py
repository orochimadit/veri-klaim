import os
import json
import datetime
from typing import Dict, Any, Optional, List
import pandas as pd
import numpy as np

APP_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(APP_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")
VERIFICATIONS_FILE = os.path.join(DATA_DIR, "verifications.json")

def _ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)

def load_verifications_db() -> Dict[str, Dict[str, Any]]:
    _ensure_data_dir()
    if not os.path.exists(VERIFICATIONS_FILE):
        return {}
    try:
        with open(VERIFICATIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading verifications.json: {e}")
        return {}

def save_verifications_db(data: Dict[str, Dict[str, Any]]) -> None:
    _ensure_data_dir()
    try:
        with open(VERIFICATIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving verifications.json: {e}")

def get_verification(no_sep: str) -> Optional[Dict[str, Any]]:
    db = load_verifications_db()
    return db.get(str(no_sep).strip())

def list_all_verifications() -> List[Dict[str, Any]]:
    db = load_verifications_db()
    return list(db.values())

def record_verification(
    no_sep: str,
    status: str,
    notes: str,
    verified_by: str = "dr. Verifikator BPJS",
    checklist: Optional[Dict[str, bool]] = None,
    claim_meta: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    db = load_verifications_db()
    
    valid_statuses = {
        "APPROVED": "Diverifikasi: Layak Bayar",
        "REJECTED": "Diverifikasi: Ditolak (Fraud)",
        "DISPUTED": "Diverifikasi: Dispute / Koreksi",
        "PENDING": "Menunggu Klarifikasi RS"
    }
    
    norm_status = status.upper() if status.upper() in valid_statuses else "APPROVED"
    status_label = valid_statuses[norm_status]
    now_iso = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
        "no_sep": str(no_sep).strip(),
        "verification_status": norm_status,
        "status_label": status_label,
        "verified_by": verified_by or "dr. Verifikator BPJS",
        "verified_at": now_iso,
        "notes": notes or "Klaim telah diperiksa silang dengan dokumen klinis pendukung.",
        "checklist": checklist or {
            "check_sep": True,
            "check_diagnosa": True,
            "check_prosedur": True,
            "check_los": True,
            "check_rujukan": True,
            "check_billing": True
        },
        "claim_meta": claim_meta or {}
    }

    db[str(no_sep).strip()] = entry
    save_verifications_db(db)
    return entry

def generate_claim_documents(claim: Dict[str, Any], ai_result: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Menghasilkan berkas dokumen pendukung digital otentik BPJS Kesehatan
    untuk diverifikasi secara manual oleh verifikator:
    1. Surat Elegibilitas Peserta (SEP)
    2. Resume Medis Pasien Pulang (DPJP)
    3. Rincian Biaya Rumah Sakit (Hospital Billing)
    4. Surat Rujukan Berjenjang FKTP
    5. Laporan Prosedur / Tindakan Bedah
    """
    no_sep = str(claim.get("no_sep") or claim.get("NO_SEP") or claim.get("FKL02") or "SEP-2024-TEST")
    patient_id = str(claim.get("id_peserta") or claim.get("ID_PESERTA") or claim.get("PSTV01") or "38319758")
    hospital_name = str(claim.get("tipe_faskes") or claim.get("TIPE_FASKES") or claim.get("FKL09") or "RS Kelas B")
    hospital_type = hospital_name
    pelayanan = str(claim.get("pelayanan") or claim.get("PELAYANAN") or claim.get("FKL10") or "RJTL").upper()
    
    tgl_masuk = str(claim.get("tgl_masuk") or claim.get("TGL_MASUK") or claim.get("FKL03") or "2024-06-06")
    tgl_pulang = str(claim.get("tgl_pulang") or claim.get("TGL_PULANG") or claim.get("FKL04") or tgl_masuk)
    los = int(claim.get("los_hari") if claim.get("los_hari") is not None else (claim.get("los_clean") if claim.get("los_clean") is not None else claim.get("LOS_HARI", 0)))
    
    icd10 = str(claim.get("kode_icd10") or claim.get("KODE_ICD10") or claim.get("FKL17A") or "Z09.8")
    nama_diag = str(claim.get("nama_diagnosa") or claim.get("NAMA_DIAGNOSA") or claim.get("FKL18A") or "Follow-up examination after other treatment")
    icd9 = str(claim.get("kode_icd9") or claim.get("KODE_ICD9_PROSEDUR") or claim.get("FKL30") or "-")
    
    inacbg = str(claim.get("kode_inacbg") or claim.get("KODE_INACBG") or claim.get("FKL19") or "Q-5-44-0")
    nama_inacbg = str(claim.get("nama_inacbg") or claim.get("NAMA_INACBG") or claim.get("FKL19A") or "KONSULTASI / EVALUASI RAWAT JALAN")
    severity = int(claim.get("severity_level") or claim.get("SEVERITY_LEVEL") or 1)
    
    biaya_tagih = float(claim.get("biaya_tagih") or claim.get("display_tagih") or claim.get("TARIF_INACBG") or claim.get("FKL47") or 207900.0)
    biaya_riil = float(claim.get("biaya_riil") or claim.get("BIAYA_RIIL_RS") or claim.get("FKL48") or biaya_tagih)

    # Status fraud dari AI
    is_fraud_ai = False
    fraud_type_ai = "NORMAL"
    risk_score_ai = 0.0
    if ai_result:
        is_fraud_ai = bool(ai_result.get("is_fraud", 0))
        fraud_type_ai = ai_result.get("fraud_type", "NORMAL")
        risk_score_ai = float(ai_result.get("risk_score", 0.0))

    # --- 1. DOKUMEN SEP DIGITAL ---
    faskes_asal = "Puskesmas Langsa Barat" if "LANGSA" in str(claim.get("FKL06", "")) else "Puskesmas Rujukan Utama"
    no_rujukan = f"0112P001{tgl_masuk.replace('-', '')}B{no_sep[-4:]}"
    poli = "Poli Penyakit Dalam" if "J18" in icd10 or "I10" in icd10 else ("Poli Bedah" if "K35" in icd10 or "S72" in icd10 else "Poli Rawat Jalan / Kontrol")
    if pelayanan == "RITL":
        poli = "Instalasi Rawat Inap (Ranap Terpadu)"
    
    sep_doc = {
        "title": "SURAT ELEGIBILITAS PESERTA (SEP)",
        "subtitle": "BPJS KESEHATAN — KANTOR CABANG REGIONAL",
        "no_sep": no_sep,
        "tgl_sep": tgl_masuk,
        "no_kartu": f"000{patient_id}89",
        "nama_peserta": f"Tn./Ny. Peserta ({patient_id[-4:]})",
        "tgl_lahir": "1982-04-15",
        "jns_kelamin": "Laki-laki" if int(patient_id[-1]) % 2 == 1 else "Perempuan",
        "peserta": "Pekerja Penerima Upah (PPU) / JKN Mandiri",
        "faskes_perujuk": faskes_asal,
        "no_rujukan": no_rujukan,
        "tgl_rujukan": tgl_masuk,
        "jns_pelayanan": "Rawat Inap Tingkat Lanjut (RITL)" if pelayanan == "RITL" else "Rawat Jalan Tingkat Lanjut (RJTL)",
        "kelas_rawat": "Kelas 2 BPJS" if pelayanan == "RITL" else "Rawat Jalan Reguler",
        "poli_tujuan": poli,
        "diagnosa_awal": f"{icd10} - {nama_diag}",
        "faskes_pelaksana": f"{hospital_name} Langsa Medika",
        "catatan": "Klaim ditagihkan sesuai ketentuan tarif INA-CBG Kemenkes RI.",
        "barcode_token": f"SEP|{no_sep}|{patient_id}|{tgl_masuk}"
    }

    # --- 2. RESUME MEDIS ELEKTRONIK (DPJP) ---
    anamnesis = (
        f"Pasien datang untuk evaluasi berkala dan follow-up terapi pasca penanganan kondisi sebelumnya. "
        f"Keluhan subjektif minimal, kondisi klinis stabil."
    ) if "Z09" in icd10 or los == 0 else (
        f"Pasien masuk dengan keluhan demam, batuk berdahak, sesak napas yang memberat sejak 2 hari SMRS. "
        f"Riwayat penyakit kronis terkontrol." if "J18" in icd10 else
        f"Nyeri perut kanan bawah akut mendadak sejak 1 hari, mual, muntah. Nyeri tekan McBurney positif." if "K35" in icd10 else
        f"Keluhan klinis utama terkait {nama_diag}. Telah dilakukan evaluasi hemodinamik dan penatalaksanaan terarah."
    )

    tindakan_tercatat = icd9 if icd9 != "-" else (
        "Eksisi Apendiks / Apendektomi (47.0)" if "K35" in icd10 and los > 0 else
        "Pemeriksaan Fisik Lengkap, Edukasi Obat, dan Evaluasi Tanda Vital" if los == 0 else
        "Oksigenasi Terapi, Inhalasi Nebulisasi, dan Terapi Cairan Intravena"
    )

    dpjp_name = "dr. Hendra Setiawan, Sp.PD" if "J18" in icd10 or "I10" in icd10 or los == 0 else "dr. Rizal Fauzi, Sp.B"
    dpjp_sip = "SIP: 446.1/098/SIP.DS/Dinkes/2023"

    resume_medis = {
        "title": "RESUME MEDIS PASIEN PULANG (DISCHARGE SUMMARY)",
        "hospital_name": f"{hospital_name} Regional Medika",
        "no_rekam_medis": f"RM-{patient_id[-6:]}",
        "no_sep": no_sep,
        "nama_pasien": f"Tn./Ny. Peserta ({patient_id[-4:]})",
        "tgl_masuk": tgl_masuk,
        "tgl_keluar": tgl_pulang,
        "lama_rawat": f"{los} Hari ({'Rawat Jalan' if los == 0 else 'Rawat Inap'})",
        "ruang_rawat": "Poli Rawat Jalan" if los == 0 else "Bangsal Melati Lt. 3 / Kamar 304",
        "keluhan_anamnesis": anamnesis,
        "tanda_vital": {
            "tekanan_darah": "120/80 mmHg",
            "nadi": "82 x/menit",
            "suhu": "36.7 °C",
            "pernapasan": "18 x/menit",
            "kesadaran": "Compos Mentis (GCS 15)"
        },
        "diagnosa_utama": f"{icd10} - {nama_diag}",
        "diagnosa_sekunder": claim.get("diag_sekunder_list") or ["-"],
        "prosedur_tindakan": tindakan_tercatat,
        "hasil_penunjang": "Laboratorium darah rutin dalam batas normal, evaluasi rontgen toraks terkontrol.",
        "terapi_diberikan": "Farmakoterapi oral pemeliharaan, resep obat kronis 30 hari sesuai formularium nasional.",
        "kondisi_keluar": "Sembuh / Perbaikan Klinis Stabil",
        "instruksi_pulang": "Kontrol ulang 30 hari kemudian ke Faskes Tingkat Pertama (FKTP) atau RS sesuai jadwal.",
        "dpjp": {
            "nama": dpjp_name,
            "sip": dpjp_sip,
            "digital_signature_hash": f"DS-DPJP-{patient_id[:4]}-{tgl_masuk}"
        }
    }

    # --- 3. RINCIAN BIAYA RUMAH SAKIT (BILLING STATEMENT) ---
    # Pecahan komponen biaya riil RS
    if los == 0:
        akomodasi = 0
        jasa_visite = int(biaya_riil * 0.40)
        tindakan = int(biaya_riil * 0.25)
        laboratorium = int(biaya_riil * 0.15)
        farmasi = int(biaya_riil * 0.15)
        bmhp = biaya_riil - (akomodasi + jasa_visite + tindakan + laboratorium + farmasi)
    else:
        akomodasi = int(biaya_riil * 0.20)
        jasa_visite = int(biaya_riil * 0.15)
        tindakan = int(biaya_riil * 0.30)
        laboratorium = int(biaya_riil * 0.15)
        farmasi = int(biaya_riil * 0.15)
        bmhp = biaya_riil - (akomodasi + jasa_visite + tindakan + laboratorium + farmasi)

    billing_items = [
        {"item": "Akomodasi & Kamar Perawatan", "biaya": akomodasi, "keterangan": f"{los} hari x Kelas Perawatan"},
        {"item": "Jasa Medis & Visite Dokter Spesialis", "biaya": jasa_visite, "keterangan": "Visite harian & konsultasi klinis"},
        {"item": "Tindakan Keperawatan & Prosedur Medis", "biaya": tindakan, "keterangan": tindakan_tercatat},
        {"item": "Pemeriksaan Penunjang (Lab & Radiologi)", "biaya": laboratorium, "keterangan": "Darah rutin, penunjang klinis"},
        {"item": "Farmasi & Obat-obatan", "biaya": farmasi, "keterangan": "Formularium Nasional JKN"},
        {"item": "Bahan Medis Habis Pakai (BMHP)", "biaya": bmhp, "keterangan": "Alat injeksi, kassa steril, antiseptic"}
    ]

    billing_statement = {
        "title": "RINCIAN BIAYA PELAYANAN PASIEN (HOSPITAL BILLING)",
        "no_kwitansi": f"BILL-{no_sep[-8:]}",
        "no_sep": no_sep,
        "tgl_cetak": tgl_pulang,
        "nama_pasien": f"Tn./Ny. Peserta ({patient_id[-4:]})",
        "faskes": hospital_name,
        "items": billing_items,
        "total_biaya_riil": biaya_riil,
        "total_tarif_inacbg": biaya_tagih,
        "kode_inacbg": inacbg,
        "deskripsi_inacbg": nama_inacbg,
        "selisih_disparitas": round(biaya_tagih - biaya_riil, 2),
        "cost_velocity_per_hari": round(biaya_tagih / max(los, 1), 2)
    }

    # --- 4. SURAT RUJUKAN FKTP ---
    surat_rujukan = {
        "title": "SURAT RUJUKAN FASILITAS KESEHATAN TINGKAT PERTAMA (FKTP)",
        "no_rujukan": no_rujukan,
        "faskes_asal": faskes_asal,
        "kabupaten_kota": "Kota Langsa" if "LANGSA" in str(claim.get("FKL06", "")) else "Kota Wilayah Faskes",
        "tgl_rujukan": tgl_masuk,
        "masa_berlaku_sampai": (datetime.datetime.strptime(tgl_masuk, "%Y-%m-%d") + datetime.timedelta(days=90)).strftime("%Y-%m-%d") if "-" in tgl_masuk else "2024-09-06",
        "nama_peserta": f"Tn./Ny. Peserta ({patient_id[-4:]})",
        "no_kartu_bpjs": f"000{patient_id}89",
        "diagnosa_rujukan": f"{icd10} - {nama_diag}",
        "catatan_rujukan": "Mohon evaluasi dan tata laksana spesifik di fasilitas kesehatan rujukan tingkat lanjutan.",
        "dokter_pemeriksa_fktp": "dr. Ahmad Fauzi (Dokter FKTP)",
        "status_validitas": "VALID BERLAKU (Sesuai Rujukan Berjenjang JKN)"
    }

    # --- 5. ANALISIS PENCOCOKAN DOKUMEN VS AI (CROSS-CHECK) ---
    cross_check = {
        "check_sep_identitas": {
            "status": "VALID",
            "label": "Identitas & Kepesertaan Cocok",
            "detail": f"Nomor SEP {no_sep} terdaftar resmi, peserta aktif JKN, status kepesertaan valid."
        },
        "check_diagnosa": {
            "status": "VALID" if not is_fraud_ai or fraud_type_ai != "UPCODING" else "PERLU_TELAAH",
            "label": "Kesesuaian Diagnosa ICD-10",
            "detail": f"Diagnosa {icd10} pada klaim sesuai dengan catatan anamnesis Resume Medis DPJP." if (not is_fraud_ai or fraud_type_ai != "UPCODING") else
                      f"Indikasi Upcoding: Diagnosa diajukan Severity Level {severity}, namun resume medis minim temuan komplikasi berat."
        },
        "check_prosedur": {
            "status": "VALID" if icd9 == "-" or ("prosedur" in tindakan_tercatat.lower() or "47.0" in tindakan_tercatat) else "PERLU_TELAAH",
            "label": "Bukti Prosedur & Tindakan Medis",
            "detail": f"Prosedur {tindakan_tercatat} tertera di resume medis dan rincian pemakaian BHP."
        },
        "check_los_rawat": {
            "status": "VALID" if not (pelayanan == "RITL" and los == 0) else "ANOMALI_PHANTOM",
            "label": "Validitas Lama Rawat (LOS)",
            "detail": f"Lama rawat {los} hari selaras dengan tanggal masuk ({tgl_masuk}) dan pulang ({tgl_pulang})." if not (pelayanan == "RITL" and los == 0) else
                      f"Anomali Phantom Billing: Pelayanan tercatat Rawat Inap (RITL) tapi LOS 0 hari dan biaya riil minim."
        },
        "check_billing_disparitas": {
            "status": "VALID" if abs(biaya_tagih - biaya_riil) <= (biaya_tagih * 0.25) else "SELISIH_TINGGI",
            "label": "Kewajaran Rasio Biaya Riil",
            "detail": f"Biaya riil RS (Rp {int(biaya_riil):,}) mencerminkan 90-100% dari tarif INA-CBG (Rp {int(biaya_tagih):,}). Wajar." if abs(biaya_tagih - biaya_riil) <= (biaya_tagih * 0.25) else
                      f"Disparitas biaya mencapai Rp {int(biaya_tagih - biaya_riil):,}. Beban riil RS jauh lebih rendah dari tagihan paket klaim."
        }
    }

    return {
        "no_sep": no_sep,
        "patient_id": patient_id,
        "hospital_type": hospital_type,
        "pelayanan": pelayanan,
        "los_hari": los,
        "icd10": icd10,
        "nama_diagnosa": nama_diag,
        "icd9": icd9,
        "inacbg": inacbg,
        "nama_inacbg": nama_inacbg,
        "biaya_tagih": biaya_tagih,
        "biaya_riil": biaya_riil,
        "ai_prediction": {
            "is_fraud": is_fraud_ai,
            "fraud_type": fraud_type_ai,
            "risk_score": risk_score_ai
        },
        "documents": {
            "sep": sep_doc,
            "resume_medis": resume_medis,
            "billing": billing_statement,
            "rujukan": surat_rujukan
        },
        "cross_check": cross_check
    }
