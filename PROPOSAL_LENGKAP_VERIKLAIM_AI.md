# PROPOSAL RESMI BPJS KESEHATAN HEALTHKATHON 2026
**Tema:** Detect Smarter, Protect JKN: Smarter Protection for a Stronger JKN (Efisiensi Risiko Program JKN)  
**Kategori:** Kategori 2: Efisiensi Risiko pada Fasilitas Kesehatan (Faskes)  
**Sub-Kategori Fokus:** Upcoding, Services Unbundling / Fragmentation, Phantom Billing  
**Format:** Slide Deck Presentation (16 Slide, Memenuhi 9 Komponen Wajib dan 6 Kriteria Penilaian)

---

## SUSUNAN ANGGOTA TIM INOVASI
1. **Aditya Pratama, S.ST., M.T. (Ketua Tim)**  
   *Peran:* Team Lead & AI/Machine Learning Specialist (WhatsApp: 0856-5441-1081)  
   *Kredensial & Afiliasi:* Lulusan S1 dan S2 Sekolah Teknik Elektro dan Informatika (STEI), Institut Teknologi Bandung (ITB). Penulis buku *Eksplorasi Machine Learning dengan Scikit-Learn* (2024), ketua/peneliti program riset AI Kemendiktisaintek & LPDP, periset machine learning prediksi penyakit diabetes, serta penanggung jawab arsitektur model NLP klinis dan deteksi anomali graf.
2. **Nurman Hariyanto, S.ST., M.T. (Anggota Tim)**  
   *Peran:* Backend, Cloud, & System Integration Engineer (S2 STEI ITB, S1 POLBAN, Udacity Cloud Developer)  
   *Tanggung Jawab:* Peneliti sistem cerdas dan mantan Project Manager PPTIK ITB & PT LSKK, rekayasa pipeline data berlatensi rendah (< 2 detik/klaim), integrasi REST API V-Claim BPJS, arsitektur cloud microservices, serta enkripsi dan privasi data (UU PDP).
3. **M. Ali Maulana (Anggota Tim)**  
   *Peran:* Hospital Workflow & Clinical Domain Specialist (Dosen Manajemen Keperawatan, Universitas Tanjungpura)  
   *Tanggung Jawab:* Peneliti manajemen keperawatan dan alur pelayanan rumah sakit, periset aplikasi *Early Warning System* di RS Universitas Tanjungpura, penanggung jawab validasi logika kepatuhan medis pada koding INA-CBGs & Permenkes No. 16/2019, serta perancangan antarmuka verifikator BPJS.

---

# STRUKTUR KONTEN SLIDE-BY-SLIDE (SLIDE 1 s.d. 16)

---

### [SLIDE 1] COVER TITLE & IDENTITAS TIM
* **Judul Solusi:** **VeriKlaim**
* **Sub-Judul:** Sistem Asistensi Audit Pra-Bayar Berbasis Analisis Semantik Klinis dan Deteksi Anomali Graf untuk Mitigasi Upcoding, Unbundling, dan Phantom Billing pada Klaim Rumah Sakit JKN
* **Kategori Kompetisi:** Kategori 2: Efisiensi Risiko pada Fasilitas Kesehatan (Faskes)
* **Sub-Kategori Fokus:** Modus 4 (Upcoding), Modus 9 (Services Unbundling), Modus 6 (Phantom Billing)
* **Susunan Tim:**
  * Ketua Tim: Aditya Pratama (AI & Data Specialist)
  * Anggota: Nurman Hariyanto (Backend & System Integration)
  * Anggota: Muhammad Ali Maulana (Healthcare Business Analyst & UI/UX)
* **Afiliasi / Domisili:** Jakarta, Indonesia | Tim Peserta Mandiri

---

### [SLIDE 2] EXECUTIVE SUMMARY: TRANSFORMASI KE AUDIT PRA-BAYAR
* **Masalah Inti:** Audit retrospektif pasca-bayar membuat pengembalian dana klaim yang bocor sulit dilakukan setelah terlanjur cair ke faskes. Pemeriksaan manual jutaan lembar rekam medis membebani kapasitas kerja petugas verifikator BPJS.
* **Solusi VeriKlaim:** Sistem asistensi audit pra-bayar yang menyaring klaim rumah sakit secara otomatis sebelum pembayaran disetujui, menggabungkan:
  1. *Clinical Semantic NLP* untuk mencocokkan kelayakan catatan medis dokter terhadap kode klaim ICD-10 dan INA-CBGs.
  2. *Graph Anomaly Detection* untuk mengidentifikasi pola penagihan abnormal dan rujukan semu antar-layanan.
