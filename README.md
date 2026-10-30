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

## 2. Arsitektur Solusi & Keunggulan Hasil Tuning Model

VeriKlaim berjalan sebagai mesin verifikasi otomatis berkecepatan tinggi dengan latensi inti **< 0,1 milidetik** per klaim dan throughput **> 415 request per detik**. Sistem mengintegrasikan ensemble machine learning (XGBoost, Isolation Forest), Explainable AI (TreeSHAP), dan Deterministic Clinical Rule Matrix yang telah ditingkatkan (*tune up*) mengacu pada **Blueprint Kemenkes RI**, **Permenkes No. 26 Tahun 2021**, dan **Permenkes No. 16 Tahun 2019**.

```
[Pengajuan Klaim FKRTL (VClaim / e-Klaim / SIMRS)]
                        │
                        ▼
            [VeriKlaim Engine v2.0]
                        │
    ┌───────────────────┼───────────────────┐
    ▼                   ▼                   ▼
Klaster 1 & 2:      Klaster 3 & 4:      Klaster 5 & 6:
Special CMG &       Cost Velocity &     Upcoding Ekstrem &
Coding Drift        Referral Bypass     Mismatch Faskes
    │                   │                   │
    └───────────────────┼───────────────────┘
                        ▼
           [TreeSHAP Explainer & XAI]
      (Dekomposisi Variabel Medis Obyektif)
                        │
                        ▼
  [Workstation Verifikasi Human-in-the-Loop]
   (Cross-check 4 Dokumen Digital oleh Dokter)
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
 [Diverifikasi Layak]         [Diverifikasi Fraud / Dispute]
 (FPK Otomatis Siap Bayar)    (Berita Acara & Rekomendasi Tarif)
```

### 6 Klaster Deteksi Kecurangan Terpadu (Hasil Tuning Blueprint Kemenkes)

1. **Klaster 1: Top-Up Special CMG (SP/RR/SI/SD) Tanpa Prosedur Operasi Utama**  
   Mendeteksi penambahan klaim *Special CMG* berbiaya tinggi (seperti obat sitostatika khusus, implant, atau rehabilitasi medik) padahal pasien tidak menjalani tindakan medis bedah/intervensi yang disyaratkan.  
   *Landasan:* Permenkes No. 26/2021 Lampiran I Bab IV.

2. **Klaster 2: Disparitas Diagnosis Masuk vs Utama (Coding Drift & Diagnosis Padding)**  
   Menganalisis inkonsistensi saat diagnosa awal masuk IGD/Poli berupa keluhan ringan (misal *Dyspepsia* K30), namun saat pulang dinaikkan menjadi diagnosa berat berbiaya mahal (*Gastric Ulcer with Hemorrhage* K25.0) tanpa catatan perkembangan klinis yang valid.  
   *Landasan:* Kaidah Koding ICD-10 & Permenkes No. 26/2021 Pasal 14.

3. **Klaster 3: Anomali Kecepatan Biaya Harian (Cost Velocity Ratio)**  
   Menghitung rasio biaya riil rumah sakit per hari rawat terhadap median standar regional. Mendeteksi klaim yang biaya hariannya melonjak 3 s.d. 7 kali lipat di atas batas wajar kelas faskesnya.  
   *Landasan:* Permenkes No. 16/2019 Pasal 4 Ayat (1) Huruf c.

4. **Klaster 4: Bypassing Rujukan Berjenjang Rawat Jalan Tingkat Lanjut (RJTL)**  
   Menandai kasus-kasus primer berulang yang langsung ditangani di rumah sakit tanpa surat rujukan sah FKTP atau tanpa indikasi gawat darurat medis yang sah.  
   *Landasan:* Permenkes No. 001/2012 & Permenkes No. 26/2021.

5. **Klaster 5: Upcoding Ekstrem Severity Level III Tanpa Terapi Intensif ICU**  
   Mendeteksi klaim berlabel keparahan berat (*Severity Level III / Major Complication*) dengan tagihan puluhan juta rupiah, namun durasi rawat inap hanya 1 hari dan tanpa penggunaan ventilator mekanik atau ruang ICU.  
   *Landasan:* Kaidah Grouping INA-CBG & Standar Pelayanan Medis Kemenkes.

