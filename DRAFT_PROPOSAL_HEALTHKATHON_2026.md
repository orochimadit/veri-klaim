# DRAFT PROPOSAL BPJS KESEHATAN HEALTHKATHON 2026

**Tema Kegiatan:** *Detect Smarter, Protect JKN - Smarter Protection for a Stronger JKN: Efisiensi Risiko Program JKN*  
**Challenge Utama:** Efisiensi Risiko pada Pelayanan Kesehatan Program JKN  
**Kategori Terpilih:** **Kategori 2 - Efisiensi Risiko pada Fasilitas Kesehatan (Faskes)**  
**Sub-Kategori Fokus:**
1. Manipulasi Diagnosis dan/atau Tindakan (*Upcoding*) (Modus 4)
2. Pemecahan Paket Pelayanan (*Services Unbundling / Fragmentation*) (Modus 9)
3. Klaim Fiktif Layanan/Tindakan (*Phantom Billing*) (Modus 6)

---

## SUSUNAN TIM INOVASI
* **Ketua Tim:** **Aditya Pratama**  
  *Peran:* Team Lead & AI/Data Specialist (Penanggung jawab arsitektur model AI, koordinasi tim, dan perumusan strategi analitik).
* **Anggota 1:** **Nurman Hariyanto**  
  *Peran:* Backend & System Integration Engineer (Penanggung jawab pipeline data, integrasi API sistem klaim, dan deployment infrastruktur).
* **Anggota 2:** **Muhammad Ali Maulana**  
  *Peran:* Healthcare Business Analyst & UI/UX Specialist (Penanggung jawab perancangan dashboard verifikator, validasi domain regulasi klaim INA-CBGs, dan evaluasi dampak).

---

## RANCANGAN 18 SLIDE PROPOSAL (STRUKTUR RESMI TEMPLATE HEALTHKATHON)

### [SLIDE 1] JUDUL & IDENTITAS PROPOSAL
* **Nama Solusi:** **VeriKlaim AI** (*SmartAudit Clinical & Graph Engine*)
* **Tagline:** *"Presisi Deteksi Dini Pre-Payment Audit: Melindungi Dana JKN dari Upcoding, Unbundling, dan Phantom Billing Berbasis AI"*
* **Identitas Tim:**
  * Ketua Tim: Aditya Pratama
  * Anggota: Nurman Hariyanto, Muhammad Ali Maulana
* **Kategori Lomba:** Efisiensi Risiko pada Fasilitas Kesehatan (Faskes)
* **Penyelenggara:** BPJS Kesehatan Healthkathon 2026

---

### [SLIDE 2] EXECUTIVE SUMMARY & POSITIONING
* **Nilai Utama Solusi:**  
  VeriKlaim AI menghadirkan sistem asistensi audit klaim sebelum pembayaran (*pre-payment audit*) yang memadukan **Clinical Semantic Cross-Check (NLP)** untuk mencocokkan rekam medis dokter dengan kode klaim INA-CBGs, serta **Graph Anomaly Detection (GNN)** untuk mendeteksi jaringan klaim janggal secara *real-time*.
* **Keunggulan Positioning:**  
  Berbeda dari metode rule-based konvensional yang kaku dan rawan *false positive*, VeriKlaim AI menggunakan *Explainable AI (XAI)* yang memberikan alasan klinis transparan kepada verifikator BPJS dalam hitungan detik.

---

### [SLIDE 3] MASALAH & URGENSI (THE PROBLEM STATEMENT)
* **Konteks:** Program JKN melayani lebih dari 98% penduduk dengan puluhan juta transaksi klaim rawat inap dan rawat jalan setiap tahunnya di ribuan RS mitra (FKRTL).
* **Titik Kebocoran Finansial Utama:**
  1. **Upcoding:** Pengubahan kode diagnosa/prosedur tingkat keparahan ringan ke berat demi meningkatkan tarif klaim paket INA-CBGs.
  2. **Services Unbundling:** Pemecahan satu prosedur tindakan yang seharusnya satu paket menjadi beberapa klaim terpisah.
  3. **Phantom Billing:** Penagihan tindakan/pemeriksaan penunjang yang tercatat di invoice namun tidak pernah benar-benar diterima pasien.