* **Nilai Tambah Utama:**
  * **Pencegahan di Garis Depan:** Menghentikan kebocoran sebelum dana dicairkan, bukan mengejar pengembalian dana setelah cair.
  * **Transparansi Bukti Medis (Explainable AI):** Menyajikan alasan diskrepansi klinis objektif dalam hitungan detik.
  * **Jalur Cepat (Fast-Track):** Faskes yang tertib dan patuh menikmati proses pembayaran klaim yang lebih cepat tanpa antrean audit manual yang panjang.

---

### [SLIDE 3] MASALAH & URGENSI: REALITAS OPERASIONAL KLAIM JKN
* **Skala Layanan JKN:**
  * Melayani lebih dari 260 juta penduduk Indonesia (cakupan mencapai 98%).
  * Bekerja sama dengan lebih dari 3.000 Rumah Sakit rujukan (FKRTL) di seluruh Indonesia.
  * Memproses puluhan juta berkas klaim rawat inap dan rawat jalan setiap tahunnya.
* **Beban Verifikasi di Lapangan:**
  * Rasio petugas verifikator BPJS terbatas dibandingkan jutaan lembar berkas rekam medis yang masuk setiap bulan.
  * Waktu rata-rata telaah manual per berkas sangat singkat, sementara dokumen rekam medis mencakup riwayat lab, laporan operasi, dan instruksi medis yang tebal.
* **Titik Kritis Inefisiensi:**
  * Keterlambatan verifikasi manual memperlambat arus kas rumah sakit mitra, sementara pelonggaran verifikasi berisiko meloloskan klaim manipulatif yang merugikan keuangan jaminan sosial.

---

### [SLIDE 4] BUKTI EMPIRIS: DATA INVESTIGASI DAN REFERENSI RESMI
* **Temuan Kasus Faktual Tim Gabungan PK-JKN (KPK, Kemenkes, BPJS Kesehatan, dan BPKP):**
  * *Kasus Riil Juli 2024:* Investigasi KPK mengungkap praktik klaim fiktif (*phantom billing*) dan manipulasi diagnosis (*upcoding*) terorganisir di 3 Rumah Sakit Swasta (dua di Sumatera Utara dan satu di Jawa Tengah) dengan nilai kerugian keuangan negara mencapai **Rp 34 Miliar hingga Rp 35 Miliar**.
  * Modus yang dilakukan: Pembuatan ribuan tagihan sesi fisioterapi fiktif dan klaim operasi katarak tanpa tindakan medis riil melalui pencatutan identitas peserta.
* **Dokumen dan Tautan Referensi Resmi:**
  1. **Liputan Investigasi DW Indonesia (30 Juli 2024):**  
     `https://www.dw.com/id/rs-rugikan-bpjs-kesehatan/a-69802484`  
     *(Bukti visual tangkapan layar liputan disertakan langsung pada slide proposal).*
  2. **Publikasi Resmi BPK RI Perwakilan Sumut / Temuan KPK:**  
     `https://sumut.bpk.go.id/wp-content/uploads/2025/09/KPK-TEMUKAN-FRAUD-KLAIM-BPJS-KESEHATAN-DI-SUMUT-DAN-JATENG-MERUGIKAN-NEGARA-RP-34-MILIAR-1.pdf`
  3. **Payung Regulasi:** Peraturan Menteri Kesehatan (Permenkes) No. 16 Tahun 2019 tentang Pencegahan dan Penanganan Kecurangan (Fraud) dalam Pelaksanaan Program JKN.
* **Sudut Pandang Integritas:** Solusi VeriKlaim dibangun dengan framing **efisiensi risiko dan integritas tata kelola pembiayaan**, memberikan dasar ilmiah yang objektif bagi BPJS maupun faskes mitra.

---

### [SLIDE 5] ANATOMI 3 MODUS KECURANGAN TARGET
1. **Manipulasi Diagnosis / Upcoding (Modus 4):**
   * *Mekanisme:* Menaikkan kode diagnosis atau tingkat keparahan penyakit secara tidak sah demi memperoleh tarif klaim INA-CBGs yang lebih tinggi.
   * *Contoh Lapangan:* Pasien dispepsia ringan dikodekan sebagai ulkus lambung akut dengan perdarahan gastrointestinal, meskipun catatan lab menunjukkan kadar hemoglobin normal dan tidak ada tindakan endoskopi.
2. **Pemecahan Layanan / Unbundling (Modus 9):**
   * *Mekanisme:* Memecah satu kesatuan prosedur medis yang semestinya ditagihkan dalam satu paket tarif menjadi beberapa klaim terpisah pada tanggal yang berdekatan.
   * *Contoh Lapangan:* Prosedur bedah laparoskopi dan perawatan pasca-bedah dipecah menjadi episode rawat jalan terpisah pada hari berikutnya untuk melipatgandakan klaim tindakan.