6. **Klaster 6: Mismatch Prosedur Medis Spesialistik vs Klasifikasi Faskes**  
   Memvalidasi kesesuaian antara izin operasional tipe faskes (RS Kelas A, B, C, D atau Khusus) dengan tindakan medis lanjutan (misal tindakan bedah saraf atau kraniotomi yang ditagihkan oleh faskes kelas D atau RS khusus bersalin).  
   *Landasan:* Standar Klasifikasi Rumah Sakit Permenkes No. 14/2021.

---

## 3. Data dan Evaluasi Keunggulan Hasil Tuning Model

Model dilatih menggunakan **50.000 baris Data Sampel Riil FKRTL BPJS Kesehatan** dan diuji secara independen pada **10.000 berkas uji validasi independen** (Automated Test Suite QA AGT-06).

### Keunggulan Metrik Kinerja Hasil Tuning

| Parameter Metrik | Target Standar BPJS | Hasil Capaian VeriKlaim | Evaluasi Kinerja |
| :--- | :---: | :---: | :--- |
| **Recall / Sensitivitas Anomali** | ≥ 95.0% | **100.00%** | **Zero False Negative** (Nol kebocoran klaim fraud) |
| **ROC-AUC Score** | ≥ 0.9500 | **1.0000** | Pemisahan sempurna antara klaim wajar dan anomali |
| **Presisi Deteksi Anomali** | ≥ 90.0% | **96.43%** | Sangat akurat, meminimalisir alarm palsu (*False Alarm*) |
| **Latensi Eksekusi Core Server** | < 15 ms | **0.079 ms** | Rata-rata inferensi sub-milidetik (< 0.1 ms) |
| **Client End-to-End Latency** | < 50 ms | **2.37 ms** | Sangat responsif untuk pemrosesan serentak |
| **Throughput Kapasitas Audit** | > 200 req/s | **415.4 req/s** | Sanggup menyaring 1,49 juta klaim per jam |
| **Transparansi Penjelasan (XAI)** | Kualitatif | **TreeSHAP 100%** | Membeberkan persentase kontribusi fitur numerik per berkas |

### 3 Indikator Dampak Terukur (Sebelum vs Sesudah)

1. **Kecepatan Telaah Verifikasi:**  
   * Sebelum: 15 s.d. 20 menit per berkas manual  
   * Sesudah: **< 1 milidetik** per berkas otomatis real-time (Efisiensi > 99%)
2. **Cakupan Audit Berkas Klaim:**  
   * Sebelum: 10% s.d. 20% klaim melalui uji petik manual  
   * Sesudah: **100% total klaim (50.000+)** tersaring secara pre-payment
3. **Penyelamatan Finansial Nyata:**  
   * Terbukti mengidentifikasi potensi kebocoran klaim senilai **Rp 14,34 Miliar** dari total portofolio klaim bermasalah pada dataset simulasi resmi.

---

## 4. Prinsip Human-in-the-Loop & Keamanan Data (UU PDP)

### Pendekatan Human-in-the-Loop: Dokter Tetap Pemegang Otoritas Final
VeriKlaim mengusung filosofi **AI sebagai Copilot Cerdas Dokter Verifikator**, BUKAN sistem algoritmik yang memutus pembayaran secara otomatis tanpa pengawasan. Seluruh rekomendasi AI disajikan ke dalam **Workstation Verifikasi Manual & Digital Medical Document Viewer**:

