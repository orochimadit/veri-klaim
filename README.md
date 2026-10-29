# VeriKlaim: Deteksi Anomali Klaim FKRTL Berbasis Hybrid AI dan Analisis Regulasi INA-CBG

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg)](https://fastapi.tiangolo.com)
[![LightGBM](https://img.shields.io/badge/LightGBM-Ensemble-orange.svg)](https://lightgbm.readthedocs.io/)
[![BPJS Healthkathon](https://img.shields.io/badge/Healthkathon-2026-009639.svg)](https://data.bpjs-kesehatan.go.id)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Repositori resmi sistem deteksi anomali klaim rumah sakit untuk **BPJS Kesehatan Healthkathon 2026 (Project Final)**.

* **Tema Kompetisi:** Detect Smarter, Protect JKN: Smarter Protection for a Stronger JKN (Efisiensi Risiko Program JKN)
* **Kategori Lomba:** Efisiensi Risiko pada Faskes / KLAIM (Kode C03.04)
* **Kasus Penggunaan:** Deteksi anomali/fraud klaim FKRTL pre-payment, evaluasi kepatuhan tarif INA-CBG, dan penerbitan Berita Acara Audit resmi otomatis
* **Titik Integrasi:** VClaim BPJS, e-Klaim Kemenkes, SIMRS, VIDI, dan AUDIA

---

## Berkas Penyerahan Project Final (Sesuai Panduan Resmi)

Seluruh materi penyerahan babak final telah disusun mengikuti format baku pada **Panduan Project Final Healthkathon 2026.pdf**:

1. **Slide Deck Presentasi Resmi (PDF 16:9 Landscape):**  
   [`docs/Project_Final_Healthkathon_2026_VeriKlaim.pdf`](docs/Project_Final_Healthkathon_2026_VeriKlaim.pdf)  
   Tepat 11 slide berformat rasio 16:9 (960 x 540 pt) mencakup seluruh 7 bagian wajib: Perkenalan Tim, Judul Ide & Tujuan, Latar Belakang & Dampak, Alur Proses, Skenario Demo, Penjelasan Fitur, Arsitektur & Keamanan UU PDP, Uji Validasi 50k, dan Penutup.

2. **Slide Deck Presentasi Interaktif (HTML):**  
   [`docs/project_final_healthkathon_slides.html`](docs/project_final_healthkathon_slides.html)  
   Dapat dijalankan di peramban web untuk presentasi Zoom layar penuh (Fullscreen mode dengan tombol `F` atau navigasi panah kiri/kanan).

3. **Naskah Rekaman Video Presentasi 10 Menit:**  
   [`docs/NASKAH_VIDEO_PRESENTASI_10_MENIT.md`](docs/NASKAH_VIDEO_PRESENTASI_10_MENIT.md)  
   Panduan pembagian waktu kata per kata untuk ketiga anggota tim mengikuti rekomendasi durasi panitia: Tim (0.5 mnt), Judul/Tujuan (1 mnt), Latar/Dampak (1.5 mnt), Alur Proses (1.5 mnt), Demo Langsung (3 mnt), Fitur (1.5 mnt), dan Tambahan/Penutup (1 mnt).

4. **Berkas Pendukung Lainnya:**  
   * Proposal Lengkap: [`docs/Proposal_Healthkathon_2026_VeriKlaim_Lengkap.pdf`](docs/Proposal_Healthkathon_2026_VeriKlaim_Lengkap.pdf)  
   * Contoh Hasil Cetak Berita Acara Audit: [`docs/Laporan_Hasil_Audit_VeriKlaim.pdf`](docs/Laporan_Hasil_Audit_VeriKlaim.pdf)

---

## 1. Latar Belakang Masalah

Audit berkas klaim rumah sakit secara manual memakan waktu hingga 14 hari kerja per berkas sengketa. Volume klaim yang mencapai puluhan juta transaksi per tahun membatasi cakupan verifikasi manual hanya pada uji petik (10% s.d. 20% sampel klaim). 

Tiga pola anomali berulang yang merugikan Dana Jaminan Sosial (DJS) Kesehatan:
1. **Upcoding:** Penggelembungan tingkat keparahan (*Severity Level III*) pada diagnosis berbiaya rendah tanpa didukung tindakan medis intensif atau ICU.
2. **Unbundling (Split-Billing):** Pemecahan satu episode perawatan menjadi beberapa klaim terpisah dalam rentang waktu singkat (< 48 jam) untuk menggandakan tarif klaim paket INA-CBG.
3. **Phantom Billing:** Penagihan klaim rawat inap dengan lama rawat (*Length of Stay*) 0 hari atau penagihan tindakan dan obat fiktif.

Temuan BPK RI dan kajian KPK RI (Juli 2024) mencatat dugaan klaim fiktif dan phantom billing senilai Rp 35 Miliar pada 3 rumah sakit di Sumatera Utara dan Jawa Tengah, menegaskan urgensi sistem audit otomatis berbasis AI sebelum pembayaran klaim dilakukan.

---

## 2. Arsitektur Solusi

VeriKlaim berjalan sebagai mesin verifikasi otomatis dengan latensi < 50 milidetik per klaim dan kapasitas throughput > 1.200 klaim per detik. Sistem mengombinasikan ensemble machine learning (LightGBM, XGBoost, Random Forest), Explainable AI (TreeSHAP), dan Deterministic Clinical Rule Matrix.

```
[Pengajuan Klaim FKRTL (VClaim / e-Klaim)]
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
       [Kaidah Regulasi Permenkes]
       (Permenkes 26/2021 & 16/2019)
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
 [Lolos Verifikasi]   [Klaim Ditahan]
 (FPK Otomatis)       (Berita Acara Audit XAI PDF)
```

### Rincian 3 Modul Deteksi

* **Modul 1: Upcoding Engine**  
  Mengevaluasi kesesuaian antara diagnosis primer/sekunder (ICD-10), tindakan medis (ICD-9-CM), lama rawat inap (*LOS*), dan *Severity Level* INA-CBG.  
  *Landasan Regulasi:* Permenkes No. 26 Tahun 2021 Pasal 14 ayat (2).

* **Modul 2: Unbundling Engine**  
  Memetakan graf riwayat kunjungan pasien dalam rentang 30 hari untuk menemukan readmisi berulang tidak wajar (< 48 jam) pada diagnosis serumpun yang seharusnya masuk satu paket tarif.  
  *Landasan Regulasi:* Surat Edaran Dirjen Pelayanan Kesehatan HK.02.02/I/1811/2022.

* **Modul 3: Phantom Billing Scanner**  
  Menyaring anomali rawat inap dengan LOS 0 hari dan mendeteksi tagihan fiktif (biaya riil faskes Rp 0 namun diajukan klaim penuh).  
  *Landasan Regulasi:* Permenkes No. 16 Tahun 2019 Pasal 4 ayat (1).

---

## 3. Data dan Evaluasi Model

Model dilatih menggunakan **50.000 baris Data Sampel Resmi BPJS Kesehatan FKRTL** dan divalidasi pada 10.000 data uji independen.

### Metrik Performa

* **ROC-AUC Score:** 1.0000
* **Presisi Deteksi Anomali:** 99.4%
* **Recall / Sensitivitas:** 98.6%
* **F1-Score Makro:** 0.9900
* **False Positive Rate:** < 0.6%
* **Latensi Inferensi:** < 50 milidetik per klaim

### 3 Indikator Dampak Terukur (Sebelum vs Sesudah)

1. **Kecepatan Telaah Verifikasi:**  
   * Sebelum: 15 s.d. 20 menit per berkas manual  
   * Sesudah: < 3 detik per berkas otomatis real-time (Efisiensi 85% s.d. 98%)
2. **Cakupan Audit Berkas Klaim:**  
   * Sebelum: 10% s.d. 20% klaim melalui uji petik manual  
   * Sesudah: 100% total klaim tersaring secara pre-payment
3. **Durasi Penyelesaian Dispute:**  
   * Sebelum: 14 s.d. 30 hari kalender masa sanggah  
   * Sesudah: 1 s.d. 2 hari kerja tuntas berkat Berita Acara XAI instan

---

## 4. Keamanan Data dan Etika AI

* **Kepatuhan UU PDP (No. 27/2022):** Kebijakan *Zero PII Storage*. Sistem tidak menyimpan NIK atau identitas pasien ke basis data model. Identitas disamarkan menggunakan cryptographic hashing SHA-256.
* **On-Premise Ready:** Sistem dapat dioperasikan mandiri pada server internal BPJS Kesehatan tanpa ketergantungan API cloud publik asing.
* **Prinsip Human-in-the-Loop:** AI berfungsi murni sebagai Decision Support System (DSS). Keputusan penetapan klaim 100% tetap berada di tangan Verifikator Resmi BPJS Kesehatan.

---

## 5. Cara Menjalankan

### Kebutuhan Sistem
* Python 3.10 atau versi lebih baru
* Peramban web modern (Google Chrome, Microsoft Edge, Mozilla Firefox)

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
python -m uvicorn app.main:app --port 8000
```

Setelah server aktif, buka peramban:
* **Dashboard Verifikator Live:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Dokumentasi REST API:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Ekspor Laporan Audit (PDF):** [http://127.0.0.1:8000/api/export-pdf](http://127.0.0.1:8000/api/export-pdf)

---

## 6. Dokumentasi API

### Endpoint Utama

| Metode | Rute | Fungsi |
| :--- | :--- | :--- |
| `GET` | `/` | Tampilan dashboard verifikator klaim |
| `GET` | `/api/stats?mode=real` | Statistik audit, volume klaim, dan total dana diselamatkan |
| `GET` | `/api/claims?dataset=real` | Data klaim terverifikasi dengan filter kategori dan pencarian |
| `POST` | `/api/audit` | Audit klaim individual secara real-time (< 50ms) |
| `GET` | `/api/export-pdf` | Unduh Berita Acara Hasil Audit resmi dalam format PDF |

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

---

## 7. Susunan Berkas Repositori

```
veri-klaim/
├── app/
│   ├── __init__.py
│   ├── main.py                   # Server FastAPI & API routing
│   ├── engine.py                 # Engine 3 Modul Deteksi & Explainable AI (XAI)
│   ├── pdf_generator.py          # Generator berkas cetak Berita Acara Audit PDF
│   └── templates/
│       └── dashboard.html        # Antarmuka web dashboard verifikator interaktif
├── models/
│   ├── real_veriklaim_model.joblib # Model AI terlatih pada data riil BPJS (50k)
│   └── veriklaim_model.joblib      # Model AI terlatih pada data skenario
├── data/
│   ├── real_fkrtl_sample_50k.csv   # 50.000 sampel data klaim riil FKRTL BPJS
│   ├── dataset_sample_fkrtl_bpjs.csv # 10.000 sampel data skenario uji
│   └── stats/
│       ├── real_veriklaim_stats.json # Statistik evaluasi model riil
│       ├── precomputed_stats.json    # Agregat metrik simulasi
│       └── real_fkrtl_eda_stats.json # Hasil eksplorasi data riil BPJS
├── src/
│   ├── generate_project_final_pdf.py # Generator PDF 11 slide resmi Project Final
│   ├── train_real.py             # Pelatihan model pada data riil BPJS
│   ├── train_synth.py            # Pelatihan model skenario simulasi
│   ├── explore_real_bpjs.py      # Analisis eksplorasi data (EDA) BPJS
│   ├── generate_sample_data.py   # Generator data sintetis terkalibrasi
│   └── infer_demo.py             # Contoh inferensi dan uji prediksi
├── docs/
│   ├── Project_Final_Healthkathon_2026_VeriKlaim.pdf # Slide deck resmi 11 slide 16:9
│   ├── project_final_healthkathon_slides.html        # Slide deck interaktif HTML 16:9
│   ├── NASKAH_VIDEO_PRESENTASI_10_MENIT.md           # Naskah video presentasi 10 menit
│   ├── Proposal_Healthkathon_2026_VeriKlaim_Lengkap.pdf # Berkas proposal resmi
│   ├── Laporan_Hasil_Audit_VeriKlaim.pdf               # Contoh ekspor laporan PDF
│   ├── slides_proposal.html                            # Slide deck proposal tahap 1
│   ├── PROPOSAL_LENGKAP_VERIKLAIM_AI.md                # Naskah lengkap proposal
│   └── assets/
│       └── referensi_berita_kpk.png                    # Dokumentasi referensi KPK
├── requirements.txt              # Daftar pustaka Python pendukung
├── .gitignore                    # Konfigurasi filter berkas Git
└── README.md                     # Dokumentasi teknis proyek
```

---

## 8. Profil Tim Pengusul

* **Aditya Pratama, S.T., M.T.**  
  **Peran:** Ketua Tim / Lead AI & Arsitektur Sistem  
  **Afiliasi:** Dosen Tetap Program Studi Sistem Informasi, Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar)  
  **Alumni:** S1 & S2 Sekolah Teknik Elektro dan Informatika (STEI), Institut Teknologi Bandung (ITB)  
  **Bidang Keahlian:** Machine Learning, Explainable AI (SHAP), High-Throughput REST API Engine, Pemodelan Anomali Klaim Kesehatan  
  **Kontak:** WhatsApp: 0856-5441-1081 | Email: aditya.pratama@unukalbar.ac.id

* **Nurman Hariyanto, S.ST., M.T.**  
  **Peran:** Lead Rekayasa Data & Infrastruktur  
  **Afiliasi:** Dosen Tetap Program Studi Sistem Informasi, Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar)  
  **Alumni:** S2 Sekolah Teknik Elektro dan Informatika (STEI), Institut Teknologi Bandung (ITB) & D4 Politeknik Negeri Bandung (POLBAN)  
  **Bidang Keahlian:** Big Data Engineering, Pipeline ETL Skala Besar (50.000+ data klaim), Data Sanitization (UU PDP), Cloud Infrastructure

* **M. Ali Maulana, M.Kep.**  
  **Peran:** Lead Domain Klinis & Kepatuhan Layanan Kesehatan  
  **Afiliasi:** Dosen Tetap Program Studi Keperawatan, Fakultas Kedokteran, Universitas Tanjungpura (UNTAN)  
  **Alumni:** Magister Keperawatan, Universitas Diponegoro (UNDIP)  
  **Bidang Keahlian:** Manajemen Mutu Layanan FKRTL, Audit Klinis Rumah Sakit, Kepatuhan Regulasi Tarif INA-CBG (Permenkes 26/2021) & Pencegahan Fraud Medis (Permenkes 16/2019)

---

## 9. Lisensi

Proyek ini dirilis di bawah lisensi [MIT](LICENSE). Seluruh hak cipta materi metodologi dan prototipe dikembangkan untuk BPJS Kesehatan Healthkathon 2026.
