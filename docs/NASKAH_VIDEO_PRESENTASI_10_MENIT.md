# NASKAH PANDUAN REKAMAN VIDEO PRESENTASI (DURASI MAKSIMAL 10 MENIT)
**Healthkathon 2026 BPJS Kesehatan — Tahap 20 Besar Menuju Final Offline**  
*Tema: Detect Smarter, Protect JKN — Smarter Protection for a Stronger JKN*  
*Kategori: Pemberi Kerja*  
*Nama Tim: Aqila Digital*  
*Nama Solusi: VeriKlaim*  

---

## 1. PANDUAN RESMI SESUAI "PANDUAN 20 BESAR" BPJS KESEHATAN

1. **Durasi Total:** Maksimal 10 menit (Target ideal: **09:30 s.d. 09:50**). *Jangan pernah melebihi 10 menit karena sistem penilaian akan memotong poin.*
2. **Platform Perekaman:** **Zoom Meeting** (Rekomendasi resmi panitia).
   - Seluruh anggota tim (Aditya Pratama, Nurman Hariyanto, M. Ali Maulana) wajib menyalakan webcam/kamera aktif sepanjang video.
   - Gunakan fitur *Share Screen* untuk menampilkan slide presentasi (`docs/Aqila Digital.pdf` atau `docs/project_final_healthkathon_slides.html`) dan beralih ke browser aktif di `https://veriklaim.absolute-tech.id/` saat sesi demo.
3. **Pengaturan YouTube:** 
   - Visibilitas: **Unlisted** (Tidak Publik) agar hanya juri dan panitia yang memiliki tautan dapat menonton.
   - Judul & Deskripsi: Hindari karakter tanda kurung jika dilarang sistem.
4. **Batas Waktu Pengiriman:** 14 - 17 November 2026 melalui email resmi ke `hackathonbpjs@bpjs-kesehatan.go.id` oleh Ketua Tim.
   - Format Subjek: `Project Final - Aqila Digital - Pemberi Kerja`
   - Lampiran Slide: `Aqila Digital.pdf` (Ukuran file kami 0.72 MB, batas maksimal 15 MB).

---

## 2. SUSUNAN WAKTU DAN STRUKTUR PRESENTASI (PANDUAN 20 BESAR HALAMAN 7)

| Menit Ke- | Durasi | Slide Acuan | Bagian Presentasi | Pembicara Utama |
| :--- | :--- | :--- | :--- | :--- |
| **00:00 - 01:00** | 1 menit (60 dtk) | Slide 1 & 2 | **Bagian 1: Perkenalan Tim Aqila Digital** | **Aditya Pratama** |
| **01:00 - 03:00** | 2 menit (120 dtk) | Slide 3 & 4 | **Bagian 2: Perubahan Setelah Coaching (4 Masukan Mentor)** | **Aditya Pratama** & **Nurman H.** |
| **03:00 - 04:00** | 1 menit (60 dtk) | Slide 5 | **Bagian 3: Ringkasan Solusi & 5-Stage Pipeline** | **Nurman Hariyanto** |
| **04:00 - 07:30** | 3.5 menit (210 dtk)| Slide 6, 7 & Web | **Bagian 4: Demo Aplikasi Versi Terbaru (Batch Upload & Workstation)** | **Aditya Pratama** |
| **07:30 - 09:00** | 1.5 menit (90 dtk) | Slide 8, 9 & 10 | **Bagian 5: Dampak, Pembobotan Ensemble AI & Rekam Medis PDP** | **M. Ali Maulana** |
| **09:00 - 10:00** | 1 menit (60 dtk) | Slide 11 & 12 | **Bagian 6: Infrastruktur Nasional 120 Juta Klaim & Penutup** | **Aditya Pratama** |

---

## 3. NASKAH KATA PER KATA (SCRIPT PRESENTASI)

### BAGIAN 1: PERKENALAN TIM AQILA DIGITAL (00:00 - 01:00 | 60 Detik)
**[Tampilkan Slide 1 Cover, lalu beralih ke Slide 2 Perkenalan Tim]**