1. **Penelaahan 4 Dokumen Klinis Digital Otentik:**  
   Verifikator dapat membuka dan memvalidasi silang (*cross-check*) 4 dokumen pendukung dalam antarmuka terpadu:
   * **Surat Eligibilitas Peserta (SEP) Digital:** Memvalidasi status keaktifan peserta, hak kelas rawat, poli rujukan, dan token barcode.
   * **Resume Medis Pasien Pulang (Discharge Summary DPJP):** Meneliti keluhan klinis, tanda-tanda vital, hasil penunjang, terapi obat, kondisi keluar, dan stempel hash tanda tangan dokter penanggung jawab pelayanan.
   * **Rincian Biaya Rumah Sakit (Hospital Billing Statement):** Membandingkan biaya riil kasir (kamar, visite, farmasi, alat kesehatan) terhadap tarif paket INA-CBG resmi.
   * **Surat Rujukan Berjenjang FKTP:** Memastikan keabsahan rujukan awal dari Puskesmas/Klinik dan validitas masa berlaku rujukan (90 hari).

2. **Panel Validasi Silang Otomatis (Cross-Check 5 Indikator):**  
   Mencocokkan keselarasan antara temuan algoritma AI dan data dokumen rekam medis untuk memudahkan verifikator mengambil kesimpulan.

3. **Formulir Pengesahan Putusan Resmi:**  
   Dokter verifikator menetapkan salah satu dari 4 status putusan definitif:
   * `✅ DIVERIFIKASI: LAYAK BAYAR` (Klaim disetujui untuk diteruskan ke proses pencairan)
   * `🚨 DIVERIFIKASI: DITOLAK / FRAUD` (Klaim ditahan karena terbukti rekayasa atau fiktif)
   * `⚠️ DIVERIFIKASI: DISPUTE KOREKSI` (Penyesuaian tarif klaim sesuai standar yang berlaku)
   * `❓ BUTUH KLARIFIKASI RS` (Meminta kelengkapan bukti penunjang medis dari DPJP RS)

4. **Jejak Audit Digital Permanen (*Audit Trail*):**  
   Setiap putusan, nama verifikator, NIP/SIP, tanggal telaah, dan catatan medis disimpan permanen ke dalam basis data audit untuk akuntabilitas hukum dan transparansi rekonsiliasi bersama rumah sakit.

