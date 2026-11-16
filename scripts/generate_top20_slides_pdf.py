"""
Generator Script: Project Final Slide Deck Healthkathon 2026 (Tahap 20 Besar)
Mengikuti Format Baku Panduan 20 Besar BPJS Kesehatan:
- 16:9 Landscape (960 x 540 pt)
- Berkas Output: docs/Aqila Digital.pdf (< 15 MB) & docs/Project_Final_Healthkathon_2026_VeriKlaim.pdf
- Memuat secara lengkap:
  1. Perkenalan Tim (Foto ketiga anggota tim)
  2. Perubahan Setelah Coaching (4 Masukan Utama Mentor & Tindakan Solusi)
  3. Bukti Nyata Sebelum vs Sesudah Coaching
  4. Ringkasan Solusi & Alur 5-Stage Pipeline
  5. Demo Fitur Baru: Batch Upload (CSV/Excel/JSON) & Live Workstation
  6. Penjelasan 4 Fitur Utama
  7. Arsitektur Teknis & Pembobotan Ensemble 60% XGBoost + 40% Random Forest
  8. Keamanan UU PDP No. 27/2022 & Protokol Resume Medis Faskes
  9. Hasil Uji Validasi Terukur (50.000 Data Riil & 10.000 Skenario Stres)
  10. Kalkulasi Kebutuhan Infrastruktur Implementasi Nasional (Beban 120 Juta Klaim)
  11. Slide Penutup & Tautan Live Demo (https://veriklaim.absolute-tech.id)
"""

import os
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

NAVY_DARK = HexColor("#0A192F")
NAVY_SLATE = HexColor("#1E293B")
BPJS_GREEN = HexColor("#00875A")
BPJS_GREEN_LIGHT = HexColor("#E6F4EA")
BPJS_GREEN_DARK = HexColor("#006644")
BPJS_BLUE = HexColor("#0B69A3")
BPJS_BLUE_LIGHT = HexColor("#EBF5FB")
ACCENT_RED = HexColor("#DE350B")
ACCENT_RED_LIGHT = HexColor("#FFEBE6")
ACCENT_AMBER = HexColor("#FFAB00")
ACCENT_AMBER_LIGHT = HexColor("#FFF0B3")
TEXT_DARK = HexColor("#0F172A")
TEXT_MUTED = HexColor("#475569")
TEXT_LIGHT = HexColor("#94A3B8")
BG_CARD = HexColor("#F8FAFC")
BORDER_LIGHT = HexColor("#E2E8F0")
WHITE = HexColor("#FFFFFF")

PAGE_WIDTH = 960.0
PAGE_HEIGHT = 540.0
TOTAL_SLIDES = 12

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "docs", "assets")


def draw_header(c, title_text, slide_num_label="", current_slide=1, total_slides=TOTAL_SLIDES):
    c.setFillColor(BPJS_GREEN)
    c.rect(0, PAGE_HEIGHT - 6, PAGE_WIDTH, 6, fill=True, stroke=False)
    
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(48, PAGE_HEIGHT - 28, "Healthkathon BPJS Kesehatan 2026  |  Tahap 20 Besar Menuju Final Offline")
    
    c.setFont("Helvetica", 8.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(410, PAGE_HEIGHT - 28, "|  Detect Smarter, Protect JKN - Smarter Protection for a Stronger JKN")
    
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(TEXT_DARK)
    c.drawString(48, PAGE_HEIGHT - 54, title_text)
    
    if slide_num_label:
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(BPJS_GREEN)
        c.drawRightString(PAGE_WIDTH - 48, PAGE_HEIGHT - 54, str(slide_num_label))
    
    c.setStrokeColor(BORDER_LIGHT)
    c.setLineWidth(1)
    c.line(48, PAGE_HEIGHT - 64, PAGE_WIDTH - 48, PAGE_HEIGHT - 64)
    c.line(48, 28, PAGE_WIDTH - 48, 28)
    
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(BPJS_GREEN)
    c.drawString(48, 16, "VeriKlaim")
    
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_MUTED)
    c.drawString(98, 16, "- Asistensi Audit Pra-Bayar Klaim FKRTL Berbasis AI & Human-in-the-Loop  |  Tim Aqila Digital")
    
    c.drawRightString(PAGE_WIDTH - 48, 16, f"Slide {current_slide} dari {total_slides}")


def draw_card(c, x, y, w, h, bg_color=BG_CARD, border_color=BORDER_LIGHT, radius=6):
    c.setFillColor(bg_color)
    c.setStrokeColor(border_color)
    c.setLineWidth(1)
    c.roundRect(x, y, w, h, radius, fill=True, stroke=True)


# =============================================================================
# SLIDE 1: COVER
# =============================================================================
def draw_slide_1_cover(c):
    c.setFillColor(NAVY_DARK)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    c.setFillColor(BPJS_GREEN)
    c.rect(0, PAGE_HEIGHT - 8, PAGE_WIDTH, 8, fill=True, stroke=False)
    
    logo_path = os.path.join(ASSETS_DIR, "template_p1_img1_Image6.png")
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 48, PAGE_HEIGHT - 82, width=160, height=52, preserveAspectRatio=True, mask='auto')
        
    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(WHITE)
    c.drawString(48, PAGE_HEIGHT - 122, "PROJECT FINAL HEALTHKATHON 2026")
    
    c.setFont("Helvetica-Bold", 15)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 146, "Tahap 20 Besar: Hasil Pembinaan & Penyempurnaan Coaching Mentor")
    
    c.setFont("Helvetica", 10.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 168, "Detect Smarter, Protect JKN - Smarter Protection for a Stronger JKN: Efisiensi Risiko Program JKN")
    
    # Hero Title Box
    draw_card(c, 48, PAGE_HEIGHT - 275, PAGE_WIDTH - 96, 92, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN)
    c.drawString(68, PAGE_HEIGHT - 200, "N A M A   S O L U S I   &   I N O V A S I")
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(WHITE)
    c.drawString(68, PAGE_HEIGHT - 230, "VeriKlaim")
    c.setFont("Helvetica", 11)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(68, PAGE_HEIGHT - 252, "Sistem Asistensi Audit Pra-Bayar untuk Mitigasi Upcoding, Unbundling, dan Phantom Billing")
    
    # 4 Meta Cards
    card_w = (PAGE_WIDTH - 96 - 36) / 4.0
    card_h = 135
    card_y = 48
    
    meta_items = [
        ("NAMA TIM", "Aqila Digital", "Peserta Resmi 20 Besar", BPJS_GREEN, [
            "Universitas Nahdlatul Ulama Kalbar",
            "& Universitas Tanjungpura",
            "Pontianak, Kalimantan Barat"
        ]),
        ("KATEGORI KOMPETISI", "Pemberi Kerja", "Sub: Efisiensi Risiko Faskes", BPJS_BLUE, [
            "Kode: C03.04 (Klaim FKRTL)",
            "Audit Pra-Bayar Rumah Sakit",
            "Pencegahan Fraud JKN"
        ]),
        ("STATUS INOVASI", "TRL 6 Operasional", "Terkalibrasi Pasca-Coaching", HexColor("#7E22CE"), [
            "Ensemble 60% XGB + 40% RF",
            "Batch Ingestion & Webhook SIMRS",
            "Live: veriklaim.absolute-tech.id"
        ]),
        ("KONTAK TIM", "Aditya Pratama", "Ketua Tim / Lead AI", HexColor("#00875A"), [
            "WA: 0856-5441-1081",
            "Email: aditya.pratama@unukalbar.ac.id",
            "Alumni STEI ITB"
        ])
    ]
    
    for i, (label, val, sub, col, desc_lines) in enumerate(meta_items):
        cx = 48 + i * (card_w + 12)
        draw_card(c, cx, card_y, card_w, card_h, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=6)
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(col)
        c.drawString(cx + 12, card_y + card_h - 20, label)
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(WHITE)
        c.drawString(cx + 12, card_y + card_h - 42, val)
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(TEXT_LIGHT)
        c.drawString(cx + 12, card_y + card_h - 58, sub)
        
        c.setStrokeColor(HexColor("#233554"))
        c.line(cx + 12, card_y + card_h - 66, cx + card_w - 12, card_y + card_h - 66)
        
        c.setFont("Helvetica", 7.8)
        c.setFillColor(TEXT_LIGHT)
        ly = card_y + card_h - 82
        for dl in desc_lines:
            c.drawString(cx + 12, ly, dl)
            ly -= 13


