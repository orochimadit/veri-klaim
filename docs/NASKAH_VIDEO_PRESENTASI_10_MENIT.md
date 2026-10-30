# NASKAH PANDUAN REKAMAN VIDEO PRESENTASI (DURASI MAKSIMAL 10 MENIT)
**Healthkathon 2026 BPJS Kesehatan — Project Final (Versi Terkalibrasi & Realistis)**  
*Tema: Detect Smarter, Protect JKN — Smarter Protection for a Stronger JKN (Efisiensi Risiko Program JKN)*  
*Kategori: Efisiensi Risiko pada Faskes / KLAIM (Kode: C03.04)*  
*Nama Solusi: VeriKlaim*  
*Nama Tim: Tim VeriKlaim Kalbar*  

---

## 1. PANDUAN UMUM & CHECKLIST SEBELUM MEREKAM (ZOOM MEETING)
1. **Durasi Total:** Maksimal 10 menit (Target ideal rekaman: 9 menit 30 detik s.d. 9 menit 50 detik).
2. **Platform Perekaman:** Zoom Meeting (Rekomendasi resmi panitia).
   - Pastikan webcam ketiga anggota tim menyala (foto/video wajah tampil jelas).
   - Gunakan fitur *Share Screen* untuk menampilkan slide presentasi (`docs/project_final_healthkathon_slides.html` atau `docs/Project_Final_Healthkathon_2026_VeriKlaim.pdf`) serta browser aktif di `http://127.0.0.1:8000/` saat sesi demo.
3. **Pengaturan YouTube:** Unggah video ke YouTube dengan visibilitas **Unlisted** (Tidak Publik) atau **Private** (pastikan tautan dapat dibuka panitia).
4. **Batas Akhir Submit:** 19 Oktober s.d. 1 November 2026 melalui Dashboard Healthkathon BPJS Kesehatan.

---

## 2. SUSUNAN WAKTU DAN PEMBAGIAN PERAN BICARA

