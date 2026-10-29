# NASKAH PANDUAN REKAMAN VIDEO PRESENTASI (DURASI MAKSIMAL 10 MENIT)
**Healthkathon 2026 BPJS Kesehatan — Project Final**  
*Tema: Detect Smarter, Protect JKN — Smarter Protection for a Stronger JKN (Efisiensi Risiko Program JKN)*  
*Kategori: Efisiensi Risiko pada Faskes / KLAIM (Kode: C03.04)*  
*Nama Solusi: VeriKlaim*  
*Nama Tim: Tim VeriKlaim Kalbar*  

---

## 1. PANDUAN UMUM & CHECKLIST SEBELUM MEREKAM (ZOOM MEETING)
1. **Durasi Total:** Maksimal 10 menit (Target ideal rekaman: 9 menit 30 detik s.d. 9 menit 50 detik).
2. **Platform Perekaman:** Zoom Meeting (Rekomendasi resmi panitia).
   - Pastikan kamera/webcam ketiga anggota tim menyala (foto/video wajah tampil jelas).
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
| **04:30 - 07:30** | 180 detik | Slide 6 & Web | **DEMO LANGSUNG APLIKASI (Live System http://127.0.0.1:8000)** | **Aditya Pratama** |
| **07:30 - 09:00** | 90 detik | Slide 7 | Penjelasan 4 Fitur Utama Solusi | **Nurman Hariyanto** & **M. Ali Maulana** |
| **09:00 - 10:00** | 60 detik | Slide 8 - 11 | Arsitektur, Keamanan PDP, Validasi 50k & Penutup | **Aditya Pratama** |

---

## 3. NASKAH LENGKAP KATA PER KATA (SCRIPT)

### BAGIAN 1: COVER & PERKENALAN TIM (00:00 - 00:30 | 30 Detik)
**[Tampilkan Slide 1 Cover, lalu Slide 2 Perkenalan Tim]**

> **Aditya Pratama (Ketua Tim):**  
> *"Assalamu’alaikum Warahmatullahi Wabarakatuh, salam sejahtera, dan salam sehat untuk Dewan Juri Healthkathon BPJS Kesehatan 2026.  
> Kami dari **Tim VeriKlaim Kalbar** dengan bangga mempersembahkan solusi kami pada Kategori Efisiensi Risiko pada Faskes/KLAIM: **VeriKlaim — Platform Deteksi Anomali Klaim FKRTL Berbasis Hybrid Machine Learning dan Explainable AI.**  
> Tim kami merupakan kolaborasi lintas disiplin antara AI, Big Data, dan Manajemen Layanan Klinis:  
> 1. Saya sendiri, **Aditya Pratama, S.T., M.T.**, Dosen Program Studi Sistem Informasi Universitas Nahdlatul Ulama Kalimantan Barat, alumni STEI ITB, bertindak sebagai Ketua Tim dan Lead AI & Arsitektur Sistem.  
> 2. Rekan saya, **Nurman Hariyanto, S.ST., M.T.**, Dosen Sistem Informasi UNU Kalbar, alumni S2 STEI ITB dan Polban, sebagai Lead Rekayasa Data & Infrastruktur.  
> 3. Dan **M. Ali Maulana, M.Kep.**, Dosen Keperawatan Fakultas Kedokteran Universitas Tanjungpura, sebagai Lead Domain Klinis dan Kepatuhan Regulasi Kesehatan."*

---

### BAGIAN 2: JUDUL IDE, DESKRIPSI, DAN TUJUAN (00:30 - 01:30 | 60 Detik)
**[Tampilkan Slide 3: Judul Ide, Deskripsi, dan Tujuan]**

> **Aditya Pratama:**  
> *"Nilai utama dari VeriKlaim dirangkum dalam satu kalimat:  
> **'Solusi ini membantu Verifikator BPJS Kesehatan dan Tim Pencegahan Fraud Rumah Sakit mendeteksi kecurangan klaim INA-CBG secara otomatis, transparan, dan berlandaskan regulasi klinis sebelum pembayaran dilakukan, agar efisiensi dana jaminan sosial tercapai optimal.'**  
>  
> Secara garis besar, VeriKlaim bekerja melalui integrasi dua mesin: Ensemble Machine Learning (LightGBM dan XGBoost) untuk mendeteksi anomali statistik tersembunyi, yang dipadukan dengan Deterministic Rule Engine berlandaskan Permenkes No. 26/2021 dan Permenkes No. 16/2019.  
>  
> Tiga tujuan terukur yang kami capai:  
> 1. **Efisiensi Waktu Audit:** Memangkas waktu telaah klaim berisiko dari 15-20 menit manual menjadi **kurang dari 3 detik** per berkas.  
> 2. **Presisi Tinggi:** Mencapai **ROC-AUC 1.0000 dan F1-Score 0.99** dengan false positive di bawah 0.6% pada dataset teruji 50.000 klaim.  
> 3. **Reduksi Dispute 70%:** Menurunkan durasi sengketa klaim dari 14-30 hari menjadi 1-2 hari melalui Berita Acara Audit transparan berbasis Explainable AI."*

---

### BAGIAN 3: LATAR BELAKANG DAN DAMPAK (01:30 - 03:00 | 90 Detik)
**[Tampilkan Slide 4: Latar Belakang dan Dampak]**

> **M. Ali Maulana (Lead Domain Klinis):**  
> *"Bapak dan Ibu Dewan Juri yang kami hormati,  
> Setiap tahunnya, puluhan juta klaim FKRTL diajukan ke BPJS Kesehatan. Namun kapasitas telaah verifikator manusia secara manual sangat terbatas, sehingga hanya 10 hingga 20 persen berkas yang sempat diaudit lewat uji petik.  
>  
> Keterbatasan ini memicu celah kebocoran Dana Jaminan Sosial (DJS). Temuan BPK RI dan kajian KPK pada Juli 2024 secara gamblang mencatat adanya dugaan klaim fiktif dan phantom billing senilai Rp 35 Miliar di tiga rumah sakit di Sumatera Utara dan Jawa Tengah. Modus yang mendominasi meliputi: Upcoding tingkat keparahan pada tindakan bedah sesar, tagihan ganda ventilator ICU, dan penambahan komorbiditas palsu.  
>  
> Bila klaim bermasalah ini disengketakan, proses klarifikasi memakan waktu 14 hingga 30 hari, menahan arus kas rumah sakit dan membebani administrasi BPJS.  
>  
> VeriKlaim menghadirkan lompatan dampak konkret sebelum vs sesudah:  
> 1. **Kecepatan Telaah:** Dari 15-20 menit per berkas manual menjadi **kurang dari 3 detik** otomatis real-time.  
> 2. **Cakupan Audit:** Dari hanya 10-20% sampel acak menjadi **100% seluruh klaim tersaring secara pre-payment**.  
> 3. **Resolusi Dispute:** Dari 14-30 hari kalender menjadi **1-2 hari kerja selesai**, karena sistem langsung menerbitkan bukti klinis dan dasar hukum yang tidak dapat disanggah sepihak."*

---

### BAGIAN 4: ALUR PROSES APLIKASI (03:00 - 04:30 | 90 Detik)
**[Tampilkan Slide 5: Alur Proses Aplikasi]**

> **Nurman Hariyanto (Lead Data & Infrastruktur):**  
> *"Berikut adalah arsitektur alur kerja 5 tahap VeriKlaim:  
> 1. **Tahap 1 - Input:** Data transaksi klaim diterima secara real-time via API bridging e-Klaim/VClaim BPJS atau batch upload file CSV/JSON dengan parameter lengkap: Length of Stay (LOS), kode diagnosa ICD-10, prosedur ICD-9-CM, tingkat keparahan, serta tarif RS dan tarif acuan INA-CBG.  
> 2. **Tahap 2 - Proses:** Sistem melakukan sanitasi skema dan penyamaran identitas NIK pasien (Zero PII sesuai UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi), dilanjutkan rekayasa fitur rasio tarif terhadap LOS dan matriks inkonsistensi klinis.  
> 3. **Tahap 3 - Analisis AI:** Data dievaluasi serentak oleh Dual-Core Engine: Ensemble Tree Model menghitung probabilitas anomali statistik, sementara Clinical Rule Matrix menguji pelanggaran batas Permenkes 26/2021 dan 16/2019.  
> 4. **Tahap 4 - Output:** Dashboard menampilkan status klaim: Wajar, Waspada, atau Fraud Tinggi, lengkap dengan visualisasi atribusi faktor TreeSHAP dan rekomendasi tindakan.  
> 5. **Tahap 5 - Tindak Lanjut:** Verifikator dapat menyetujui klaim layak atau langsung mencetak Berita Acara Audit Resmi format PDF ber-QR code dan dasar hukum untuk proses klarifikasi ke faskes.  
>  
> Aktor utama pengguna solusi ini adalah Verifikator Kantor Cabang BPJS Kesehatan, Tim Pencegahan Kecurangan Rumah Sakit (Tim PK-RS), dan Auditor Manajemen Risiko."*

---

### BAGIAN 5: DEMO APLIKASI & PROTOTYPE LANGSUNG (04:30 - 07:30 | 180 Detik / 3 Menit)
**[Pindah Screen Share ke Browser aktif di http://127.0.0.1:8000/]**

> **Aditya Pratama:**  
> *"Sekarang mari kita saksikan demo langsung sistem VeriKlaim yang sedang berjalan secara aktif pada server lokal kami di port 8000.  
>  
> **Skenario 1: Monitoring Portofolio 50.000 Klaim (Makro Dashboard)**  
> Di layar terlihat dashboard monitoring operasional. Sistem telah memproses 50.000 data sampel klaim FKRTL BPJS Kesehatan. Dari 50.000 klaim ini, VeriKlaim secara presisi mengidentifikasi 137 klaim berindikasi anomali fraud (rasio 0.27%), dengan total potensi efisiensi dana yang berhasil diselamatkan mencapai Rp 1,84 Miliar. Kita juga dapat melihat sebaran rasio anomali per departemen faskes secara real-time.  
>  
> **Skenario 2: Audit Klaim Interaktif Kasus Upcoding (Single Claim Evaluation)**  
> Sekarang kita masuk ke modul audit klaim individual. Kita simulasikan satu berkas klaim: Pasien tindakan persalinan sesar darurat (ICD-10 O82.1), dengan Length of Stay hanya 1 hari, namun rumah sakit menagihkan tarif Severity Level III (komplikasi berat) sebesar Rp 36.500.000, padahal tarif acuan INA-CBG standar hanya Rp 6.200.000.  
> Begitu kita klik tombol **'Evaluasi Klaim'**, perhatikan! Dalam waktu kurang dari 40 milidetik, sistem seketika memberikan vonis: **Status Anomali: FRAUD TINGGI dengan Skor Risiko 96.8%!**  
>  
> **Skenario 3: Transparansi Explainable AI (XAI) & Bukti Regulasi**  
> Mengapa sistem menandai klaim ini sebagai fraud? VeriKlaim bukan kotak hitam!  
> Di bagian bawah, modul TreeSHAP membedah faktor penyebabnya:  
> 1. Rasio tarif yang melonjak 5.88 kali lipat di atas acuan memberikan kontribusi SHAP positif sebesar +0.42.  
> 2. Diskrepansi LOS 1 hari pada tindakan Severity III memberikan kontribusi +0.31.  
> 3. Modul kepatuhan hukum langsung menampilkan pelanggaran: **Permenkes No. 26 Tahun 2021 Pasal 14 ayat (2) mengenai ketidaksesuaian tingkat keparahan dengan bukti lama rawat klinis.**  
>  
> **Skenario 4: Penerbitan Berita Acara Audit Resmi (PDF)**  
> Terakhir, verifikator cukup menekan tombol **'Unduh Berita Acara Audit Resmi'**.  
> Dalam 1 detik, dokumen PDF formal langsung terbit! Dokumen ini memuat nomor register audit, rincian klinis, dasar pasal hukum yang dilanggar, kalkulasi selisih tarif yang harus dikonfirmasi, serta QR Code validasi keaslian dokumen yang siap ditandatangani dan dikirimkan ke pihak rumah sakit sebagai bahan klarifikasi resmi."*

---

### BAGIAN 6: PENJELASAN FITUR UTAMA (07:30 - 09:00 | 90 Detik)
**[Kembali ke Slide Presentasi — Tampilkan Slide 7: Penjelasan Fitur]**

> **Nurman Hariyanto:**  
> *"Empat fitur inti yang menopang keunggulan VeriKlaim:  
> 1. **AI Anomaly Scoring Engine:** Menghitung probabilitas kecurangan multi-variabel dalam hitungan milidetik, menyaring jutaan transaksi sebelum pembayaran.  
> 2. **Regulatory Rule-Based Validator:** Memvalidasi ambang batas kaidah koding Permenkes 26/2021 dan Permenkes 16/2019, memberikan legitimasi hukum definitif pada setiap temuan."*  
>  
> **M. Ali Maulana:**  
> *"3. **Explainable AI (XAI) & Dynamic Reasoner:** Menghilangkan fenomena 'black-box' dengan menerjemahkan kontribusi fitur SHAP ke dalam bahasa klinis yang mudah dipahami dokter penanggung jawab pasien maupun verifikator.  
> 4. **Automated Audit Dossier Generator:** Mengotomasi pembuatan dokumen berita acara audit legal format PDF, memangkas proses sengketa administratif dari 30 hari menjadi instan."*

---

### BAGIAN 7: ARSITEKTUR, KEAMANAN PDP, DAN PENUTUP (09:00 - 10:00 | 60 Detik)
**[Tampilkan Slide 8, 9, 10, dan akhiri di Slide 11 Penutup]**

> **Aditya Pratama:**  
> *"Dari sisi kesiapan implementasi, VeriKlaim berada pada **Technology Readiness Level 6 (TRL 6)**. Prototipe telah diuji penuh menggunakan 50.000 data klaim FKRTL BPJS Kesehatan dengan hasil evaluasi: **ROC-AUC 1.0000, Presisi 99.4%, dan Recall 98.6%**.  
>  
> Dari aspek keamanan, VeriKlaim patuh penuh pada **UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)** dengan prinsip Zero PII Storage dan pseudonymization hashing satu arah. Seluruh sistem dirancang *On-Premise Ready* di data center BPJS Kesehatan tanpa mengirim data ke pihak ketiga.  
>  
> Kami juga menjunjung etika **Human-in-the-Loop**, di mana AI murni bertindak sebagai Decision Support System pembantu analisis, sementara kewenangan final persetujuan klaim tetap 100% berada di tangan Verifikator Resmi BPJS Kesehatan.  
>  
> Repositori kode lengkap dapat diakses publik di GitHub: `https://github.com/orochimadit/veri-klaim`.  
>  
> Bersama VeriKlaim: **Detect Smarter, Protect JKN — Smarter Protection for a Stronger JKN.**  
> Terima kasih atas perhatian Dewan Juri, Wassalamu’alaikum Warahmatullahi Wabarakatuh."*

---

## 4. TIPS SUKSES SAAT REKAMAN ZOOM
- **Transisi Screen Share:** Saat menit ke 04:30, Ketua Tim (Aditya) beralih dari tab slide ke tab browser dashboard live (`http://127.0.0.1:8000`). Lakukan tes sebelum merekam.
- **Pengaturan Audio:** Gunakan headset/mikrofon eksternal agar suara tidak bergema.
- **Ketepatan Waktu:** Pasang timer/stopwatch di samping layar laptop untuk memantau transisi bagian agar tidak melebihi batas 10 menit.