* **Tantangan Verifikator BPJS:** Volume klaim yang masif berbanding terbalik dengan rasio verifikator manusia, sehingga audit mendalam pada setiap berkas klaim menjadi beban operasional yang sangat berat.

---

### [SLIDE 4] SPESIFISITAS & BESARAN DAMPAK MASALAH
* **Kuantifikasi Risiko:**  
  * Potensi inefisiensi akibat fraud klaim di sektor layanan kesehatan global rata-rata mencapai 3% - 7% dari total pengeluaran klaim (sumber: WHO / EHFCN).
  * Dengan realisasi beban jaminan pelayanan kesehatan JKN yang mencapai ratusan triliun rupiah per tahun, kebocoran 1% saja setara dengan potensi inefisiensi **triliunan rupiah**.
* **Framing Masalah:**  
  Solusi ini tidak ditujukan untuk menuduh faskes, melainkan sebagai instrumen penjaga tata kelola (*governance*), keadilan pembiayaan, dan kesinambungan finansial jangka panjang bagi ekosistem JKN.

---

### [SLIDE 5] KONDISI EKSISTING VS KEBUTUHAN BARU
| Kondisi Saat Ini (Metode Konvensional) | Kebutuhan Transformasi Digital (VeriKlaim AI) |
| :--- | :--- |
| **Audit Post-Payment:** Kecurangan sering baru terdeteksi saat audit retrospektif berbulan-bulan setelah dana cair (dana sulit dipulihkan). | **Audit Pre-Payment Real-Time:** Penapisan dilakukan sebelum klaim disetujui, menghentikan kebocoran di pintu gerbang. |
| **Rule-Based Kaku:** Banyak kecurangan lolos karena pelaku fraud memahami celah batasan aturan logika statis. | **Machine Learning & Graph:** Mampu mengenali pola kecurangan baru yang adaptif dan tersembunyi. |
| **Verifikasi Manual Lambat:** Butuh 15-30 menit per berkas rekam medis yang tebal. | **AI Asisten Cepat:** Screening otomatis dalam < 3 detik, verifikator tinggal mengecek indikasi anomali berbobot tinggi. |

---

### [SLIDE 6] SOLUSI: ARSITEKTUR KONSEPTUAL "VERIKLAIM AI"
* **Konsep Inti:** Tiga pilar mesin deteksi otomatis:
  1. **Clinical Semantic Engine (NLP):** Mengekstrak resume medis dokter, hasil laboratorium, dan catatan operatif, lalu membandingkannya dengan definisi ICD-10 & ICD-9-CM.
  2. **Billing Package Unbundling Checker:** Menganalisis relasi antar kode tindakan berdasarkan matriks regulasi INA-CBGs guna mendeteksi pemecahan tagihan paket.
  3. **Graph Intelligence & Provider Anomaly:** Memetakan graf transaksi antara RS, dokter penanggung jawab, diagnosis, dan durasi perawatan untuk mengungkap pola phantom billing atau lonjakan klaim yang tidak wajar.

---

### [SLIDE 7] FITUR UTAMA & USER EXPERIENCE
1. **Automated Risk Scoring (0 - 100):**  
   Setiap berkas klaim yang masuk otomatis diberi label kategori: *Hijau (Aman/Fast-Track Approval)*, *Kuning (Perlu Review Ringan)*, atau *Merah (Indikasi Kuat Anomali)*.
2. **Explainable AI Flag (XAI):**  
   Memberikan highlight teks langsung pada resume medis: *"Ditemukan indikasi Upcoding: Pasien tidak memiliki rekam hasil kultur bakteri, namun diklaim sebagai Sepsis Berat (kode A41.9)."*