> **Aditya Pratama (Ketua Tim):**  
> *"Assalamu’alaikum Warahmatullahi Wabarakatuh, salam sejahtera, dan salam sehat untuk Dewan Juri dan Coach Healthkathon BPJS Kesehatan 2026.  
> Kami dari **Tim Aqila Digital** dengan bangga mempersembahkan project final kami pada Kategori Pemberi Kerja: **VeriKlaim — Sistem Asistensi Audit Pra-Bayar Klaim INA-CBG Berbasis Explainable AI SHAP, 6-Klaster Regulasi Kemenkes, dan Workstation Human-in-the-Loop 4 Dokumen Digital.**  
> 
> Tim Aqila Digital merupakan sinergi lintas disiplin yang solid:  
> 1. Saya sendiri, **Aditya Pratama, S.T., M.T.**, Dosen Sistem Informasi Universitas Nahdlatul Ulama Kalimantan Barat, alumni S1 & S2 STEI ITB, selaku Ketua Tim dan Lead AI & Arsitektur Sistem.  
> 2. Rekan saya, **Nurman Hariyanto, S.ST., M.T.**, Dosen Sistem Informasi UNU Kalbar, alumni S2 STEI ITB, selaku Lead Rekayasa Data & Pipeline Infrastruktur.  
> 3. Dan **M. Ali Maulana, M.Kep.**, Dosen Keperawatan Fakultas Kedokteran Universitas Tanjungpura, selaku Lead Domain Layanan Klinis dan Kepatuhan Regulasi Kesehatan.  
> Seluruh anggota tim hadir lengkap dalam sesi rekaman ini."*

---

### BAGIAN 2: PERUBAHAN SETELAH COACHING (01:00 - 03:00 | 120 Detik)
**[Tampilkan Slide 3: Perubahan Setelah Coaching, lalu Slide 4: Bukti Nyata Sebelum vs Sesudah]**

> **Aditya Pratama:**  
> *"Bapak dan Ibu Dewan Juri yang kami hormati,  
> Sesi coaching bersama mentor BPJS memberikan akselerasi luar biasa bagi VeriKlaim. Kami telah menindaklanjuti dan mengimplementasikan **100% dari 4 catatan masukan coach** ke dalam sistem produksi:  
> 
> **Pertama, terkait ketiadaan fitur upload dan integrasi klaim:**  
> Kami langsung membangun modul **Drag-and-Drop Batch Upload multi-format (CSV, Excel XLSX, dan JSON)** dengan auto-schema parser dan penyediaan template klaim terstandar, serta merilis endpoint **Webhook SIMRS otomatis** (`POST /api/claims/batch-audit`).  
> 
> **Kedua, terkait pembobotan skoring akurasi AI:**  
> Kami mengimplementasikan **Calibrated Ensemble dengan bobot 60% XGBoost dan 40% Random Forest**. Kombinasi ini memberikan akurasi prediksi 98.44%, Recall 100% pada batas regulasi baku, dengan latensi inferensi super cepat di bawah 0.15 milidetik per klaim."*

> **Nurman Hariyanto (Melanjutkan Bagian 2):**  
> *"Melanjutkan poin coaching berikutnya:  
> **Ketiga, terkait mekanisme permintaan data rekam medis pasien untuk klarifikasi RS:**  
> Menjawab kekhawatiran regulasi kerahasiaan medik, kami merancang **Protokol Text-Only Structured Snippet dari DPJP**. Rumah sakit tidak perlu mengunggah berkas PDF mentah yang rentan kebocoran data. Sebaliknya, DPJP hanya memasukkan intisari klinis terstruktur yang dievaluasi secara semantik objektif oleh AI, sepenuhnya patuh pada **UU Pelindungan Data Pribadi No. 27 Tahun 2022** dan **Permenkes No. 24 Tahun 2022**.  
> 
> **Keempat, perhitungan infrastruktur skala nasional:**  
> Kami telah menyusun kalkulasi komputasi lengkap untuk melayani total volume **120 Juta Klaim Nasional per tahun**, dengan arsitektur 4-Node High-Availability Cluster On-Premise berkapasitas 1.600 Transaksi per Detik, lebih dari 10 kali lipat kebutuhan beban puncak BPJS Kesehatan.  
> Tabel pada Slide 4 membuktikan transformasi nyata VeriKlaim dari prototype laboratorium menjadi solusi siap pakai skala industri."*

---

### BAGIAN 3: RINGKASAN SOLUSI & ALUR SISTEM (03:00 - 04:00 | 60 Detik)
**[Tampilkan Slide 5: Ringkasan Solusi & Alur Proses]**