| Menit Ke- | Durasi | Slide Acuan | Bagian Presentasi | Pembicara Utama |
| :--- | :--- | :--- | :--- | :--- |
| **00:00 - 00:30** | 30 detik | Slide 1 & 2 | Cover & Perkenalan 3 Anggota Tim | **Aditya Pratama** |
| **00:30 - 01:30** | 60 detik | Slide 3 | Judul Ide, Nilai Utama, Deskripsi & 3 Tujuan Terukur | **Aditya Pratama** |
| **01:30 - 03:00** | 90 detik | Slide 4 | Latar Belakang Masalah (KPK/BPK) & 3 Indikator Dampak | **M. Ali Maulana** |
| **03:00 - 04:30** | 90 detik | Slide 5 | Alur Proses Aplikasi (Input, Proses, AI, Output, Tindak Lanjut) | **Nurman Hariyanto** |
| **04:30 - 07:30** | 180 detik | Slide 6 & Web | **DEMO LANGSUNG APLIKASI (Live Workstation http://127.0.0.1:8000)** | **Aditya Pratama** |
| **07:30 - 09:00** | 90 detik | Slide 7 | Penjelasan 4 Fitur Utama Solusi | **Nurman Hariyanto** & **M. Ali Maulana** |
| **09:00 - 10:00** | 60 detik | Slide 8 - 11 | Arsitektur, Keamanan PDP, Validasi Realistis & Penutup | **Aditya Pratama** |

---

## 3. NASKAH LENGKAP KATA PER KATA (SCRIPT)

### BAGIAN 1: COVER & PERKENALAN TIM (00:00 - 00:30 | 30 Detik)
**[Tampilkan Slide 1 Cover, lalu Slide 2 Perkenalan Tim]**

> **Aditya Pratama (Ketua Tim):**  
> *"Assalamu’alaikum Warahmatullahi Wabarakatuh, salam sejahtera, dan salam sehat untuk Dewan Juri Healthkathon BPJS Kesehatan 2026.  
> Kami dari **Tim VeriKlaim Kalbar** dengan bangga mempersembahkan solusi kami pada Kategori Efisiensi Risiko pada Faskes/KLAIM: **VeriKlaim — Platform Deteksi Anomali Klaim FKRTL Berbasis 6-Klaster Kemenkes, Explainable AI SHAP, dan Workstation Human-in-the-Loop 4 Dokumen Digital.**  
> Tim kami merupakan kolaborasi lintas disiplin antara AI, Big Data, dan Manajemen Layanan Klinis:  
> 1. Saya sendiri, **Aditya Pratama, S.T., M.T.**, Dosen Program Studi Sistem Informasi Universitas Nahdlatul Ulama Kalimantan Barat, alumni S1 & S2 STEI ITB, bertindak sebagai Ketua Tim dan Lead AI & Arsitektur Sistem.  
> 2. Rekan saya, **Nurman Hariyanto, S.ST., M.T.**, Dosen Sistem Informasi UNU Kalbar, alumni S2 STEI ITB dan Polban, sebagai Lead Rekayasa Data & Infrastruktur.  
> 3. Dan **M. Ali Maulana, M.Kep.**, Dosen Keperawatan Fakultas Kedokteran Universitas Tanjungpura, sebagai Lead Domain Klinis dan Kepatuhan Regulasi Kesehatan."*

---

### BAGIAN 2: JUDUL IDE, DESKRIPSI, DAN TUJUAN (00:30 - 01:30 | 60 Detik)
**[Tampilkan Slide 3: Judul Ide, Deskripsi, dan Tujuan]**

> **Aditya Pratama:**  
> *"Nilai utama dari VeriKlaim dirangkum dalam satu kalimat:  
> **'Solusi ini membantu Verifikator BPJS Kesehatan dan Tim Pengendali Fraud Faskes mendeteksi kecurangan klaim INA-CBG secara otomatis, transparan, dan berlandaskan regulasi klinis sebelum pembayaran dilakukan, agar efisiensi dana jaminan sosial tercapai optimal.'**  
>  
> Secara garis besar, VeriKlaim bekerja melalui integrasi dua mesin: Ensemble Machine Learning (XGBoost dan Isolation Forest) yang dipadukan dengan 6 Klaster Deteksi Kecurangan Terpadu Blueprint Kemenkes RI, Permenkes No. 26/2021, dan Permenkes No. 16/2019.  
>  
> Tiga target terukur yang kami capai:  
> 1. **Otomasi Screening & Efisiensi Waktu > 85%:** Sistem menyaring otomatis 100% berkas klaim sebelum bayar dalam hitungan milidetik, sehingga dokter verifikator cukup fokus 1-2 menit menelaah berkas berisiko tinggi melalui workstation digital, dibandingkan 15-20 menit per berkas manual.  
> 2. **Sensitivitas Tinggi & Presisi 96.4%:** Sensitivitas mencapai 98.6% hingga 100% pada batasan kaidah aturan baku regulasi, dengan presisi 96.4% yang meminimalkan alarm palsu bagi rumah sakit.  
> 3. **Reduksi Dispute & Pencegahan Kebocoran DJS:** Menurunkan durasi sengketa klaim dari 14-30 hari menjadi 1-2 hari kerja tuntas berkat bukti 4 berkas digital. Terbukti memvalidasi pemotongan overclaim riil Rp 61 Juta pada 50.000 data sampel BPJS dan potensi Rp 14,34 Miliar pada skenario uji stres."*

---

### BAGIAN 3: LATAR BELAKANG DAN DAMPAK (01:30 - 03:00 | 90 Detik)
**[Tampilkan Slide 4: Latar Belakang dan Dampak]**

> **M. Ali Maulana (Lead Domain Klinis):**  
> *"Bapak dan Ibu Dewan Juri yang kami hormati,  
> Setiap tahunnya, puluhan juta klaim FKRTL diajukan ke BPJS Kesehatan. Namun kapasitas verifikasi manual sangat terbatas, sehingga hanya 10 hingga 20 persen berkas yang sempat diaudit lewat uji petik acak.  
>  
> Keterbatasan ini memicu celah overclaim dan inefisiensi Dana Jaminan Sosial (DJS). Temuan BPK RI dan kajian KPK pada Juli 2024 secara gamblang mencatat dugaan klaim fiktif dan phantom billing senilai Rp 35 Miliar di tiga rumah sakit di Sumatera Utara dan Jawa Tengah. Modus yang mendominasi meliputi: Top-Up Special CMG fiktif tanpa tindakan bedah, disparitas diagnosa masuk ringan menjadi diagnosa pulang berat (coding drift), upcoding tingkat keparahan tanpa perawatan ICU, dan klaim rawat jalan yang membypass sistem rujukan berjenjang.  
>  
> VeriKlaim menghadirkan perbaikan dampak konkret sebelum vs sesudah:  
> 1. **Kecepatan Telaah:** Dari 15-20 menit per berkas menumpuk menjadi **screening instan AI**, di mana dokter cukup meneliti berkas beranomali dalam 1-2 menit.  
> 2. **Cakupan Audit:** Dari hanya 10-20% sampel acak menjadi **100% seluruh klaim tersaring secara pre-payment** dengan sensitivitas tinggi dan presisi 96.4%.  
> 3. **Penyelesaian Dispute:** Dari 14-30 hari kalender menjadi **1-2 hari kerja selesai**, karena dokter verifikator dan pihak faskes memiliki dasar pembuktian 4 berkas digital otentik yang transparan."*

---

### BAGIAN 4: ALUR PROSES APLIKASI (03:00 - 04:30 | 90 Detik)
**[Tampilkan Slide 5: Alur Proses Aplikasi]**

> **Nurman Hariyanto (Lead Data & Infrastruktur):**  
> *"Berikut adalah arsitektur alur kerja 5 tahap VeriKlaim:  
> 1. **Tahap 1 - Input:** Data transaksi klaim diterima via API VClaim/e-Klaim atau batch upload file CSV/JSON, mencakup atribut klinis dan 4 berkas digital pendukung.  
> 2. **Tahap 2 - Proses:** Sistem melakukan validasi skema dan hashing NIK SHA-256 (kepatuhan UU PDP No. 27/2022), dilanjutkan rekayasa fitur Cost Velocity Ratio dan analisis disparitas koding.  
> 3. **Tahap 3 - Analisis AI:** Data dievaluasi serentak oleh Dual-Core Engine: Ensemble XGBoost dan Isolation Forest menghitung skor risiko, sementara 6 Klaster Kemenkes menguji kepatuhan kaidah INA-CBG secara deterministik.  
> 4. **Tahap 4 - Output:** Hasil disajikan ke dalam **Workstation Verifikasi Dokter**, lengkap dengan skor anomali, dekomposisi TreeSHAP, dan viewer 4 dokumen digital terintegrasi.  
> 5. **Tahap 5 - Tindak Lanjut:** Dokter verifikator mengesahkan putusan akhir, mencatat rekam jejak digital (audit trail), dan mengunduh Berita Acara Audit Resmi format PDF ber-QR code.  
>  
> Aktor utama pengguna solusi ini adalah Dokter Verifikator Kantor Cabang BPJS Kesehatan, Tim Pencegahan Kecurangan Rumah Sakit (Tim PK-RS), dan Auditor Manajemen Risiko."*

---

### BAGIAN 5: DEMO APLIKASI & PROTOTYPE LANGSUNG (04:30 - 07:30 | 180 Detik / 3 Menit)
**[Pindah Screen Share ke Browser aktif di http://127.0.0.1:8000/]**

> **Aditya Pratama:**  
> *"Sekarang mari kita saksikan demo langsung sistem VeriKlaim yang sedang berjalan aktif pada server lokal kami di port 8000.  
>  
> **Skenario 1: Monitoring Portofolio Klaim & 6 Klaster Kemenkes**  
> Di layar terlihat dashboard monitoring operasional dengan palet resmi Mobile JKN. Pada dataset riil BPJS 50.000 klaim, VeriKlaim secara tepat memvalidasi 64 klaim yang terpotong overclaim oleh verifikator senilai Rp 61 Juta. Sementara pada dataset skenario uji stres 10.000 klaim, sistem mendeteksi potensi overclaim multi-klaster senilai Rp 14,34 Miliar. Kita dapat memfilter klaim berdasarkan 6 klaster deteksi Kemenkes secara real-time.  
>  
> **Skenario 2: Audit Klaim Interaktif Kasus Upcoding Ekstrem**  
> Sekarang kita masuk ke evaluasi klaim individual. Kita simulasikan satu berkas klaim: Pasien persalinan sesar darurat (ICD-10 O82.1), dengan lama rawat hanya 1 hari, namun diajukan Severity III (komplikasi berat) sebesar Rp 36.500.000, padahal tarif acuan hanya Rp 6.200.000 dan pasien tidak dirawat di ICU.  
> Dalam hitungan milidetik, sistem seketika memberikan vonis: **Status Anomali: FRAUD TINGGI dengan Skor Risiko 98.2%!**  
>  
> **Skenario 3: Workstation Dokter & Cross-Check 4 Dokumen Digital (Human-in-the-Loop)**  
> Di sinilah keunggulan utama VeriKlaim: Dokter verifikator dapat menekan tombol **'Buka Workstation'**.  
> Terbuka modal terpadu yang menampilkan 4 dokumen klinis otentik:  
> 1. **Surat Eligibilitas Peserta (SEP) Digital.**  
> 2. **Resume Medis Pasien Pulang dari DPJP.**  
> 3. **Rincian Tagihan Billing Rumah Sakit.**  
> 4. **Surat Rujukan Berjenjang FKTP.**  
> Dokter dapat memvalidasi langsung kesesuaian antara diagnosa, lama rawat, dan obat yang diberikan. Modul TreeSHAP membeberkan faktor pemicu anomali secara numerik, disertai rujukan resmi Permenkes 26/2021 dan Permenkes 16/2019.  
>  
> **Skenario 4: Pengesahan Putusan Dokter & Penerbitan Dokumen PDF**  
> Dokter verifikator memilih putusan: **'Sahkan Status: FRAUD TINGGI'**, memasukkan catatan telaah klinis, dan menekan tombol simpan. Putusan ini langsung tercatat secara persisten ke dalam audit trail sistem.  
> Terakhir, verifikator dapat langsung mengunduh **Berita Acara Audit Resmi format PDF** ber-QR code serta **Buku Panduan Fitur Platform VeriKlaim** untuk lampiran klarifikasi resmi ke pihak rumah sakit."*

---

### BAGIAN 6: PENJELASAN FITUR UTAMA (07:30 - 09:00 | 90 Detik)
**[Kembali ke Slide Presentasi — Tampilkan Slide 7: Penjelasan Fitur]**

> **Nurman Hariyanto:**  
> *"Empat fitur inti yang menopang keunggulan VeriKlaim:  
> 1. **6-Cluster Fraud Detection Engine:** Menyaring 6 klaster Blueprint Kemenkes secara cepat dan deterministik dengan kapasitas throughput di atas 400 request per detik.  
> 2. **Human-in-the-Loop Workstation & 4 Dokumen:** Memberikan ruang telaah otentik bagi dokter verifikator untuk memeriksa berkas SEP, Resume DPJP, Billing, dan Rujukan secara transparan."*  
>  
> **M. Ali Maulana:**  
> *"3. **TreeSHAP Explainability & LLM Collaborator:** Membongkar kotak hitam AI dengan atribusi fitur matematis dan narasi klinis cerdas berlandaskan pasal regulasi baku.  
> 4. **Automated Dossier & Buku Panduan Platform:** Mengotomasi penerbitan dokumen Berita Acara Audit PDF formal dan Buku Panduan Fitur, memangkas masa sengketa klaim pending menjadi 1-2 hari kerja tuntas."*

---

### BAGIAN 7: ARSITEKTUR, KEAMANAN PDP, DAN PENUTUP (09:00 - 10:00 | 60 Detik)
**[Tampilkan Slide 8, 9, 10, dan akhiri di Slide 11 Penutup]**

> **Aditya Pratama:**  
> *"Dari sisi kesiapan implementasi, VeriKlaim berada pada **Technology Readiness Level 6 (TRL 6)**. Prototipe telah diuji pada 50.000 data sampel klaim FKRTL BPJS Kesehatan dan 10.000 data skenario uji dengan performa: **Sensitivitas 98.6% - 100%, Presisi 96.4%, ROC-AUC 0.998 - 1.000, dan latensi end-to-end API hanya 2.4 ms**.  
>  
> Dari aspek kepatuhan regulasi, VeriKlaim patuh penuh pada **UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)** dengan prinsip Zero PII Storage dan pseudonymization hashing satu arah. Seluruh sistem dirancang *On-Premise Ready* di server internal BPJS Kesehatan tanpa mengirim data ke pihak ketiga asing.  
>  
> Prinsip **Human-in-the-Loop** kami pegang teguh: AI murni bertindak sebagai Decision Support System cerdas, sementara wewenang final persetujuan klaim tetap 100% berada di tangan Dokter Verifikator Resmi BPJS Kesehatan.  
>  
> Repositori kode dan dokumentasi lengkap dapat diakses publik di GitHub: `https://github.com/orochimadit/veri-klaim`.  
>  
> Bersama VeriKlaim: **Detect Smarter, Protect JKN — Smarter Protection for a Stronger JKN.**  
> Terima kasih atas perhatian Dewan Juri, Wassalamu’alaikum Warahmatullahi Wabarakatuh."*

---

## 4. TIPS SUKSES SAAT REKAMAN ZOOM
- **Transisi Screen Share:** Saat menit ke 04:30, Ketua Tim (Aditya) beralih dari tab slide ke tab browser dashboard live (`http://127.0.0.1:8000`). Tunjukkan tombol buka workstation dokter dan viewer 4 dokumen digital.
- **Pengaturan Audio:** Gunakan headset/mikrofon eksternal agar suara tidak bergema.
- **Ketepatan Waktu:** Pasang timer/stopwatch di samping layar laptop untuk memantau transisi bagian agar tidak melebihi batas 10 menit.