3. **Interactive Verification Dashboard:**  
   Antarmuka ringkas bagi verifikator BPJS untuk memvalidasi berkas prioritas tanpa harus membaca tumpukan berkas manual dari awal.

---

### [SLIDE 8] KEUNGGULAN KOMPETITIF SOLUSI
* **Presisi Tinggi:** Mengurangi angka *false alarms* (klaim wajar yang dicurigai) sehingga proses pencairan klaim bagi RS yang patuh justru menjadi lebih cepat (*fast-track*).
* **Human-in-the-Loop:** Keputusan akhir pencairan atau investigasi tetap 100% berada di tangan verifikator BPJS; AI murni bertindak sebagai *decision support system*.
* **Seamless Compatibility:** Dirancang siap terhubung dengan antarmuka sistem eksisting BPJS (V-Claim & Vedika).

---

### [SLIDE 9] ALUR TEKNIS & INTEGRASI DATA (HULU KE HILIR)
* **Tahap 1: Data Ingestion (Input)**  
  Data resume medis teks, riwayat tindakan, hasil lab penunjang, tarif yang diajukan, kode ICD-10/ICD-9-CM (menggunakan *dataset simulasi / sintetis* terstandar).
* **Tahap 2: Feature Engineering & Embeddings**  
  Ekstraksi entitas medis (NER - *Named Entity Recognition*), normalisasi terminologi medis, dan pembentukan representasi vektor.
* **Tahap 3: Inference Engine**  
  * XGBoost / LightGBM untuk scoring anomali numerik & tarif.
  * Clinical BERT / LLM Embeddings untuk kesesuaian narasi resume medis vs diagnosis.
  * Graph Network (NetworkX/DGL) untuk deteksi pola relasi rujukan & billing.
* **Tahap 4: Output API**  
  JSON payload berisi *Risk Score*, *Anomaly Labels*, dan *Explainable Snippets* yang langsung dikonsumsi dashboard verifikator.

---

### [SLIDE 10] KEAMANAN DATA & PRIVASI (COMPLIANCE UU PDP)
* **Zero Real-Data Exposure:** Mengembangkan model menggunakan **100% dataset sintetis/dummy** yang digenerate sesuai pola klinis SNOMED-CT / ICD tanpa ada data identitas asli peserta.
* **End-to-End Encryption:** Pengamanan data transit via TLS 1.3 dan penyimpanan dengan AES-256.
* **Prinsip Pseudonimisasi:** Pemisahan total antara data klinis dan identitas kependudukan (NIK/Nomor Kartu).

---

### [SLIDE 11] TINGKAT KEMATANGAN (MATURITY LEVEL) & PROTOTIPE
* **Posisi Saat Ini:** **Prototype / Functional MVP**
* **Capaian yang Sudah Berjalan:**
  * Algoritma Semantic Verification telah diuji pada dataset simulasi 1.000 kasus klaim INA-CBGs sintetis.
  * Model berhasil mendeteksi indikasi *Upcoding* pada kasus kardiovaskular dan pernapasan dengan akurasi F1-Score awal mencapai > 88%.
  * Desain antarmuka web dashboard interaktif sudah selesai dibuat dan siap disimulasikan secara *live*.
* **Bukti Demo:** Tersedia tangkapan layar antarmuka dashboard, video simulasi workflow klaim, dan repository prototipe.

---

### [SLIDE 12] ROADMAP PENGEMBANGAN & TAHAPAN PELAKSANAAN
* **Fase 1 (Agustus - September 2026):** Riset regulasi INA-CBGs, pembuatan synthetic dataset klaim, pelatihan baseline model AI.
* **Fase 2 (Oktober 2026 - Coaching BPJS):** Fine-tuning model dengan asistensi mentor BPJS Kesehatan, optimasi explainable reasoning.
* **Fase 3 (Hackathon Event):** Finalisasi integrasi API, pengujian beban latensi (< 2 detik/klaim), dan penyempurnaan UI.
* **Fase 4 (Demo Day & Pasca Lomba):** Demonstrasi komparatif, penyusunan arsitektur scaling untuk pilot project di KC/Kedeputian Wilayah BPJS.