3. **Klaim Layanan Fiktif / Phantom Billing (Modus 6):**
   * *Mekanisme:* Menagihkan klaim atas tindakan medis, sesi terapi, atau pemeriksaan diagnostik yang tidak pernah diberikan kepada pasien.
   * *Contoh Lapangan:* Menggunakan identitas kartu BPJS peserta dari kegiatan sosial untuk menagihkan ratusan sesi fisioterapi fiktif tanpa kehadiran pasien di faskes.

---

### [SLIDE 6] ARSITEKTUR FUNGSIONAL VERIKLAIM
* **Tiga Modul Utama:**
  1. **Modul Semantic NLP Klinis:** Membaca teks bebas resume medis dokter (catatan gejala, hasil laboratorium, catatan operasi) dan mengevaluasi kesesuaian semantiknya terhadap kriteria diagnostik ICD-10.
  2. **Modul Matriks Regulasi Unbundling:** Mengevaluasi relasi temporal antar-prosedur yang ditagihkan dalam interval waktu tertentu menggunakan basis pengetahuan aturan tarif INA-CBGs.
  3. **Modul Analisis Graf Transaksi:** Memetakan jaringan hubungan antara rumah sakit, dokter penanggung jawab pelayanan (DPJP), spesialisasi, dan pola frekuensi klaim historis untuk mendeteksi lonjakan klaim massal yang mencurigakan.

---

### [SLIDE 7] FITUR KUNCI: PENJELASAN LOGIS BAGI VERIFIKATOR (EXPLAINABLE AI)
* **Tingkatan Skor Risiko Klaim (Risk Score 0-100):**
  * *Skor 0 - 30 (Kategori Hijau / Aman):* Berkas lengkap dan konsisten secara klinis, diproses melalui jalur persetujuan otomatis (fast-track).
  * *Skor 31 - 70 (Kategori Kuning / Perlu Konfirmasi):* Terdapat diskrepansi minor yang memerlukan verifikasi berkas standar.
  * *Skor 71 - 100 (Kategori Merah / Anomali Tinggi):* Indikasi kuat penyimpangan terstruktur, masuk ke antrean investigasi prioritas.
* **Contoh Rekam Bukti Klinis Transparan:**
  * Kode Klaim: Sepsis Berat (A41.9) - Tarif Paket Rp 18.400.000.
  * Temuan Analisis: Catatan lab mencatat leukosit 8.100/uL, suhu tubuh 36.8°C, tidak ada hasil kultur darah positif.
  * Rekomendasi Sistem: Tinjau kesesuaian terhadap kode Demam Bukan Akibat Infeksi Spesifik (R50.9) - Tarif Rp 4.200.000.
  * Selisih Biaya: Rp 14.200.000.

---

### [SLIDE 8] INTEGRASI SISTEM V-CLAIM TANPA MENGUBAH PROSEDUR FASKES
* **Tahapan Integrasi:**
  1. *Pengajuan Berkas:* RS mengunggah berkas klaim digital dan resume medis melalui portal V-Claim BPJS seperti biasa.
  2. *Penapisan Cepat:* Layanan API VeriKlaim memproses teks rekam medis dan menghitung skor risiko dalam waktu rata-rata 1.8 detik.
  3. *Pemisahan Alur:* Klaim valid langsung diteruskan ke antrean pembayaran cepat. Klaim anomali disortir ke dasbor verifikator bersama ringkasan bukti klinis.
  4. *Keputusan Final:* Verifikator BPJS menetapkan persetujuan, permintaan revisi berkas, atau penolakan klaim.

---

### [SLIDE 9] SPESIFIKASI LAPISAN TEKNOLOGI HULU KE HILIR
* **Lapisan 1: Penyerapan dan Sanitasi Data:** Penerimaan berkas via REST API, ekstraksi teks dokumen resume medis, pemisahan elemen data pribadi (PII anonymization).
* **Lapisan 2: Ekstraksi Entitas Klinis:** Clinical Named Entity Recognition (NER) untuk mengidentifikasi diagnosis, obat, tindakan, dan nilai uji laboratorium numerik.
* **Lapisan 3: Mesin Klasifikasi Anomali:** Pencocokan semantik kesesuaian diagnosis, model klasifikasi tabular untuk pola tarif, dan analisis keterhubungan graf jaringan faskes.
* **Lapisan 4: Penyajian Keputusan (Service API):** Layanan mikro FastAPI terenkripsi yang menghasilkan respon JSON terstruktur ke dasbor verifikator BPJS Kesehatan.

---

### [SLIDE 10] KEAMANAN DATA DAN KEPATUHAN UU PDP NO. 27 TAHUN 2022
* **Penggunaan 100% Data Sintetis:** Prototipe awal dikembangkan tanpa data riil peserta JKN yang tidak berizin, mematuhi poin 12 panduan resmi Healthkathon.
* **Pemisahan Identitas dan Enkripsi:** Data identitas (NIK/Nomor Kartu) dipisahkan dari rekam klinis melalui tokenisasi. Data transit dilindungi TLS 1.3 dan penyimpanan data terenkripsi AES-256.
* **Pengendalian Akses Ketat (RBAC):** Hak akses berjenjang hanya untuk verifikator BPJS terotorisasi, dilengkapi rekam jejak audit (audit log) yang tidak dapat dimanipulasi.