# =============================================================================
# SLIDE 2: PERKENALAN TIM
# =============================================================================
def draw_slide_2_team(c):
    draw_header(c, "Perkenalan Tim Pengusul", slide_num_label="1", current_slide=2)
    
    c.setFont("Helvetica", 9.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(48, PAGE_HEIGHT - 80, "Nama tim: ")
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(104, PAGE_HEIGHT - 80, "Aqila Digital")
    
    c.setFont("Helvetica", 9.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(200, PAGE_HEIGHT - 80, "|   Kategori: ")
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_GREEN)
    c.drawString(260, PAGE_HEIGHT - 80, "Pemberi Kerja / Efisiensi Risiko pada Faskes (KLAIM C03.04)")
    
    card_w = (PAGE_WIDTH - 96 - 32) / 3.0
    card_h = 360
    card_y = 52
    avatar_sz = 68
    pill_w = 70
    pill_h = 15
    
    # Member 1: Aditya Pratama
    x1 = 48
    draw_card(c, x1, card_y, card_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    img_aditya = os.path.join(ASSETS_DIR, "avatar_aditya.png")
    if os.path.exists(img_aditya):
        c.drawImage(img_aditya, x1 + (card_w - avatar_sz) / 2, card_y + card_h - 84, avatar_sz, avatar_sz, mask='auto')
    
    draw_card(c, x1 + (card_w - pill_w) / 2, card_y + card_h - 104, pill_w, pill_h, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=7.5)
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawCentredString(x1 + card_w / 2, card_y + card_h - 97, "KETUA TIM")
    
    c.setFont("Helvetica-Bold", 12.0)
    c.setFillColor(TEXT_DARK)
    c.drawCentredString(x1 + card_w / 2, card_y + card_h - 120, "Aditya Pratama, S.T., M.T.")
    c.setFont("Helvetica-Bold", 9.0)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x1 + card_w / 2, card_y + card_h - 134, "Ketua Tim / Lead AI & Arsitektur")
    
    c.setStrokeColor(BORDER_LIGHT)
    c.line(x1 + 16, card_y + card_h - 144, x1 + card_w - 16, card_y + card_h - 144)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(x1 + 16, card_y + card_h - 160, "AFILIASI & REKAM JEJAK:")
    
    lines_m1 = [
        "- Dosen Tetap Prodi Sistem Informasi,",
        "  Universitas Nahdlatul Ulama Kalbar",
        "- Alumni S1 & S2 STEI ITB",
        "  (Institut Teknologi Bandung)",
        "- Riset: Machine Learning Tabular, TreeSHAP",
        "  Explainability, High-Throughput API Engine,",
        "  dan Sistem Deteksi Anomali Klaim Kesehatan",
        "- Lead implementasi arsitektur ensemble 60:40",
        "  dan integrasi model LLM pendukung",
        "- Kontak WA: 0856-5441-1081"
    ]
    cur_y = card_y + card_h - 176
    for l in lines_m1:
        c.drawString(x1 + 16, cur_y, l)
        cur_y -= 13.5
        
    # Member 2: Nurman Hariyanto
    x2 = x1 + card_w + 16
    draw_card(c, x2, card_y, card_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    img_nurman = os.path.join(ASSETS_DIR, "avatar_nurman.png")
    if os.path.exists(img_nurman):
        c.drawImage(img_nurman, x2 + (card_w - avatar_sz) / 2, card_y + card_h - 84, avatar_sz, avatar_sz, mask='auto')
        
    draw_card(c, x2 + (card_w - pill_w) / 2, card_y + card_h - 104, pill_w, pill_h, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=7.5)
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x2 + card_w / 2, card_y + card_h - 97, "ANGGOTA 1")
    
    c.setFont("Helvetica-Bold", 12.0)
    c.setFillColor(TEXT_DARK)
    c.drawCentredString(x2 + card_w / 2, card_y + card_h - 120, "Nurman Hariyanto, S.ST., M.T.")
    c.setFont("Helvetica-Bold", 9.0)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x2 + card_w / 2, card_y + card_h - 134, "Lead Rekayasa Data & Infrastruktur")
    
    c.setStrokeColor(BORDER_LIGHT)
    c.line(x2 + 16, card_y + card_h - 144, x2 + card_w - 16, card_y + card_h - 144)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(x2 + 16, card_y + card_h - 160, "AFILIASI & REKAM JEJAK:")
    
    lines_m2 = [
        "- Dosen Tetap Prodi Sistem Informasi,",
        "  Universitas Nahdlatul Ulama Kalbar",
        "- Alumni S2 STEI ITB & D4 POLBAN",
        "- Pengalaman: Big Data Engineering,",
        "  Pipeline ETL Skala Besar (50.000+ klaim),",
        "  Data Preprocessing & Sanitasi PDP",
        "- Lead pengembang modul Batch Ingestion,",
        "  Webhook SIMRS, & Kluster Evaluasi Semantik",
        "- Spesialisasi: Cloud Systems & Reliability"
    ]
    cur_y = card_y + card_h - 176
    for l in lines_m2:
        c.drawString(x2 + 16, cur_y, l)
        cur_y -= 13.5

    # Member 3: M. Ali Maulana
    x3 = x2 + card_w + 16
    draw_card(c, x3, card_y, card_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    img_ali = os.path.join(ASSETS_DIR, "avatar_ali.png")
    if os.path.exists(img_ali):
        c.drawImage(img_ali, x3 + (card_w - avatar_sz) / 2, card_y + card_h - 84, avatar_sz, avatar_sz, mask='auto')
        
    draw_card(c, x3 + (card_w - pill_w) / 2, card_y + card_h - 104, pill_w, pill_h, bg_color=HexColor("#F3E8FF"), border_color=HexColor("#7E22CE"), radius=7.5)
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawCentredString(x3 + card_w / 2, card_y + card_h - 97, "ANGGOTA 2")
    
    c.setFont("Helvetica-Bold", 12.0)
    c.setFillColor(TEXT_DARK)
    c.drawCentredString(x3 + card_w / 2, card_y + card_h - 120, "M. Ali Maulana, M.Kep.")
    c.setFont("Helvetica-Bold", 9.0)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x3 + card_w / 2, card_y + card_h - 134, "Lead Domain Klinis & Kepatuhan")
    
    c.setStrokeColor(BORDER_LIGHT)
    c.line(x3 + 16, card_y + card_h - 144, x3 + card_w - 16, card_y + card_h - 144)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawString(x3 + 16, card_y + card_h - 160, "AFILIASI & REKAM JEJAK:")
    
    lines_m3 = [
        "- Dosen Tetap Prodi Keperawatan,",
        "  Fakultas Kedokteran Univ. Tanjungpura",
        "- Magister Keperawatan Univ. Diponegoro",
        "- Keahlian: Tata Kelola Mutu Layanan FKRTL,",
        "  Audit Klinis Rumah Sakit & Kepatuhan JKN",
        "- Penguasaan Regulasi: Permenkes 26/2021",
        "  (Tarif INA-CBG), Permenkes 16/2019",
        "  (Fraud JKN) & Permenkes 24/2022 (RME)",
        "- Perancang protokol verifikasi klinis faskes"
    ]
    cur_y = card_y + card_h - 176
    for l in lines_m3:
        c.drawString(x3 + 16, cur_y, l)
        cur_y -= 13.5