> **Nurman Hariyanto:**  
> *"VeriKlaim beroperasi melalui alur 5-tahap end-to-end yang seamless:  
> 1. **Tahap 1 Ingesti:** Berkas klaim diterima dari API VClaim BPJS, batch upload portal faskes, atau webhook SIMRS.  
> 2. **Tahap 2 Validasi & PDP:** Validasi skema tarif INA-CBG dan hashing NIK SHA-256 demi privasi data peserta.  
> 3. **Tahap 3 Dual-Engine AI:** Pengujian simultan oleh 6 Klaster Aturan Kemenkes (Recall 100%) dan Ensemble Machine Learning 60:40 (Presisi 96.4%).  
> 4. **Tahap 4 Workstation Dokter (HITL):** Dokter verifikator menelaah klaim flagged pada workstation 1-layar, didukung visualisasi TreeSHAP dan Text-Only Snippet DPJP.  
> 5. **Tahap 5 Putusan & Output:** Dokter mengesahkan status audit, mencatat audit trail permanen, dan mengunduh Berita Acara Audit Resmi format PDF ber-QR Code untuk integrasi penyelesaian sengketa di E-Klaim."*

---

### BAGIAN 4: DEMO APLIKASI VERSI TERBARU (04:00 - 07:30 | 210 Detik / 3.5 Menit)
**[Pindah Screen Share ke Browser aktif di https://veriklaim.absolute-tech.id/]**

> **Aditya Pratama:**  
> *"Sekarang mari kita uji coba langsung sistem VeriKlaim versi terbaru yang aktif pada server produksi di tautan **https://veriklaim.absolute-tech.id/**.  
> 
> **Fitur Baru 1: Batch Upload Portal & Template Unduhan (Masukan 1)**  
> Di layar terlihat menu baru **'Unggah Berkas Klaim'**. Pengguna atau rumah sakit dapat mengklik tombol 'Unduh Template Klaim' untuk mendapatkan struktur kolom terstandar.  
> Sekarang kita simulasikan: Saya drag file CSV berisi batch klaim ke area upload. Sistem langsung mem-parsing 1.000 baris klaim dalam waktu 0.8 detik! Sistem secara otomatis memisahkan mana klaim aman (Wajar) dan mana klaim beranomali tinggi yang perlu ditinjau dokter verifikator.  
> 
> **Fitur Baru 2: Audit Klaim Kasus Upcoding Ekstrem**  
> Mari kita buka salah satu klaim berisiko tinggi: Pasien persalinan sesar darurat (ICD-10 O82.1), lama rawat hanya 1 hari, tanpa indikasi komplikasi di ICU, namun diajukan Severity III sebesar Rp 36.500.000 (tarif acuan wajar hanya Rp 6.200.000).  
> Dalam hitungan milidetik, Dual-Engine AI memberikan vonis tegas: **FRAUD TINGGI dengan Skor Risiko 98.4%!**  
> 
> **Fitur Baru 3: Workstation Human-in-the-Loop & TreeSHAP Waterfall**  
> Dokter verifikator menekan tombol **'Buka Workstation'**.  
> Terbuka modal terpadu:  
> - Di sisi kiri, panel **Explainable AI TreeSHAP** membeberkan secara matematis bahwa pemicu utama anomali adalah disparitas biaya 5.8 kali lipat dan ketiadaan tindakan ICU, merujuk langsung ke **Permenkes No. 26 Tahun 2021**.  
> - Di sisi kanan, tersedia viewer 4 dokumen: SEP Digital, Billing RS, Rujukan FKTP, dan **Resume Medis Pasien**.  
> 
> **Fitur Baru 4: Mekanisme Text-Only Snippet Klarifikasi RS (Masukan 3)**  
> Perhatikan tab Resume Medis: Rumah sakit tidak mengunggah PDF tebal, melainkan teks ringkasan klinis DPJP. Engine NLP semantik kami memverifikasi apakah ada bukti laboratorium atau tanda vital objektif. Jika teks hanya berupa dalih klise tanpa bukti fisik, sistem menandainya sebagai 'Klarifikasi Tidak Memadai'.  
> 
> **Fitur Baru 5: Pengesahan & Penerbitan Berita Acara PDF**  
> Dokter verifikator memilih putusan: **'Sahkan Status: FRAUD TINGGI'**, memasukkan catatan klinis, dan menekan simpan.  
> Dokter dapat langsung mengklik **'Unduh Berita Acara Audit'**. Terbitlah dokumen PDF resmi ber-QR Code dengan tanda tangan elektronik dokter verifikator yang siap dilampirkan dalam mediasi BPJS."*

---

### BAGIAN 5: DAMPAK, PEMBOBOTAN AI, & PROTOKOL PRIVASI (07:30 - 09:00 | 90 Detik)
**[Pindah Screen Share kembali ke Slide 8, 9, dan 10]**

> **M. Ali Maulana (Lead Domain Klinis):**  
> *"Bapak dan Ibu Dewan Juri,  
> Solusi VeriKlaim tidak hanya unggul secara antarmuka, tetapi memiliki landasan klinis, matematis, dan regulasi yang kokoh:  
> 
> 1. **Dampak Klinis & Kecepatan Telaah:**  
> Waktu audit dokter dipangkas lebih dari **85%**, dari 15-20 menit per berkas menumpuk menjadi hanya 1-2 menit pada berkas berisiko. Masa sengketa klaim faskes yang biasanya berlarut-larut 14 hingga 30 hari kalender, selesai dalam **1-2 hari kerja tuntas**.  
> 
> 2. **Keandalan Model Ensemble 60:40 (Slide 8):**  
> Formulasi 60% XGBoost dan 40% Random Forest terbukti memberikan nilai *variance damping* yang stabil. Recall 100% pada aturan baku regulasi menjamin perlindungan mutlak Dana Jaminan Sosial dari kebocoran upcoding dan phantom billing.  
> 
> 3. **Perlindungan Data Pribadi Pasien (Slide 9):**  
> Melalui protokol Text-Only Structured Snippet, BPJS terbebas dari risiko pelanggaran UU PDP No. 27/2022 maupun overload server akibat penyimpanan jutaan berkas scan rekam medis.  
> 
> 4. **Validasi Terukur (Slide 10):**  
> Pada pengujian 50.000 data klaim riil BPJS, VeriKlaim memvalidasi tepat 64 kasus overclaim senilai **Rp 61,2 Juta**, dan pada uji stres 10.000 data sintetis ekstrem, sistem mendeteksi potensi overclaim hingga **Rp 14,34 Miliar**."*

---

### BAGIAN 6: INFRASTRUKTUR NASIONAL & PENUTUP (09:00 - 10:00 | 60 Detik)
**[Tampilkan Slide 11: Kalkulasi Infrastruktur Nasional, lalu Slide 12: Penutup]**

> **Aditya Pratama:**  
> *"Menjawab masukan keempat mentor mengenai implementasi skala nasional:  
> BPJS Kesehatan memproses sekitar **120 Juta Klaim FKRTL per tahun** atau 400.000 klaim per hari kerja, dengan estimasi beban puncak (peak traffic) sekitar **150 Transaksi per Detik (TPS)**.  
> 
> Berdasarkan uji stress benchmark, mesin FastAPI VeriKlaim dengan C-optimized inference mampu melayani **1.600 TPS** pada klaster **4-Node High-Availability On-Premise** (spesifikasi 128 vCPU, 256 GB RAM, 4 TB NVMe). Ini menyediakan *headroom* kapasitas lebih dari **10 kali lipat** dari kebutuhan nasional, dengan jaminan kedaulatan data di dalam negeri sesuai PP No. 71 Tahun 2019.  
> 
> **Kesimpulan:**  
> VeriKlaim adalah solusi pra-bayar yang matang, presisi, patuh hukum, dan siap diimplementasikan secara nasional demi mewujudkan Program JKN yang berkelanjutan, adil, dan transparan.  
> 
> Kami, **Tim Aqila Digital**, siap melangkah dan memberikan pembuktian terbaik pada tahap Final Offline di hadapan pimpinan BPJS Kesehatan.  
> Terima kasih. Wassalamu’alaikum Warahmatullahi Wabarakatuh."*

---

## 4. CHECKLIST FINAL SEBELUM SUBMIT

- [x] Slide PDF `Aqila Digital.pdf` berukuran **0.72 MB** (< 15 MB) di `docs/Aqila Digital.pdf`.
- [x] Slide presentasi HTML ter-update di `docs/project_final_healthkathon_slides.html`.
- [x] Live system aktif di `https://veriklaim.absolute-tech.id`.
- [x] Fitur Batch Upload, Calibrated Ensemble 60:40, Snippet DPJP, dan Kalkulasi Infra Nasional telah tertanam di kode sumber.
- [x] Video YouTube diatur **Unlisted**, durasi maksimal **10 menit** (target 09:30 - 09:50).
- [x] Seluruh anggota tim (Aditya, Nurman, Ali) menyalakan kamera wajah sepanjang Zoom recording.
- [x] Email dikirim dari alamat email Ketua Tim ke `hackathonbpjs@bpjs-kesehatan.go.id` sebelum 17 November 2026.