---

### [SLIDE 11] KESIAPAN PROTOTIPE FUNGSIONAL (EARLY MVP)
* **Hasil Pengujian Validasi pada 1.500 Kasus Sintetis:**
  * F1-Score Deteksi Upcoding: **89.3%**
  * Akurasi Matriks Unbundling: **93.8%**
  * Waktu Komputasi Inferensi: Rata-rata **1.8 detik** per berkas klaim lengkap.
* **Kesiapan Demonstrasi:** Komponen API backend dan antarmuka penelaah berkas telah terhubung secara fungsional dan siap disimulasikan langsung saat penjurian.

---

### [SLIDE 12] PETA JALAN PENGEMBANGAN MENUJU GRAND FINAL
* **Agustus - September 2026 (Fase 1):** Riset taksonomi regulasi, penyusunan dataset sintetis 1.500 kasus, dan pelatihan model dasar NLP.
* **Oktober 2026 (Fase 2):** Penyelarasan bobot anomali bersama mentor klinis dan TI BPJS Kesehatan serta penyempurnaan penalaran XAI.
* **November 2026 (Fase 3 - Hackathon Onsite):** Pengujian beban throughput, integrasi simulasi API V-Claim, dan finalisasi antarmuka verifikator.
* **Desember 2026 (Fase 4 - Demo Day Grand Final):** Demonstrasi komparatif di hadapan dewan juri dan penyusunan kerangka uji coba pilot project.

---

### [SLIDE 13] ESTIMASI DAMPAK NYATA BAGI EKOSISTEM JKN
* **Bagi BPJS Kesehatan:**
  * Penapisan dini berpotensi mengamankan efisiensi dana jaminan sebesar 2% hingga 3% dari total alokasi risiko klaim anomali.
  * Memangkas waktu telaah dokumen manual petugas verifikator hingga 60%.
* **Bagi Fasilitas Kesehatan (RS Mitra):**
  * Berkas klaim dari faskes yang patuh cair lebih cepat melalui jalur fast-track.
  * Menjadi instrumen audit mandiri bagi koder rekam medis faskes sebelum berkas diajukan ke BPJS.
* **Bagi Peserta JKN:**
  * Menjaga kesinambungan dana jaminan sosial jangka panjang dan mencegah tindakan medis berlebihan yang tidak perlu.

---

### [SLIDE 14] PRINSIP HUMAN-IN-THE-LOOP DAN MITIGASI BIAS
* **Tidak Ada Penolakan Otomatis:** Sistem tidak membatalkan klaim secara sepihak. Keputusan akhir sepenuhnya dipegang oleh verifikator manusia.
* **Kalibrasi Kelas dan Fasilitas RS:** Penilaian mempertimbangkan tipe rumah sakit (Kelas A, B, C, D) dan fasilitas di wilayah terpencil agar tidak terjadi diskriminasi audit.
* **Matriks Aturan Adaptif:** Parameter tarif dan batasan kode klinis dipisahkan dalam modul konfigurasi regulasi sehingga mudah diperbarui saat regulasi Kemenkes berganti.

---

### [SLIDE 15] KOMPOSISI TIM DAN PEMBAGIAN PERAN
* **Aditya Pratama (Ketua Tim):** Penanggung jawab arsitektur model NLP klinis, algoritma pencocokan semantik diagnosis ICD-10, evaluasi metrik akurasi, dan koordinasi tim.
* **Nurman Hariyanto (Anggota Tim):** Penanggung jawab pipeline data, integrasi REST API ke sistem klaim, pengujian throughput latensi, dan kepatuhan privasi data.
* **Muhammad Ali Maulana (Anggota Tim):** Penanggung jawab validasi aturan INA-CBGs dan Permenkes 16/2019, perancangan antarmuka penelaahan berkas verifikator, dan analisis kelayakan efisiensi.

---

### [SLIDE 16] PENUTUP DAN KOMITMEN PESERTA
* **Komitmen Tim:** Tim menyatakan kesiapan mengikuti seluruh rangkaian kegiatan kompetisi secara hybrid: mulai dari webinar pembekalan, sesi coaching mentoring, hackathon onsite, hingga Demo Day Grand Final.
* **Saluran Komunikasi Resmi:**
  * Ketua Tim: Aditya Pratama
  * Status Registrasi: Terdaftar pada portal resmi healthkathon.bpjs-kesehatan.go.id
  * WhatsApp: Nomor ponsel aktif untuk koordinasi grup panitia

---