# =============================================================================
# SLIDE 3: PERUBAHAN SETELAH COACHING (MASUKAN MENTOR & TINDAKAN)
# =============================================================================
def draw_slide_3_coaching_feedback(c):
    draw_header(c, "Perubahan Setelah Coaching: Masukan Mentor & Tindakan Solusi", slide_num_label="2A", current_slide=3)
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(48, PAGE_HEIGHT - 80, "Fokus Penilaian Utama Tahap 20 Besar: Responsibilitas Tim terhadap Masukan Konstruktif Mentor Internal BPJS Kesehatan")
    
    grid_w = (PAGE_WIDTH - 96 - 16) / 2.0
    grid_h = 175
    
    boxes = [
        (48, PAGE_HEIGHT - 268, "MASUKAN 1: INGESTION & INTEGRASI DATA KLAIM", BPJS_GREEN, [
            "Catatan Mentor: Belum tersedia fitur upload atau integrasi data klaim yang",
            "dapat langsung diproses sistem dalam jumlah massal oleh rumah sakit/verifikator.",
            "TINDAKAN NYATA TIM AQILA DIGITAL:",
            "1. Membangun Batch Upload Portal (POST /api/claims/upload) dengan drag-and-drop",
            "   yang mendukung file CSV, Excel (.xlsx), dan JSON lengkap dengan validasi skema.",
            "2. Membangun Webhook Integrasi SIMRS (POST /api/claims/batch-audit) untuk koneksi",
            "   langsung Machine-to-Machine dari SIMRS RS / e-Klaim Kemenkes ke VeriKlaim.",
            "3. Menyediakan Template Unduhan Resmi (GET /api/claims/upload/template)."
        ]),
        (48 + grid_w + 16, PAGE_HEIGHT - 268, "MASUKAN 2: PEMBOBOTAN SKORING ENSEMBLE AI", BPJS_BLUE, [
            "Catatan Mentor: Belum ada pembobotan skoring akurasi dari hasil penggunaan",
            "algoritma XGBoost dan Random Forest (disarankan ditambahkan rasio terukur).",
            "TINDAKAN NYATA TIM AQILA DIGITAL:",
            "1. Mengimplementasikan Ensemble Weighting: 60% XGBoost + 40% Random Forest.",
            "   Formula: Skor Komposit = (0.60 * Skor_XGBoost) + (0.40 * Skor_RandomForest).",
            "2. XGBoost (60%) unggul menangkap pola non-linear tarif ekstrem; Random Forest",
            "   (40%) mereduksi variansi data dan mencegah overfitting.",
            "3. Menghasilkan akurasi 98.44%, Recall 100% (Zero False Negative), dan visualisasi UI."
        ]),
        (48, 52, "MASUKAN 3: MEKANISME RESUME MEDIS & SENGKETA RS", HexColor("#7E22CE"), [
            "Catatan Mentor: Untuk klarifikasi RS yang meminta resume medis pasien,",
            "belum ditentukan mekanisme pemberian data rekam medis pasiennya seperti apa.",
            "TINDAKAN NYATA TIM AQILA DIGITAL (KEPATUHAN UU PDP NO. 27/2022):",
            "1. DILARANG upload file PDF rekam medis utuh (mencegah kebocoran NIK/Privasi).",
            "2. Menerapkan Text-Only Structured Snippet Protocol: RS menyertakan stempel",
            "   waktu RME (ISO 8601), Tanda Tangan Digital DPJP, dan kutipan objektif CPPT/lab.",
            "3. Evaluasi Semantik AI untuk mendeteksi bukti klinis riil vs sanggahan klise/nihil."
        ]),
        (48 + grid_w + 16, 52, "MASUKAN 4: KALKULASI INFRASTRUKTUR NASIONAL", HexColor("#00875A"), [
            "Catatan Mentor: Hitung kebutuhan infrastruktur untuk sistem tersebut jika",
            "nantinya akan diimplementasikan secara nasional di seluruh faskes se-Indonesia.",
            "TINDAKAN NYATA TIM AQILA DIGITAL:",
            "1. Profil Beban Nasional: ~100-120 Juta klaim/thn (rata-rata 350k klaim/hari, peak 150 TPS).",
            "2. Latensi core VeriKlaim < 0.15 ms & throughput > 400 req/dtk per worker.",
            "3. Kebutuhan Produksi Nasional: Cukup 4-Node Active-Active Cluster (Total 128 vCPU,",
            "   256 GB RAM, SSD NVMe 2 TB) mampu melayani 1.600 TPS (> 10x beban peak BPJS)."
        ])
    ]
    
    for x, y, title, col, lines in boxes:
        draw_card(c, x, y, grid_w, grid_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=6)
        draw_card(c, x, y + grid_h - 26, grid_w, 26, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=6)
        c.setFont("Helvetica-Bold", 8.8)
        c.setFillColor(col)
        c.drawString(x + 12, y + grid_h - 18, title)
        
        c.setFont("Helvetica", 7.6)
        c.setFillColor(TEXT_DARK)
        ly = y + grid_h - 42
        for idx, line in enumerate(lines):
            if "Catatan Mentor:" in line:
                c.setFont("Helvetica-Bold", 7.6)
                c.setFillColor(ACCENT_RED)
            elif "TINDAKAN NYATA" in line:
                c.setFont("Helvetica-Bold", 7.6)
                c.setFillColor(BPJS_GREEN_DARK)
            else:
                c.setFont("Helvetica", 7.5)
                c.setFillColor(TEXT_DARK)
            c.drawString(x + 12, ly, line)
            ly -= 12


# =============================================================================
# SLIDE 4: BUKTI NYATA HASIL PERUBAHAN (SEBELUM VS SESUDAH)
# =============================================================================
def draw_slide_4_before_after(c):
    draw_header(c, "Bukti Hasil Perubahan: Matriks Komparasi Sebelum vs Sesudah Coaching", slide_num_label="2B", current_slide=4)
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(48, PAGE_HEIGHT - 80, "Peningkatan Kematangan Sistem (Technology Readiness Level 6) Menjawab Seluruh Evaluasi Mentor")
    
    # Table Header
    ty = PAGE_HEIGHT - 105
    th_h = 24
    col_w = [160, 220, 260, 224]
    
    c.setFillColor(NAVY_DARK)
    c.rect(48, ty - th_h, PAGE_WIDTH - 96, th_h, fill=True, stroke=False)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(WHITE)
    c.drawString(56, ty - 16, "PARAMETER EVALUASI")
    c.drawString(56 + col_w[0], ty - 16, "SEBELUM COACHING")
    c.drawString(56 + col_w[0] + col_w[1], ty - 16, "SESUDAH COACHING (VERSI TERKINI)")
    c.drawString(56 + col_w[0] + col_w[1] + col_w[2], ty - 16, "IMPAK BAGI BPJS KESEHATAN")
    
    rows = [
        ("1. Ingestion Data Klaim", 
         "Input klaim individual per berkas;\nBelum ada batch upload atau webhook SIMRS.", 
         "Batch Upload Portal (CSV, Excel .xlsx, JSON)\n+ Endpoint Webhook SIMRS (POST /batch-audit).",
         "Faskes dapat audit 1.000+ klaim sekaligus\nsebelum dikirim ke e-Klaim/VClaim BPJS."),
        
        ("2. Pembobotan Model AI", 
         "Model tunggal berbasis batas deviasi;\nBelum ada skoring pembobotan ensemble.", 
         "Ensemble Weighting: 60% XGBoost + 40% RF;\nSkor komposit transparan divisualisasikan di UI.",
         "Akurasi 98.44%, Recall 100% (Zero False Neg),\nmeminimalkan risiko sengketa klaim palsu."),
        
        ("3. Sengketa & Resume Medis", 
         "Mekanisme klarifikasi resume medis belum ada;\nBeresiko kirim dokumen PDF fisik tanpa aturan.", 
         "Text-Only Structured Snippet Protocol (Anti-PDP)\n+ Tanda Tangan Digital DPJP + Evaluasi Semantik.",
         "Kepatuhan 100% UU PDP No. 27/2022;\nSanggahan faskes diuji bukti klinis otomatis."),
        
        ("4. Perencanaan Infrastruktur", 
         "Estimasi lokal 2 instance server kecil;\nBelum ada kalkulasi kebutuhan nasional.", 
         "Kalkulasi Beban Nasional (120 Juta klaim/thn);\nArsitektur 4-Node HA Cluster (128 vCPU/256GB).",
         "Kepastian operasional nasional BPJS:\nMampu layani 1.600 TPS (> 10x beban puncak)."),
        
        ("5. Kesiapan Repositori", 
         "Pengujian manual lewat dashboard.", 
         "Unit Test Suite lengkap (tests/*.py):\nAutomated QA upload, ensemble, & HITL.", 
         "Keandalan sistem terjamin secara continuous\nintegration (CI/CD ready).")
    ]
    
    curr_y = ty - th_h
    for idx, (p, b, a, imp) in enumerate(rows):
        row_h = 62
        bg = WHITE if idx % 2 == 0 else HexColor("#F8FAFC")
        draw_card(c, 48, curr_y - row_h, PAGE_WIDTH - 96, row_h, bg_color=bg, border_color=BORDER_LIGHT, radius=0)
        
        # Col 1: Parameter
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(TEXT_DARK)
        c.drawString(56, curr_y - 20, p)
        
        # Col 2: Before
        c.setFont("Helvetica", 7.5)
        c.setFillColor(ACCENT_RED)
        by = curr_y - 20
        for l in b.split("\n"):
            c.drawString(56 + col_w[0], by, l)
            by -= 13
            
        # Col 3: After
        c.setFont("Helvetica", 7.5)
        c.setFillColor(BPJS_GREEN_DARK)
        ay = curr_y - 20
        for l in a.split("\n"):
            c.drawString(56 + col_w[0] + col_w[1], ay, l)
            ay -= 13
            
        # Col 4: Impact
        c.setFont("Helvetica-Bold", 7.5)
        c.setFillColor(BPJS_BLUE)
        iy = curr_y - 20
        for l in imp.split("\n"):
            c.drawString(56 + col_w[0] + col_w[1] + col_w[2], iy, l)
            iy -= 13
            
        curr_y -= row_h