### Kepatuhan Regulasi & Keamanan Data
* **Kepatuhan UU PDP (No. 27/2022):** Kebijakan *Zero PII Storage*. Identitas peserta disamarkan dengan *cryptographic hashing* SHA-256.
* **Arsitektur Hybrid Zero-Crash:** Saklar mode AI otomatis beralih antara Google Gemini Pro Cloud (analisis semantik mendalam) dan Deterministic Rules Engine Lokal (mode darurat saat koneksi internet terputus).
* **On-Premise Ready:** Sistem dapat dijalankan sepenuhnya di infrastruktur lokal data center BPJS Kesehatan tanpa mengekspor data sensitif ke server eksternal.

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
* **Dokumentasi Swagger REST API:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Buku Panduan Lengkap Fitur (PDF):** [http://127.0.0.1:8000/api/download-feature-guide](http://127.0.0.1:8000/api/download-feature-guide)
* **Ekspor Berita Acara Audit (PDF):** [http://127.0.0.1:8000/api/export-pdf](http://127.0.0.1:8000/api/export-pdf)

---

## 6. Dokumentasi API

Sistem menyediakan antarmuka **Swagger UI interaktif** pada `/docs` yang terbagi ke dalam 5 modul tag terstruktur:

### Endpoint Utama

| Metode | Rute | Tag / Modul | Fungsi |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Antarmuka | Dashboard eksekutif & workstation verifikator klinis |
| `GET` | `/docs` | Dokumentasi | Spesifikasi Swagger API OpenAPI v3 interaktif |
| `GET` | `/api/stats` | Statistik | Agregat KPI keuangan, volume 50.000 klaim & dana diselamatkan |
| `GET` | `/api/claims` | Klaim FKRTL | Pencarian kilat (~20ms), filter tipe anomali & status verifikasi manual |
| `GET` | `/api/claims/{no_sep}/documents` | Human-in-the-Loop | Pengambilan 4 berkas digital klinis (SEP, Resume DPJP, Billing, Rujukan) |
| `POST` | `/api/claims/{no_sep}/verify` | Human-in-the-Loop | Pengesahan putusan resmi dokter verifikator BPJS (Audit Trail) |
| `GET` | `/api/verifications` | Human-in-the-Loop | Rekam jejak riwayat seluruh verifikasi manual yang telah disahkan |
| `POST` | `/api/audit` | Audit & Deteksi AI | Evaluasi forensik klaim individual seketika (< 0.1 ms core execution) |
| `POST` | `/api/system/mode` | Sistem & AI Mode | Saklar mode AI cerdas (Online Gemini Pro vs Offline Rule Engine) |
| `GET` | `/api/export-pdf` | Laporan & Ekspor | Unduh Berita Acara Hasil Audit resmi dalam format PDF |
| `GET` | `/api/download-feature-guide` | Laporan & Ekspor | Unduh Buku Panduan Lengkap Semua Fitur Platform VeriKlaim (PDF) |

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
│   ├── main.py                   # Server FastAPI, API routing & precomputed indexing
│   ├── engine.py                 # Engine 6 Klaster Kemenkes, XGBoost, Isolation Forest & SHAP
│   ├── verification_service.py   # Workstation Human-in-the-Loop & generator 4 dokumen digital
│   ├── llm_collaborator.py       # Kolaborator AI Hybrid (Gemini Pro & Deterministic Fallback)
│   ├── pdf_generator.py          # Generator berkas cetak Berita Acara Audit PDF
│   └── templates/
│       └── dashboard.html        # Antarmuka dashboard (Palet Mobile JKN & Modal Verifikasi)
├── models/
│   ├── real_veriklaim_model.joblib # Model AI terlatih pada 50.000 data riil BPJS
│   └── veriklaim_model.joblib      # Model AI skenario simulasi
├── data/
│   ├── real_fkrtl_sample_50k.csv   # 50.000 sampel data klaim riil FKRTL BPJS
│   ├── dataset_sample_fkrtl_bpjs.csv # 10.000 sampel data skenario uji
│   ├── verifications.json        # Basis data persisten rekam jejak verifikasi manual
│   └── stats/
│       ├── real_veriklaim_stats.json # Statistik evaluasi model riil BPJS
│       ├── precomputed_stats.json    # Agregat metrik simulasi
│       └── real_fkrtl_eda_stats.json # Hasil eksplorasi data riil BPJS
├── src/
│   ├── generate_project_final_pdf.py # Generator PDF 11 slide resmi Project Final
│   ├── train_real.py             # Pelatihan model pada data riil BPJS
│   ├── train_synth.py            # Pelatihan model skenario simulasi
│   ├── explore_real_bpjs.py      # Analisis eksplorasi data (EDA) BPJS
│   ├── generate_sample_data.py   # Generator data sintetis terkalibrasi
│   └── infer_demo.py             # Contoh inferensi dan uji prediksi
├── scripts/
│   └── generate_feature_guide_pdf.py # Generator Buku Panduan Fitur PDF 5 Halaman
├── docs/
│   ├── Project_Final_Healthkathon_2026_VeriKlaim.pdf # Slide deck resmi 11 slide 16:9
│   ├── project_final_healthkathon_slides.html        # Slide deck interaktif HTML 16:9
│   ├── Buku_Panduan_Fitur_Platform_VeriKlaim.pdf     # Buku Panduan Lengkap Fitur Platform PDF
│   ├── Laporan_Hasil_Audit_VeriKlaim.pdf               # Contoh ekspor laporan PDF
│   ├── Proposal_Healthkathon_2026_VeriKlaim_Lengkap.pdf # Berkas proposal resmi
│   ├── NASKAH_VIDEO_PRESENTASI_10_MENIT.md           # Naskah video presentasi 10 menit
│   ├── slides_proposal.html                            # Slide deck proposal tahap 1
│   ├── PROPOSAL_LENGKAP_VERIKLAIM_AI.md                # Naskah lengkap proposal
│   └── assets/
│       ├── referensi_berita_kpk.png                    # Dokumentasi referensi KPK
│       ├── template_p1_img1_Image6.png                 # Aset grafis slide deck
│       └── template_p11_img1_Image6.png                # Aset grafis slide deck
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
