# VeriKlaim: Deteksi Anomali Klaim FKRTL Berbasis Ensemble AI dan Analisis Graf

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg)](https://fastapi.tiangolo.com)
[![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble-orange.svg)](https://xgboost.readthedocs.io/)
[![BPJS Healthkathon](https://img.shields.io/badge/Healthkathon-2026-009639.svg)](https://data.bpjs-kesehatan.go.id)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Repositori sistem deteksi anomali klaim rumah sakit untuk BPJS Kesehatan Healthkathon 2026.

* **Kategori Lomba:** Klaim (Kode C03.04)
* **Kasus Penggunaan:** Deteksi anomali/fraud klaim dan verifikasi kesesuaian dokumen resume medis (RME)
* **Titik Integrasi:** VClaim, VIDI, SIGAP, AUDIA, dan Dashboard EMR

---

## 1. Masalah

Audit berkas klaim rumah sakit secara manual memakan waktu hingga 14 hari kerja per berkas. Volume klaim yang mencapai lebih dari 1 juta transaksi per hari menciptakan celah verifikasi. 

Tiga pola anomali berulang yang merugikan Dana Jaminan Sosial (DJS):
1. **Upcoding:** Penggelembungan tingkat keparahan (*Severity Level III*) pada diagnosis berbiaya rendah tanpa didukung tindakan medis intensif atau ICU.
2. **Unbundling (Split-Billing):** Pemecahan satu episode perawatan menjadi beberapa klaim terpisah dalam rentang waktu singkat (< 48 jam) untuk menggandakan tarif klaim paket INA-CBG.
3. **Phantom Billing:** Penagihan klaim rawat inap dengan lama rawat (*Length of Stay*) 0 hari atau biaya obat/tindakan fiktif.

---

## 2. Arsitektur Solusi

VeriKlaim berjalan sebagai mesin verifikasi otomatis dengan latensi < 15 milidetik per klaim. Sistem mengombinasikan supervised learning (XGBoost), unsupervised learning (Isolation Forest), dan analisis graf riwayat kunjungan pasien.

```
[Pengajuan Klaim RS (VClaim / RME)]
                 │
                 ▼
       [VeriKlaim Engine]
                 │
  ┌──────────────┼──────────────┐
  ▼              ▼              ▼
Modul 1:       Modul 2:       Modul 3:
Upcoding       Unbundling     Phantom Billing
(ICD-10 vs     (Graf Waktu    (Filter LOS 0 Hari
 INA-CBG)       < 30 Hari)     & Outlier Biaya)
  │              │              │
  └──────────────┼──────────────┘
                 ▼
     [Kaidah & Regulasi Permenkes]
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
[Lolos Verifikasi]   [Klaim Ditahan]
(FPK Otomatis)       (Koreksi Tarif / Audit VIDI)
```

### Rincian 3 Modul Deteksi

* **Modul 1: Upcoding Engine**  
  Mengevaluasi kesesuaian antara diagnosis primer/sekunder (ICD-10), tindakan medis (ICD-9-CM), lama rawat inap (*LOS*), dan *Severity Level* INA-CBG.  
  *Landasan Regulasi:* Permenkes No. 26 Tahun 2021 Pasal 14.

* **Modul 2: Unbundling Engine**  
  Memetakan graf riwayat kunjungan pasien (`PSTV01`) dalam rentang 30 hari untuk menemukan readmisi berulang tidak wajar (< 48 jam) pada diagnosis serumpun.  
  *Landasan Regulasi:* Surat Edaran Dirjen Pelayanan Kesehatan HK.02.02/I/1811/2022.

* **Modul 3: Phantom Billing Scanner**  
  Menyaring anomali rawat inap dengan LOS 0 hari dan mendeteksi tagihan obat fiktif (biaya riil faskes Rp 0 namun diajukan klaim penuh).  
  *Landasan Regulasi:* Permenkes No. 16 Tahun 2019 Pasal 4 Ayat 1.

---

## 3. Data dan Evaluasi Model

Model dilatih menggunakan **50.000 baris Data Sampel Resmi BPJS Kesehatan FKRTL 2024** dan divalidasi pada 10.000 data uji independen.

### Metrik Performa

* **ROC-AUC Score:** 1.0000
* **Presisi Deteksi Anomali:** 96.0%
* **Recall / Sensitivitas:** 100.0%
* **Latensi Inferensi:** < 15 milidetik per klaim

### Temuan pada Data Sampel BPJS FKRTL 2024

1. **Jejak Pemotongan Klaim Riil:** Terdeteksi 103 klaim di mana verifikator BPJS memotong tagihan RS dengan total koreksi selisih Rp 120.504.356 (kasus terbanyak: ISPA, Infeksi Virus, Tifoid, dan Dispepsia).
2. **Rawat Inap LOS 0 Hari:** Ditemukan 71 kasus pasien rawat inap yang pulang pada hari yang sama namun ditagihkan klaim paket rawat inap penuh (contoh: SEP `419911224V002625` senilai Rp 2.223.200).
3. **Upcoding Tingkat Berat:** Teridentifikasi kasus diabetes koma Severity III bernilai Rp 33.456.700 dengan lama rawat hanya 1 hari tanpa prosedur kompleks (SEP `92660224V000918`).

---

## 4. Cara Menjalankan

### Kebutuhan Sistem
* Python 3.10 atau versi lebih baru
* Git

### Instalasi dan Eksekusi

```bash
# 1. Kloning repositori
git clone https://github.com/orochimadit/veri-klaim.git
cd veri-klaim

# 2. Buat lingkungan virtual Python
python -m venv .venv

# 3. Aktivasi lingkungan virtual
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 4. Pasang dependensi
pip install -r requirements.txt

# 5. Jalankan server aplikasi
python app.py
```

Setelah server aktif, buka peramban:
* **Dashboard Verifikator:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Dokumentasi REST API:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Ekspor Laporan Audit (PDF):** [http://127.0.0.1:8000/api/export-pdf](http://127.0.0.1:8000/api/export-pdf)

---

## 5. Dokumentasi API

### Endpoint Utama

| Metode | Rute | Fungsi |
| :--- | :--- | :--- |
| `GET` | `/` | Tampilan dashboard verifikator klaim |
| `GET` | `/api/stats?mode=real` | Statistik audit, volume klaim, dan total dana diselamatkan |
| `GET` | `/api/claims?dataset=real` | Data klaim terverifikasi dengan filter kategori dan pencarian |
| `POST` | `/api/audit` | Audit klaim individual secara real-time |
| `GET` | `/api/export-pdf` | Unduh laporan resmi audit forensik dalam format PDF |

### Contoh Request `POST /api/audit`

```json
{
  "no_sep": "SEP-SIM-2026-0042",
  "id_peserta": "PST-00124",
  "tipe_faskes": "RS Kelas C",
  "pelayanan": "RITL",
  "kode_icd10": "J18.9",
  "nama_diagnosa": "Pneumonia Tidak Spesifik",
  "kode_komorbid": "-",
  "kode_icd9": "-",
  "kode_inacbg": "J-4-16-III",
  "nama_inacbg": "INFEKSI SALURAN PERNAPASAN",
  "severity_level": 3,
  "los_hari": 2,
  "biaya_tagih": 17400000.0,
  "biaya_riil": 3400000.0,
  "kunjungan_terakhir_hari": 999
}
```

### Contoh Response `POST /api/audit`

```json
{
  "no_sep": "SEP-SIM-2026-0042",
  "is_fraud": 1,
  "fraud_type": "UPCODING",
  "status_label": "KLAIM DITAHAN — ANOMALI",
  "risk_score": 95.0,
  "potensi_hemat_idr": 14000000,
  "module_scores": {
    "upcoding_score": 95.0,
    "unbundling_score": 0.0,
    "phantom_score": 0.0
  },
  "audit_findings": [
    "Klaim diajukan pada Severity Level 3 namun lama rawat hanya 2 hari tanpa prosedur bedah intensif pendukung.",
    "Beban biaya riil faskes hanya 19.5% dari nilai klaim INA-CBG yang diajukan."
  ],
  "dasar_regulasi": [
    "Permenkes No. 26 Tahun 2021 Pasal 14: Penetapan Severity Level III wajib didukung bukti penggunaan sumber daya klinis intensif."
  ],
  "rekomendasi_verifikator": [
    "Koreksi klaim: Turunkan Severity Level dari III ke Level I/II sesuai resume medis riil.",
    "Verifikasi lembar instruksi DPJP dan bukti pemeriksaan penunjang."
  ]
}
```

---

## 6. Susunan Berkas Repositori

```
veri-klaim/
├── app.py                             # Server FastAPI dan routing layanan
├── veriklaim_engine.py                # 3 Modul Deteksi dan kaidah regulasi
├── export_audit_pdf.py                # Pembuat berkas cetak laporan audit PDF
├── dashboard.html                     # Antarmuka dashboard verifikator
├── train_real_data_model.py           # Pelatihan model pada data riil BPJS
├── train_veriklaim_model.py           # Pelatihan model skenario simulasi
├── explore_real_bpjs_data.py          # Analisis eksplorasi data (EDA) BPJS
├── real_veriklaim_model.joblib        # Bobot model terlatih data riil 2024
├── veriklaim_model.joblib             # Bobot model skenario simulasi
├── real_fkrtl_sample_50k.csv          # 50.000 sampel data klaim nyata FKRTL
├── dataset_sample_fkrtl_bpjs.csv      # 10.000 sampel data skenario uji
├── precomputed_stats.json             # Agregat metrik simulasi
├── real_veriklaim_stats.json          # Metrik evaluasi model data riil
├── requirements.txt                   # Daftar dependensi Python
├── README.md                          # Dokumentasi teknis sistem
├── Proposal_Healthkathon_2026_VeriKlaim_Lengkap.pdf # Berkas proposal resmi
└── Laporan_Resmi_Audit_VeriKlaim_BPJS.pdf           # Contoh ekspor laporan PDF
```

---

## 7. Tim Pengusul

* **Aditya Pratama, S.T., M.T.**  
  Ketua Tim / Lead AI & Arsitektur Sistem  
  Dosen Program Studi Sistem Informasi, Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar)  
  Alumni Magister Teknik Elektro (Teknologi Informasi), STEI Institut Teknologi Bandung (ITB)  
  Kontak: 0856-5441-1081

* **Nurman Hariyanto, S.ST., M.T.**  
  Lead Rekayasa Data & Infrastruktur  
  Dosen Program Studi Sistem Informasi, Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar)  
  Alumni Magister Teknik Media Digital dan Game, STEI Institut Teknologi Bandung (ITB) / Politeknik Negeri Bandung

* **M. Ali Maulana, M.Kep.**  
  Lead Domain Klinis & Kepatuhan Layanan Kesehatan  
  Dosen Program Studi Keperawatan, Fakultas Kedokteran, Universitas Tanjungpura (UNTAN)

---

## 8. Lisensi

Proyek ini dirilis di bawah lisensi [MIT](LICENSE). Dikembangkan untuk BPJS Kesehatan Healthkathon 2026.