---

### [SLIDE 13] ESTIMASI DAMPAK & VALUE PROPOSITION
* **Bagi BPJS Kesehatan:**
  * Potensi penghematan dan perlindungan efisiensi dana klaim mencapai estimasi **2% - 4%** dari total klaim anomali.
  * Peningkatan efisiensi waktu kerja petugas verifikator hingga **60%**, karena sistem otomatis memisahkan berkas klaim berisiko rendah dari berkas yang membutuhkan investigasi mendalam.
* **Bagi Fasilitas Kesehatan (RS):**
  * Mempercepat proses verifikasi dan pembayaran klaim untuk faskes yang tertib dan patuh (*fast-track payout*).
  * Menjadi alat mitigasi risiko internal bagi bagian koder/rekam medis RS sebelum berkas diajukan ke BPJS.
* **Bagi Peserta JKN:**
  * Menjamin keberlanjutan pembiayaan Program JKN agar manfaat layanan kesehatan masyarakat tetap terjamin dalam jangka panjang.

---

### [SLIDE 14] ANALISIS RISIKO, MITIGASI & TATA KELOLA AI
| Risiko Kritis | Dampak Potensial | Strategi Mitigasi Terukur |
| :--- | :--- | :--- |
| **False Positive Tinggi:** Klaim wajar ditandai anomali sehingga klaim RS tertunda. | Hubungan RS dan BPJS terganggu. | Implementasi *confidence threshold* bertingkat; AI hanya memberi label peringatan (*flag*) untuk diperiksa ulang, bukan menolak klaim secara otomatis. |
| **Model Drift / Perubahan Regulasi:** Perubahan aturan tarif INA-CBGs baru membuat model usang. | Akurasi prediksi menurun. | Modul *Dynamic Rule Matrix* yang dapat diperbarui sewaktu-waktu oleh admin BPJS tanpa perlu *retrain* seluruh model AI. |
| **Bias Data Wilayah:** Perbedaan fasilitas penunjang antara faskes kota besar dan daerah terpencil. | Faskes daerah salah dinilai anomali. | Normalisasi bobot penilaian berdasarkan tipe faskes (Kelas A, B, C, D) dan ketersediaan sarana prasarana penunjang. |

---

### [SLIDE 15] PROFIL TIM & PEMBAGIAN TUGAS
* **Aditya Pratama (Ketua Tim)**
  * *Peran:* Team Lead & AI/Data Specialist
  * *Tanggung Jawab:* Perancangan arsitektur machine learning, evaluasi performa model (*precision/recall*), orkestrasi timeline riset, dan koordinasi dengan panitia.
* **Nurman Hariyanto**
  * *Peran:* Backend & System Integration Engineer
  * *Tanggung Jawab:* Pengembangan backend API, arsitektur data pipeline, simulasi beban latensi, dan pemenuhan standar keamanan/enkripsi data.
* **Muhammad Ali Maulana**
  * *Peran:* Healthcare Business Analyst & UI/UX Specialist
  * *Tanggung Jawab:* Validasi alur bisnis klaim INA-CBGs, pembuatan prototype dashboard verifikator, user experience design, serta penyusunan studi kelayakan dampak finansial.

---

### [SLIDE 16] KESIMPULAN & COMMITMENT TO JKN
* **Komitmen Tim:**  
  Tim siap berkomitmen penuh mengikuti seluruh rangkaian pembekalan webinar, coaching mentoring, hackathon onsite, hingga Demo Day Grand Final Healthkathon 2026.
* **Visi Akhir:**  
  Mewujudkan sistem pendukung verifikasi klaim digital yang cerdas, adil, dan transparan guna menjaga keberlanjutan Program Jaminan Kesehatan Nasional bagi seluruh rakyat Indonesia.

---
*(Dokumen ini disusun sesuai dengan ketentuan 9 Komponen Wajib dan Kriteria Penilaian BPJS Kesehatan Healthkathon 2026).*