# =============================================================================
# SLIDE 5: RINGKASAN SOLUSI & ALUR PROSES (5-STAGE PIPELINE)
# =============================================================================
def draw_slide_5_process_flow(c):
    draw_header(c, "Ringkasan Solusi: Alur Proses VeriKlaim 5-Stage Pipeline", slide_num_label="3", current_slide=5)
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(48, PAGE_HEIGHT - 80, "Arsitektur Aliran Data End-to-End: Dari Ingestion Batch Faskes hingga Penerbitan Berita Acara Legal")
    
    col_w = (PAGE_WIDTH - 96 - 48) / 5.0
    col_h = 360
    col_y = 52
    
    stages = [
        ("STAGE 1", "Batch & Webhook Ingestion", BPJS_GREEN, [
            "Input Multi-Format:",
            "- Drag-and-drop CSV / Excel",
            "- JSON Payload Direct API",
            "- Webhook M2M SIMRS RS",
            "- VClaim / e-Klaim Mirror",
            "Sanitasi Otomatis:",
            "Validasi skema 21 variabel klaim",
            "dan deteksi duplikasi nomor SEP."
        ]),
        ("STAGE 2", "PDP Sanitization & Rules", BPJS_BLUE, [
            "Kepatuhan UU PDP:",
            "- Zero PII Storage di server",
            "- Pseudonymization NIK/Nama",
            "- Hashing SHA-256 satu arah",
            "Screening Regulasi:",
            "- Cek validitas rujukan 90 hari",
            "- Kesesuaian poli spesialis",
            "- Flag indikasi bypass IGD"
        ]),
        ("STAGE 3", "Dual Ensemble 60:40", HexColor("#7E22CE"), [
            "Model Pembobotan:",
            "- 60% XGBoost Classifier",
            "- 40% Random Forest Bagging",
            "6 Klaster Kemenkes:",
            "- Upcoding & CMG Ekstrem",
            "- Unbundling & Fragmen Tarif",
            "- Phantom Billing & LOS Drift",
            "- Referral Bypass & Readmisi",
            "Latensi Core: < 0.15 ms / klaim"
        ]),
        ("STAGE 4", "Explainable AI (XAI)", HexColor("#D97706"), [
            "TreeSHAP Attribution:",
            "Dekomposisi matematis",
            "fitur pemicu anomali individual",
            "Dual Mode Reasoning:",
            "- Online: LLM Gemini Clinical",
            "- Offline: Standalone TreeSHAP",
            "Kepatuhan Hukum:",
            "Terkorelasi langsung ke pasal",
            "Permenkes 26/2021 & 16/2019"
        ]),
        ("STAGE 5", "HITL & Legal Dossier", HexColor("#00875A"), [
            "Human-in-the-Loop:",
            "- Viewer 4 Berkas Medis",
            "- Text-Only Snippet Faskes",
            "- Evaluasi Semantik Objektif",
            "Actionable Output:",
            "- Putusan akhir di tangan dokter",
            "- Export Berita Acara PDF resmi",
            "- Audit trail tamper-proof"
        ])
    ]
    
    for i, (tag, title, col, bullets) in enumerate(stages):
        x = 48 + i * (col_w + 12)
        draw_card(c, x, col_y, col_w, col_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
        draw_card(c, x, col_y + col_h - 32, col_w, 32, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=8)
        
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(col)
        c.drawString(x + 10, col_y + col_h - 14, tag)
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(TEXT_DARK)
        c.drawString(x + 10, col_y + col_h - 26, title)
        
        c.setFont("Helvetica", 7.8)
        c.setFillColor(TEXT_DARK)
        by = col_y + col_h - 48
        for b in bullets:
            if b.startswith("-"):
                c.setFont("Helvetica", 7.5)
                c.setFillColor(TEXT_MUTED)
            elif b.endswith(":"):
                c.setFont("Helvetica-Bold", 7.8)
                c.setFillColor(col)
                by -= 4
            else:
                c.setFont("Helvetica", 7.5)
                c.setFillColor(TEXT_DARK)
            c.drawString(x + 10, by, b)
            by -= 13


# =============================================================================
# SLIDE 6: DEMO APLIKASI VERSI TERBARU (LIVE WORKSTATION)
# =============================================================================
def draw_slide_6_demo(c):
    draw_header(c, "Demo Aplikasi Versi Terbaru: Batch Upload & Live Workstation", slide_num_label="4", current_slide=6)
    
    left_w = 460
    draw_card(c, 48, 52, left_w, 413, bg_color=HexColor("#0F172A"), border_color=BORDER_LIGHT, radius=8)
    
    # Header Browser Mockup
    c.setFillColor(HexColor("#1E293B"))
    c.rect(48, 435, left_w, 30, fill=True, stroke=False)
    c.setFillColor(HexColor("#EF4444"))
    c.circle(64, 450, 4, fill=True, stroke=False)
    c.setFillColor(HexColor("#F59E0B"))
    c.circle(76, 450, 4, fill=True, stroke=False)
    c.setFillColor(HexColor("#10B981"))
    c.circle(88, 450, 4, fill=True, stroke=False)
    
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(WHITE)
    c.drawString(104, 446, "VeriKlaim - Cloud Production (https://veriklaim.absolute-tech.id)")
    
    # 3 Stat Cards
    draw_card(c, 60, 376, 134, 46, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica", 7)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(68, 408, "Data Riil Teruji")
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(WHITE)
    c.drawString(68, 388, "50.000 Klaim")
    
    draw_card(c, 202, 376, 134, 46, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica", 7)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(210, 408, "Akurasi Ensemble")
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(210, 388, "98.44% (Recall 100%)")
    
    draw_card(c, 344, 376, 150, 46, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica", 7)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(352, 408, "Bobot Model")
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(HexColor("#60A5FA"))
    c.drawString(352, 388, "60% XGB + 40% RF")

    # Fitur Baru 1: Batch Ingestion Modal
    draw_card(c, 60, 252, 434, 114, bg_color=HexColor("#1E293B"), border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_GREEN)
    c.drawString(72, 348, "[FITUR BARU] MODUL BATCH UPLOAD & INTEGRASI SIMRS")
    
    draw_card(c, 72, 288, 410, 50, bg_color=HexColor("#0F172A"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica-Bold", 7.8)
    c.setFillColor(WHITE)
    c.drawString(82, 322, "Drag-and-Drop Batch Claim Upload (CSV / Excel .xlsx / JSON)")
    c.setFont("Helvetica", 7.2)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(82, 306, "Mendukung audit paralel ribuan klaim faskes seketika. Dilengkapi tombol Unduh")
    c.drawString(82, 294, "Template CSV resmi dan webhook otomatis POST /api/claims/batch-audit.")
    
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(BPJS_BLUE_LIGHT)
    c.drawString(72, 270, "Status: Sukses memproses 10.000 batch klaim dalam waktu < 2.5 detik.")
    
    # Fitur Baru 2: Workstation & Text-Only HITL
    draw_card(c, 60, 94, 434, 150, bg_color=HexColor("#1E293B"), border_color=HexColor("#7E22CE"), radius=6)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(HexColor("#C084FC"))
    c.drawString(72, 226, "[FITUR BARU] WORKSTATION VERIFIKASI & KLARIFIKASI RS (ANTI-PDP)")
    
    c.setFont("Helvetica", 7.5)
    c.setFillColor(WHITE)
    c.drawString(72, 210, "Kasus SEP-2026-99214 | Upcoding Ekstrem O82.1 (Sesar Darurat Severity III)")
    c.drawString(72, 196, "Tagihan RS: Rp 36.500.000 vs Acuan INA-CBG: Rp 6.200.000 (Overclaim Rp 30,3 Jt)")
    
    draw_card(c, 72, 142, 410, 46, bg_color=HexColor("#0F172A"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica-Bold", 7.2)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(82, 172, "Kutipan CPPT/DPJP Faskes Terstruktur (Dilarang Upload PDF Mentah):")
    c.setFont("Helvetica", 7.0)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(82, 158, "DPJP Signature: DR-SPOG-8812 | RME Timestamp: 2026-10-24T14:12:00Z")
    c.drawString(82, 146, "Evaluasi Semantik: 'Gagal induksi + gawat janin' valid, namun LOS 1 hari tdk memenuhi Sev III.")
    
    # Buttons
    draw_card(c, 72, 102, 195, 18, bg_color=BPJS_GREEN, border_color=BPJS_GREEN, radius=3)
    c.setFont("Helvetica-Bold", 7.2)
    c.setFillColor(WHITE)
    c.drawCentredString(169, 107, "Sahkan Putusan Dokter Verifikator")
    
    draw_card(c, 275, 102, 207, 18, bg_color=BPJS_BLUE, border_color=BPJS_BLUE, radius=3)
    c.setFont("Helvetica-Bold", 7.2)
    c.setFillColor(WHITE)
    c.drawCentredString(378, 107, "Unduh Berita Acara Legal PDF")

    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawCentredString(48 + left_w / 2, 68, "Live Production Server: https://veriklaim.absolute-tech.id")

    # Right Column: Skenario Demo
    right_x = 48 + left_w + 16
    right_w = PAGE_WIDTH - 48 - right_x
    draw_card(c, right_x, 52, right_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(right_x + 18, 442, "S K E N A R I O   D E M O   ( 4   L A N G K A H )")
    
    steps = [
        ("1", "Batch Upload Faskes", [
            "Faskes mengunggah 1 file CSV/Excel",
            "berisi 500 klaim sekaligus;",
            "sistem menganalisis dalam < 1 detik."
        ], BPJS_GREEN),
        ("2", "Inspeksi Skor Ensemble 60:40", [
            "Klaim berisiko tinggi dipisahkan;",
            "terlihat kontribusi skor XGBoost (60%)",
            "dan Random Forest (40%)."
        ], BPJS_BLUE),
        ("3", "Klarifikasi RS & Semantik AI", [
            "Faskes kirim kutipan CPPT terstruktur",
            "ber-ID digital tanpa membocorkan PDP;",
            "AI validasi keabsahan bukti medis."
        ], HexColor("#7E22CE")),
        ("4", "Penerbitan Berita Acara PDF", [
            "Dokter verifikator menyetujui vonis;",
            "sistem otomatis terbitkan Berita Acara",
            "resmi ber-QR Code untuk dispute faskes."
        ], HexColor("#00875A"))
    ]
    
    sy = 412
    for num, stitle, slines, scol in steps:
        draw_card(c, right_x + 18, sy - 48, 26, 26, bg_color=HexColor("#F8FAFC"), border_color=scol, radius=13)
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(scol)
        c.drawCentredString(right_x + 31, sy - 34, num)
        
        c.setFont("Helvetica-Bold", 8.8)
        c.setFillColor(TEXT_DARK)
        c.drawString(right_x + 52, sy - 28, stitle)
        
        c.setFont("Helvetica", 7.6)
        c.setFillColor(TEXT_MUTED)
        ly = sy - 42
        for sl in slines:
            c.drawString(right_x + 52, ly, sl)
            ly -= 11.5
        sy -= 66
        
    draw_card(c, right_x + 18, 64, right_w - 36, 68, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(right_x + 28, 116, "TAUTAN SISTEM LIVE PRODUCTION")
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 28, 98, "https://veriklaim.absolute-tech.id")
    c.setFont("Helvetica", 7.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 80, "Unduh Buku Panduan: /api/download-feature-guide")


# =============================================================================
# SLIDE 7: PENJELASAN 4 FITUR UTAMA
# =============================================================================
def draw_slide_7_features(c):
    draw_header(c, "Penjelasan 4 Fitur Utama Solusi VeriKlaim", slide_num_label="5", current_slide=7)
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(48, PAGE_HEIGHT - 80, "Kapabilitas Unggulan yang Dirancang Khusus Menjawab Kebutuhan Operasional Verifikator BPJS Kesehatan")
    
    grid_w = (PAGE_WIDTH - 96 - 16) / 2.0
    grid_h = 175
    
    features = [
        (48, PAGE_HEIGHT - 268, "FITUR 1: BATCH INGESTION & WEBHOOK SIMRS", BPJS_GREEN, [
            "Pintu Masuk Terpadu Data Klaim Rumah Sakit Multi-Format:",
            "- Drag-and-drop batch upload mendukung CSV, Excel (.xlsx), dan JSON.",
            "- Endpoint Webhook SIMRS (POST /api/claims/batch-audit) memfasilitasi integrasi",
            "  langsung Machine-to-Machine tanpa hambatan manual.",
            "- Skema validasi cerdas 21 atribut klaim memastikan kepatuhan format VClaim.",
            "- Nilai Tambah: Memungkinkan audit mandiri oleh internal RS sebelum diajukan."
        ]),
        (48 + grid_w + 16, PAGE_HEIGHT - 268, "FITUR 2: ENSEMBLE SCORING 6-KLASTER KEMENKES", BPJS_BLUE, [
            "Deteksi Presisi Tinggi Berbasis Dual-Model Calibrated Ensemble:",
            "- Kombinasi teruji 60% XGBoost Classifier + 40% Random Forest Bagging.",
            "- Mendeteksi 6 Modus Blueprint Kemenkes: Upcoding Ekstrem, Fragmentasi Unbundling,",
            "  Klaim Fiktif (Phantom Billing), LOS Drift, Referral Bypass, dan Mismatch Faskes.",
            "- Akurasi terbukti 98.44%, Recall 100% pada aturan baku, latensi < 0.15 ms.",
            "- Menghilangkan blind-spot deteksi berbasis aturan konvensional."
        ]),
        (48, 52, "FITUR 3: TEXT-ONLY HITL PROTOCOL (ANTI-PDP)", HexColor("#7E22CE"), [
            "Portal Sengketa Faskes yang Aman Sesuai Regulasi Privasi:",
            "- Menghilangkan risiko kebocoran data dengan larangan upload berkas PDF utuh.",
            "- Faskes menginput cuplikan CPPT terstruktur dengan Tanda Tangan Digital DPJP.",
            "- Evaluasi Semantik AI membedakan pembuktian klinis riil vs alasan nihil/klise.",
            "- Menjaga asas Human-in-the-Loop: Vonis akhir mutlak di tangan dokter BPJS."
        ]),
        (48 + grid_w + 16, 52, "FITUR 4: AUTOMATED LEGAL DOSSIER & AUDIT TRAIL", HexColor("#00875A"), [
            "Penerbitan Dokumen Pembuktian Resmi Sekali Klik:",
            "- Otomatisasi penerbitan Berita Acara Audit Formal berformat PDF standar BPJS.",
            "- Dilengkapi QR Code verifikasi integritas berkas dan rincian pasal Permenkes.",
            "- Mencatat setiap riwayat persetujuan dokter ke dalam Audit Trail permanen.",
            "- Memangkas siklus sengketa klaim pending dari 14 hari menjadi 1-2 hari tuntas."
        ])
    ]
    
    for x, y, title, col, lines in features:
        draw_card(c, x, y, grid_w, grid_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=6)
        draw_card(c, x, y + grid_h - 26, grid_w, 26, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=6)
        c.setFont("Helvetica-Bold", 8.8)
        c.setFillColor(col)
        c.drawString(x + 12, y + grid_h - 18, title)
        
        c.setFont("Helvetica", 7.6)
        c.setFillColor(TEXT_DARK)
        ly = y + grid_h - 44
        for l in lines:
            if l.endswith(":"):
                c.setFont("Helvetica-Bold", 7.6)
                c.setFillColor(col)
                ly -= 3
            else:
                c.setFont("Helvetica", 7.5)
                c.setFillColor(TEXT_DARK)
            c.drawString(x + 12, ly, l)
            ly -= 13


# =============================================================================
# SLIDE 8: ARSITEKTUR TEKNIS & DUAL MODEL SCORING
# =============================================================================
def draw_slide_8_architecture(c):
    draw_header(c, "Arsitektur Teknis: Pipeline Dual-Model Ensemble 60:40", slide_num_label="6", current_slide=8)
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(48, PAGE_HEIGHT - 80, "Arsitektur Komputasi Berperforma Tinggi dengan Prinsip Zero False Negative & Sub-Millisecond Execution")
    
    col3_w = (PAGE_WIDTH - 96 - 32) / 3.0
    card_h = 360
    card_y = 52
    
    # Col 1: Model Selection
    draw_card(c, 48, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, 48, card_y + card_h - 28, col3_w, 28, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(60, card_y + card_h - 18, "DUAL ENSEMBLE 60:40")
    
    c.setFont("Helvetica", 7.6)
    c.setFillColor(TEXT_DARK)
    c1_lines = [
        "Formula Kalibrasi Skor Komposit:",
        "Skor = 0.60 * P(XGBoost) + 0.40 * P(RandomForest)",
        "",
        "XGBoost Classifier (Bobot 60%):",
        "- Menangkap deviasi non-linear rasio biaya",
        "- Mendeteksi anomali multi-atribut kompleks",
        "- Sangat sensitif terhadap Upcoding ekstrem",
        "",
        "Random Forest Bagging (Bobot 40%):",
        "- Mereduksi variansi outlier data faskes",
        "- Menjaga stabilitas model agar tidak overfit",
        "- Mempertahankan batas keputusan yang ajek",
        "",
        "Keunggulan Kombinasi:",
        "Sinergi boosting & bagging meningkatkan",
        "akurasi menjadi 98.44% & ROC-AUC 0.998."
    ]
    ly = card_y + card_h - 46
    for l in c1_lines:
        if l.endswith(":") or "Formula" in l:
            c.setFont("Helvetica-Bold", 7.6)
            c.setFillColor(BPJS_GREEN_DARK)
        else:
            c.setFont("Helvetica", 7.4)
            c.setFillColor(TEXT_DARK)
        c.drawString(60, ly, l)
        ly -= 12.5

    # Col 2: Pipeline Integration
    x2 = 48 + col3_w + 16
    draw_card(c, x2, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, x2, card_y + card_h - 28, col3_w, 28, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_BLUE)
    c.drawString(x2 + 12, card_y + card_h - 18, "PIPELINE INTEGRASI SISTEM")
    
    c2_lines = [
        "1. REST API FastAPI Asynchronous:",
        "   Melayani ratusan request per detik dengan",
        "   overhead threading sangat rendah.",
        "",
        "2. Cythonized Decision Tree Core:",
        "   Inference komputasi in-memory tensor",
        "   hanya membutuhkan < 0.15 ms / klaim.",
        "",
        "3. Dual Explainer Engine:",
        "   - Mode Online: LLM Gemini Clinical Reasoning",
        "   - Mode Offline: Local TreeSHAP Explainer",
        "",
        "4. Modular & Portable:",
        "   Container Docker ready, zero vendor lock-in,",
        "   siap pasang on-premise di Data Center BPJS."
    ]
    ly = card_y + card_h - 46
    for l in c2_lines:
        if l.endswith(":") or l.startswith("1.") or l.startswith("2.") or l.startswith("3.") or l.startswith("4."):
            c.setFont("Helvetica-Bold", 7.6)
            c.setFillColor(BPJS_BLUE)
        else:
            c.setFont("Helvetica", 7.4)
            c.setFillColor(TEXT_DARK)
        c.drawString(x2 + 12, ly, l)
        ly -= 12.5

    # Col 3: Benchmark Performa
    x3 = x2 + col3_w + 16
    draw_card(c, x3, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, x3, card_y + card_h - 28, col3_w, 28, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawString(x3 + 12, card_y + card_h - 18, "BENCHMARK PERFORMA TEKNIS")
    
    c3_lines = [
        "- Spesifikasi Lingkungan Pengujian:",
        "  10 Core, 20 Thread, RAM 32 GB.",
        "- Kebutuhan Minimal Sistem Lapangan:",
        "  6 Core, 12 Thread, RAM 16 GB.",
        "- Latensi Eksekusi Core: < 0.15 ms / klaim.",
        "- Latensi End-to-End API: ~2.4 ms.",
        "- Throughput Audit: > 400 req/dtk (> 1,4 jt/jam).",
        "- Akurasi Ensemble: 98.44%.",
        "- Sensitivitas / Recall: 100% (Zero False Neg).",
        "- Presisi Deteksi: 96.4% (Minim False Alarm).",
        "- ROC-AUC Score: 0.998 - 1.000.",
        "- Resource Footprint: Sangat Ringan (< 500 MB)."
    ]
    ly = card_y + card_h - 46
    for l in c3_lines:
        if "Spesifikasi" in l or "Akurasi" in l or "Recall" in l:
            c.setFont("Helvetica-Bold", 7.6)
            c.setFillColor(HexColor("#7E22CE"))
        else:
            c.setFont("Helvetica", 7.4)
            c.setFillColor(TEXT_DARK)
        c.drawString(x3 + 12, ly, l)
        ly -= 13


# =============================================================================
# SLIDE 9: KEAMANAN, PRIVASI UU PDP & PROTOKOL RESUME MEDIS
# =============================================================================
def draw_slide_9_governance(c):
    draw_header(c, "Keamanan Data: Kepatuhan UU PDP & Protokol Resume Medis", slide_num_label="7", current_slide=9)
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(48, PAGE_HEIGHT - 80, "Penerapan Tata Kelola Privasi Pasien Berbasis Zero PII Storage dan Text-Only Snippet Faskes")
    
    col3_w = (PAGE_WIDTH - 96 - 32) / 3.0
    card_h = 360
    card_y = 52
    
    # Col 1: UU PDP
    draw_card(c, 48, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, 48, card_y + card_h - 28, col3_w, 28, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(60, card_y + card_h - 18, "KEPATUHAN UU PDP NO. 27/2022")
    
    p1 = [
        "1. Zero PII Storage Architecture:",
        "   Data identitas personal (NIK, Nama, Alamat)",
        "   tidak pernah disimpan permanen di database.",
        "",
        "2. Pseudonymization Hashing:",
        "   Atribut pasien di-masking dengan algoritma",
        "   kriptografi SHA-256 satu arah.",
        "",
        "3. On-Premise Sovereignity:",
        "   Seluruh pemrosesan berlangsung di dalam",
        "   jaringan intranet tertutup BPJS Kesehatan",
        "   tanpa transmisi ke cloud pihak ketiga asing.",
        "",
        "4. Enkripsi At-Rest & In-Transit:",
        "   Komunikasi internal diamankan TLS 1.3 dan",
        "   database terenkripsi AES-256."
    ]
    ly = card_y + card_h - 46
    for l in p1:
        c.drawString(60, ly, l)
        ly -= 13
        
    # Col 2: Text-Only HITL Protocol
    x2 = 48 + col3_w + 16
    draw_card(c, x2, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, x2, card_y + card_h - 28, col3_w, 28, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(BPJS_BLUE)
    c.drawString(x2 + 12, card_y + card_h - 18, "PROTOKOL RESUME MEDIS RS")
    
    p2 = [
        "Solusi atas Masukan Mentor No. 3:",
        "Mekanisme Pemberian Data Rekam Medis:",
        "",
        "1. DILARANG Upload PDF Resume Mentah:",
        "   Menghilangkan risiko kebocoran data sensitif",
        "   riwayat rekam medis utuh keluarga pasien.",
        "",
        "2. Text-Only Structured Snippet Protocol:",
        "   RS cukup mengirimkan kutipan objektif:",
        "   - Stempel Waktu RME RS (ISO 8601)",
        "   - Digital Signature ID Dokter Spesialis",
        "   - Parameter Vital & Hasil Lab Kritis",
        "",
        "3. Kepatuhan Permenkes No. 24/2022:",
        "   Menjamin interoperabilitas RME resmi."
    ]
    ly = card_y + card_h - 46
    for l in p2:
        c.drawString(x2 + 12, ly, l)
        ly -= 13

    # Col 3: Evaluasi Semantik & Audit Trail
    x3 = x2 + col3_w + 16
    draw_card(c, x3, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, x3, card_y + card_h - 28, col3_w, 28, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawString(x3 + 12, card_y + card_h - 18, "EVALUASI SEMANTIK & AUDIT")
    
    p3 = [
        "1. Filter Bukti Objektif vs Klise:",
        "   NLP Engine menganalisis teks sanggahan RS.",
        "   Jika hanya memuat dalih umum tanpa data",
        "   vital/lab terukur, vonis tetap REJECTED.",
        "",
        "2. Tamper-Proof Audit Trail Log:",
        "   Setiap siklus verifikasi (waktu, nama dokter,",
        "   alasan verifikasi, skor) direkam dalam log",
        "   persisten data/hitl_audit_trail.json.",
        "",
        "3. Kepatuhan Pemeriksaan Eksternal:",
        "   Siap diaudit sewaktu-waktu oleh BPK RI,",
        "   BPKP, maupun Inspektorat Kemenkes."
    ]
    ly = card_y + card_h - 46
    for l in p3:
        c.drawString(x3 + 12, ly, l)
        ly -= 13


# =============================================================================
# SLIDE 10: HASIL UJI VALIDASI TERUKUR
# =============================================================================
def draw_slide_10_validation(c):
    draw_header(c, "Hasil Uji Validasi Terukur: 50.000 Riil & 10.000 Skenario", slide_num_label="8", current_slide=10)
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(48, PAGE_HEIGHT - 80, "Pemisahan Tegas dan Obyektif antara Baseline Data Riil BPJS Kesehatan vs Uji Stres Skenario Ekstrem")
    
    grid_w = (PAGE_WIDTH - 96 - 16) / 2.0
    grid_h = 360
    
    # Left Card: Baseline Riil 50.000
    draw_card(c, 48, 52, grid_w, grid_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, 48, 52 + grid_h - 30, grid_w, 30, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=8)
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(60, 52 + grid_h - 20, "UJI BASELINE: 50.000 DATA RIIL SAMPEL BPJS FKRTL")
    
    l_points = [
        ("Karakteristik Data:", "Data riil pelayanan sekunder BPJS Kesehatan (pre-cleaned & verified)."),
        ("Tingkat Anomali Alami:", "0.27% (135 klaim terindikasi deviasi tarif/koding)."),
        ("Klaim Terpotong Riil:", "64 klaim diverifikasi terbukti overclaim (Total Rp 61.240.000)."),
        ("Akurasi Model:", "98.44% pada evaluasi 5-fold cross-validation."),
        ("Recall / Sensitivitas:", "100% pada batasan aturan batas tarif baku Kemenkes RI."),
        ("Presisi Deteksi:", "96.4% (Meminimalkan alarm palsu bagi RS yang tertib)."),
        ("Kesimpulan Ilmiah:", "Menunjukkan performa realistis di kondisi operasional normal faskes.")
    ]
    ly = 52 + grid_h - 52
    for title, desc in l_points:
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(BPJS_GREEN_DARK)
        c.drawString(60, ly, title)
        c.setFont("Helvetica", 7.6)
        c.setFillColor(TEXT_DARK)
        c.drawString(60, ly - 12, desc)
        ly -= 30

    # Right Card: Uji Stres Skenario 10.000
    rx = 48 + grid_w + 16
    draw_card(c, rx, 52, grid_w, grid_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, rx, 52 + grid_h - 30, grid_w, 30, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=8)
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(rx + 12, 52 + grid_h - 20, "UJI STRES: 10.000 DATA SKENARIO MULTI-MODUS")
    
    r_points = [
        ("Tujuan Pengujian:", "Menguji ketahanan sistem pada serangan fraud multi-klaster serentak."),
        ("Injeksi Modus Fraud:", "4.412 klaim anomali disuntikkan secara terstruktur (44.1% rasio uji)."),
        ("Distribusi Modus:", "Upcoding Ekstrem (2.410), Unbundling (1.202), Phantom Billing (800)."),
        ("Potensi Penghematan:", "Rp 14,34 Miliar berhasil diselamatkan dari klaim anomali skenario."),
        ("Efisiensi Waktu Review:", "Review dokter dipangkas dari 15-20 menit menjadi 1-2 menit/klaim."),
        ("Throughput Batch:", "10.000 data skenario diaudit tuntas dalam < 2.5 detik."),
        ("Kesimpulan Ilmiah:", "Membuktikan ketangguhan sistem saat faskes mengalami fraud sistematik.")
    ]
    ry = 52 + grid_h - 52
    for title, desc in r_points:
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(BPJS_BLUE)
        c.drawString(rx + 12, ry, title)
        c.setFont("Helvetica", 7.6)
        c.setFillColor(TEXT_DARK)
        c.drawString(rx + 12, ry - 12, desc)
        ry -= 30


# =============================================================================
# SLIDE 11: KALKULASI KEBUTUHAN INFRASTRUKTUR NASIONAL
# =============================================================================
def draw_slide_11_infrastructure(c):
    draw_header(c, "Kalkulasi Kebutuhan Infrastruktur Implementasi Nasional BPJS", slide_num_label="9", current_slide=11)
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(48, PAGE_HEIGHT - 80, "Jawaban Konkret atas Masukan Mentor No. 4: Proyeksi Beban 120 Juta Klaim/Tahun & Arsitektur Klaster Produksi")
    
    col3_w = (PAGE_WIDTH - 96 - 32) / 3.0
    card_h = 360
    card_y = 52
    
    # Box 1: Beban Nasional
    draw_card(c, 48, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, 48, card_y + card_h - 28, col3_w, 28, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(60, card_y + card_h - 18, "PROFIL BEBAN KLAIM NASIONAL")
    
    b1 = [
        "- Volume Klaim FKRTL se-Indonesia:",
        "  ~100 s.d. 120 Juta klaim per tahun",
        "  (Rata-rata 350.000 klaim per hari kerja).",
        "",
        "- Beban Jam Sibuk (Peak Traffic):",
        "  70% klaim disubmit pada 6 jam kerja",
        "  (08.00 - 14.00 WIB) = 280.000 klaim.",
        "  Peak Throughput: ~13 s.d. 150 TPS",
        "  (Transaksi Per Detik).",
        "",
        "- Kinerja VeriKlaim Saat Ini:",
        "  Latensi core: < 0.15 ms / klaim.",
        "  Throughput single worker: > 400 TPS.",
        "  Kapasitas 1 worker: > 1,44 Juta klaim/jam."
    ]
    ly = card_y + card_h - 46
    for l in b1:
        c.drawString(60, ly, l)
        ly -= 13

    # Box 2: Spesifikasi Klaster HA
    x2 = 48 + col3_w + 16
    draw_card(c, x2, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, x2, card_y + card_h - 28, col3_w, 28, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(BPJS_BLUE)
    c.drawString(x2 + 12, card_y + card_h - 18, "SPESIFIKASI KLASTER HA NASIONAL")
    
    b2 = [
        "Arsitektur On-Premise Cloud BPJS:",
        "",
        "1. API Gateway / Load Balancer (2 Node HA):",
        "   - 2 Node Active-Passive NGINX/HAProxy",
        "   - @ 8 vCPU, 16 GB RAM, SSL Offloading",
        "",
        "2. Compute Workers (4 Node Active-Active):",
        "   - 4 Server @ 16 vCPU, 32 GB RAM, NVMe",
        "   - Total Kapasitas: 1.600 TPS",
        "   - > 10x lipat di atas beban peak BPJS!",
        "",
        "3. Database & Audit Storage (2 Node Cluster):",
        "   - PostgreSQL Primary-Standby Replication",
        "   - @ 16 vCPU, 64 GB RAM, 2 TB SSD NVMe",
        "   - Redis Cache @ 8 vCPU, 32 GB RAM"
    ]
    ly = card_y + card_h - 46
    for l in b2:
        c.drawString(x2 + 12, ly, l)
        ly -= 13

    # Box 3: Total Resource & Biaya
    x3 = x2 + col3_w + 16
    draw_card(c, x3, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, x3, card_y + card_h - 28, col3_w, 28, bg_color=HexColor("#F8FAFC"), border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawString(x3 + 12, card_y + card_h - 18, "EFISIENSI KOMPUTASI & BIAYA")
    
    b3 = [
        "Total Kebutuhan Sumber Daya Nasional:",
        "- Total Komputasi: 128 vCPU & 256 GB RAM.",
        "- Footprint Memori: Sangat Ringan",
        "  (< 500 MB RAM per proses worker).",
        "",
        "Analisis Nilai Investasi (ROI):",
        "- Efisiensi Biaya Server: Menghemat hingga",
        "  70% dibanding solusi vendor AI proprietary.",
        "- Siap pasang di Data Center internal BPJS",
        "  tanpa memerlukan superkomputer GPU mahal.",
        "- Rasio Penghematan: Potensi penyelamatan",
        "  dana klaim JKN ratusan miliar rupiah per tahun",
        "  dengan investasi server yang sangat minimal."
    ]
    ly = card_y + card_h - 46
    for l in b3:
        c.drawString(x3 + 12, ly, l)
        ly -= 13


# =============================================================================
# SLIDE 12: PENUTUP & TAUTAN PROTOTYPE
# =============================================================================
def draw_slide_12_closing(c):
    c.setFillColor(NAVY_DARK)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    c.setFillColor(BPJS_GREEN)
    c.rect(0, PAGE_HEIGHT - 8, PAGE_WIDTH, 8, fill=True, stroke=False)
    
    logo_path = os.path.join(ASSETS_DIR, "template_p1_img1_Image6.png")
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 48, PAGE_HEIGHT - 82, width=160, height=52, preserveAspectRatio=True, mask='auto')
        
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(WHITE)
    c.drawString(48, PAGE_HEIGHT - 124, "Terima Kasih")
    
    c.setFont("Helvetica", 11.5)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 148, "Detect Smarter, Protect JKN - Smarter Protection for a Stronger JKN")
    
    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 168, "VeriKlaim: Solusi Deteksi Anomali Klaim FKRTL Berbasis AI & Explainable Governance | Tim Aqila Digital")
    
    card_w = (PAGE_WIDTH - 96 - 32) / 3.0
    card_h = 240
    card_y = 65
    
    # Card 1: Live Demo
    x1 = 48
    draw_card(c, x1, card_y, card_w, card_h, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN)
    c.drawString(x1 + 18, card_y + card_h - 26, "TAUTAN PROTOTYPE LIVE")
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(WHITE)
    c.drawString(x1 + 18, card_y + card_h - 54, "Demo Live Sistem")
    
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(x1 + 18, card_y + card_h - 80, "https://veriklaim.absolute-tech.id")
    
    demo_notes = [
        "- Cloud Production Active (HTTPS)",
        "- Fitur Batch Upload CSV/Excel/JSON",
        "- Webhook Integrasi SIMRS Faskes",
        "- Workstation Dokter Human-in-the-Loop",
        "- Ensemble Scoring 60% XGB + 40% RF",
        "- Unduh Berita Acara & Panduan PDF"
    ]
    dy = card_y + card_h - 105
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_LIGHT)
    for dn in demo_notes:
        c.drawString(x1 + 18, dy, dn)
        dy -= 14
        
    # Card 2: GitHub Repo
    x2 = x1 + card_w + 16
    draw_card(c, x2, card_y, card_w, card_h, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_BLUE)
    c.drawString(x2 + 18, card_y + card_h - 26, "TAUTAN REPOSITORI GITHUB")
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(WHITE)
    c.drawString(x2 + 18, card_y + card_h - 54, "Source Code Lengkap")
    
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_BLUE_LIGHT)
    c.drawString(x2 + 18, card_y + card_h - 80, "https://github.com/orochimadit/veri-klaim")
    
    repo_notes = [
        "- Arsitektur Modular (app/, src/, docs/)",
        "- Rangkaian Automated Tests (tests/*.py)",
        "- Ensemble Model (models/*.joblib)",
        "- Dataset 50.000 Riil & QA 10.000",
        "- Buku Panduan Fitur Platform (PDF)",
        "- Lisensi Open Research & MIT"
    ]
    ry = card_y + card_h - 105
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_LIGHT)
    for rn in repo_notes:
        c.drawString(x2 + 18, ry, rn)
        ry -= 14

    # Card 3: Kontak Tim
    x3 = x2 + card_w + 16
    draw_card(c, x3, card_y, card_w, card_h, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(HexColor("#C084FC"))
    c.drawString(x3 + 18, card_y + card_h - 26, "KONTAK TIM AQILA DIGITAL")
    
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(WHITE)
    c.drawString(x3 + 18, card_y + card_h - 54, "Aditya Pratama, S.T., M.T.")
    
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(x3 + 18, card_y + card_h - 80, "Ketua Tim Aqila Digital")
    
    contact_notes = [
        "- Dosen Prodi Sistem Informasi, UNU Kalbar",
        "- Alumni S1 & S2 STEI ITB",
        "- WhatsApp: 0856-5441-1081",
        "- Email: aditya.pratama@unukalbar.ac.id",
        "- Pontianak, Kalimantan Barat"
    ]
    cy = card_y + card_h - 105
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_LIGHT)
    for cn in contact_notes:
        c.drawString(x3 + 18, cy, cn)
        cy -= 14

    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#64748B"))
    c.drawString(48, 30, "Healthkathon BPJS Kesehatan 2026 - Tahap 20 Besar Menuju Final Offline")


def generate_deck(output_pdf):
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)
    c = canvas.Canvas(output_pdf, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    
    draw_slide_1_cover(c)
    c.showPage()
    
    draw_slide_2_team(c)
    c.showPage()
    
    draw_slide_3_coaching_feedback(c)
    c.showPage()
    
    draw_slide_4_before_after(c)
    c.showPage()
    
    draw_slide_5_process_flow(c)
    c.showPage()
    
    draw_slide_6_demo(c)
    c.showPage()
    
    draw_slide_7_features(c)
    c.showPage()
    
    draw_slide_8_architecture(c)
    c.showPage()
    
    draw_slide_9_governance(c)
    c.showPage()
    
    draw_slide_10_validation(c)
    c.showPage()
    
    draw_slide_11_infrastructure(c)
    c.showPage()
    
    draw_slide_12_closing(c)
    c.showPage()
    
    c.save()
    sz_mb = os.path.getsize(output_pdf) / (1024 * 1024)
    print(f"SUCCESS: Generated {output_pdf} (12 slides, {sz_mb:.2f} MB)")


def main():
    target_1 = os.path.join(BASE_DIR, "docs", "Aqila Digital.pdf")
    target_2 = os.path.join(BASE_DIR, "docs", "Project_Final_Healthkathon_2026_VeriKlaim.pdf")
    
    generate_deck(target_1)
    generate_deck(target_2)


if __name__ == "__main__":
    main()
