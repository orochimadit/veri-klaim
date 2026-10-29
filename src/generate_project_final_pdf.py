"""
Generator Script: Project Final Slide Deck Healthkathon 2026
Format: 16:9 Landscape PDF (960 x 540 pt) strictly matching the official BPJS Healthkathon 2026 template.
Output: docs/Project_Final_Healthkathon_2026_VeriKlaim.pdf
"""

import os
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

# Palette BPJS & Professional Modern Slide Theme
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


def draw_header(c, title_text, slide_num_label="", current_slide=1, total_slides=11):
    """Draws standardized template header and footer."""
    # Top banner bar
    c.setFillColor(BPJS_GREEN)
    c.rect(0, PAGE_HEIGHT - 6, PAGE_WIDTH, 6, fill=True, stroke=False)
    
    # Subtitle / context string
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(48, PAGE_HEIGHT - 28, "Project Final  Healthkathon 2026")
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(200, PAGE_HEIGHT - 28, "|  Detect Smarter, Protect JKN - Smarter Protection for a Stronger JKN")
    
    # Slide main title
    c.setFont("Helvetica-Bold", 19)
    c.setFillColor(TEXT_DARK)
    c.drawString(48, PAGE_HEIGHT - 54, title_text)
    
    # Slide indicator in the top right (matching template number badge)
    if slide_num_label:
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(BPJS_GREEN)
        c.drawRightString(PAGE_WIDTH - 48, PAGE_HEIGHT - 54, str(slide_num_label))
    
    # Subtle separator line
    c.setStrokeColor(BORDER_LIGHT)
    c.setLineWidth(1)
    c.line(48, PAGE_HEIGHT - 64, PAGE_WIDTH - 48, PAGE_HEIGHT - 64)
    
    # Footer
    c.setStrokeColor(BORDER_LIGHT)
    c.line(48, 28, PAGE_WIDTH - 48, 28)
    
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(BPJS_GREEN)
    c.drawString(48, 16, "VeriKlaim")
    
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_MUTED)
    c.drawString(100, 16, "- Solusi Efisiensi Risiko Klaim FKRTL Berbasis AI | Tim VeriKlaim Kalbar")
    
    page_str = f"Slide {current_slide} dari {total_slides}"
    c.drawRightString(PAGE_WIDTH - 48, 16, page_str)


def draw_card(c, x, y, w, h, bg_color=BG_CARD, border_color=BORDER_LIGHT, radius=6):
    """Draws a rounded card box."""
    c.setFillColor(bg_color)
    c.setStrokeColor(border_color)
    c.setLineWidth(1)
    c.roundRect(x, y, w, h, radius, fill=True, stroke=True)


def draw_slide_1_cover(c):
    """Slide 1: Cover strictly according to Page 1 of template."""
    # Deep professional background with subtle gradient effect
    c.setFillColor(NAVY_DARK)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    
    # Top BPJS Green accent line
    c.setFillColor(BPJS_GREEN)
    c.rect(0, PAGE_HEIGHT - 8, PAGE_WIDTH, 8, fill=True, stroke=False)
    
    # Logo / Badge
    logo_path = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\docs\assets\template_p1_img1_Image6.png"
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 48, PAGE_HEIGHT - 85, width=170, height=58, preserveAspectRatio=True, mask='auto')
    else:
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(BPJS_GREEN)
        c.drawString(48, PAGE_HEIGHT - 60, "BPJS KESEHATAN")
    
    # Header titles
    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(WHITE)
    c.drawString(48, PAGE_HEIGHT - 125, "PROJECT FINAL")
    
    c.setFont("Helvetica-Bold", 17)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 150, "Healthkathon 2026")
    
    c.setFont("Helvetica", 11)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 170, "Detect Smarter, Protect JKN - Smarter Protection for a Stronger JKN: Efisiensi Risiko Program JKN")
    
    # Card 1: NAMA SOLUSI
    draw_card(c, 48, PAGE_HEIGHT - 275, PAGE_WIDTH - 96, 85, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(BPJS_GREEN)
    c.drawString(68, PAGE_HEIGHT - 210, "N A M A   S O L U S I")
    
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(WHITE)
    c.drawString(68, PAGE_HEIGHT - 236, "VeriKlaim")
    
    c.setFont("Helvetica", 10.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(68, PAGE_HEIGHT - 258, "Platform Deteksi Anomali Klaim FKRTL Berbasis Hybrid Machine Learning & Explainable AI (Permenkes 26/2021)")
    
    # 3 Columns below: NAMA TIM | ID TIM | KATEGORI
    col_w = (PAGE_WIDTH - 96 - 32) / 3.0
    
    # Column 1: NAMA TIM
    x1 = 48
    draw_card(c, x1, 75, col_w, 140, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN)
    c.drawString(x1 + 18, 192, "N A M A   T I M")
    c.setFont("Helvetica-Bold", 15)
    c.setFillColor(WHITE)
    c.drawString(x1 + 18, 168, "Tim VeriKlaim Kalbar")
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(x1 + 18, 144, "Universitas Nahdlatul Ulama Kalbar")
    c.drawString(x1 + 18, 128, "& Universitas Tanjungpura")
    c.drawString(x1 + 18, 104, "Kolaborasi AI, Data & Klinis")
    
    # Column 2: ID TIM
    x2 = x1 + col_w + 16
    draw_card(c, x2, 75, col_w, 140, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN)
    c.drawString(x2 + 18, 192, "I D   T I M")
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(WHITE)
    c.drawString(x2 + 18, 168, "C03.04-082")
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(x2 + 18, 144, "Status: Lolos Tahap Proposal")
    c.drawString(x2 + 18, 128, "Jalur: Mahasiswa & Akademisi")
    c.drawString(x2 + 18, 104, "Healthkathon BPJS 2026")
    
    # Column 3: KATEGORI
    x3 = x2 + col_w + 16
    draw_card(c, x3, 75, col_w, 140, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN)
    c.drawString(x3 + 18, 192, "K A T E G O R I")
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(WHITE)
    c.drawString(x3 + 18, 168, "Efisiensi Risiko Program JKN")
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(x3 + 18, 144, "Sub-Kategori: Efisiensi Faskes / KLAIM")
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(x3 + 18, 124, "Fokus: Upcoding, Unbundling,")
    c.drawString(x3 + 18, 108, "& Phantom Billing Klaim INA-CBG")
    
    # Bottom footnote
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#64748B"))
    c.drawString(48, 38, "Sesuai Panduan Project Final Healthkathon 2026 - Template Resmi Presentasi Final")


def draw_slide_2_team(c):
    """Slide 2: Perkenalan Tim strictly according to Page 4 of template."""
    draw_header(c, "Perkenalan Tim", slide_num_label="1", current_slide=2, total_slides=11)
    
    # Sub-bar info
    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT_MUTED)
    c.drawString(48, PAGE_HEIGHT - 82, "Nama tim: ")
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(TEXT_DARK)
    c.drawString(104, PAGE_HEIGHT - 82, "Tim VeriKlaim Kalbar")
    
    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT_MUTED)
    c.drawString(240, PAGE_HEIGHT - 82, "|   Kategori: ")
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(BPJS_GREEN)
    c.drawString(305, PAGE_HEIGHT - 82, "Efisiensi Risiko pada Faskes / KLAIM (C03.04)")
    
    # 3 Member Cards
    card_w = (PAGE_WIDTH - 96 - 32) / 3.0
    card_h = 360
    card_y = 52
    
    # Member 1: Aditya Pratama
    x1 = 48
    draw_card(c, x1, card_y, card_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    # Avatar badge
    draw_card(c, x1 + (card_w - 70) / 2, card_y + card_h - 85, 70, 70, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=35)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawCentredString(x1 + card_w / 2, card_y + card_h - 48, "AP")
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(BPJS_GREEN)
    c.drawCentredString(x1 + card_w / 2, card_y + card_h - 75, "ANGGOTA 1")
    
    c.setFont("Helvetica-Bold", 12.5)
    c.setFillColor(TEXT_DARK)
    c.drawCentredString(x1 + card_w / 2, card_y + card_h - 105, "Aditya Pratama, S.T., M.T.")
    
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x1 + card_w / 2, card_y + card_h - 122, "Ketua Tim / Lead AI & Arsitektur")
    
    # Divider line
    c.setStrokeColor(BORDER_LIGHT)
    c.line(x1 + 16, card_y + card_h - 134, x1 + card_w - 16, card_y + card_h - 134)
    
    # Details
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(x1 + 16, card_y + card_h - 152, "AFILIASI & REKAM JEJAK:")
    
    c.setFont("Helvetica", 8.5)
    c.setFillColor(TEXT_DARK)
    lines_m1 = [
        "- Dosen Tetap Prodi Sistem Informasi,",
        "  Universitas Nahdlatul Ulama Kalbar",
        "- Alumni S1 & S2 STEI ITB",
        "  (Institut Teknologi Bandung)",
        "- Pengalaman: Riset AI/ML, Pipeline Deteksi",
        "  Anomali Klaim Kesehatan, High-Throughput",
        "  API Engine & Sistem Terdistribusi",
        "- Lead implementasi ensemble tree model",
        "  dan Explainable AI (SHAP)",
        "- Kontak WA: 0856-5441-1081"
    ]
    cur_y = card_y + card_h - 170
    for line in lines_m1:
        c.drawString(x1 + 16, cur_y, line)
        cur_y -= 14
        
    # Member 2: Nurman Hariyanto
    x2 = x1 + card_w + 16
    draw_card(c, x2, card_y, card_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    # Avatar badge
    draw_card(c, x2 + (card_w - 70) / 2, card_y + card_h - 85, 70, 70, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=35)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x2 + card_w / 2, card_y + card_h - 48, "NH")
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x2 + card_w / 2, card_y + card_h - 75, "ANGGOTA 2")
    
    c.setFont("Helvetica-Bold", 12.5)
    c.setFillColor(TEXT_DARK)
    c.drawCentredString(x2 + card_w / 2, card_y + card_h - 105, "Nurman Hariyanto, S.ST., M.T.")
    
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x2 + card_w / 2, card_y + card_h - 122, "Lead Rekayasa Data & Infrastruktur")
    
    c.setStrokeColor(BORDER_LIGHT)
    c.line(x2 + 16, card_y + card_h - 134, x2 + card_w - 16, card_y + card_h - 134)
    
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(x2 + 16, card_y + card_h - 152, "AFILIASI & REKAM JEJAK:")
    
    lines_m2 = [
        "- Dosen Tetap Prodi Sistem Informasi,",
        "  Universitas Nahdlatul Ulama Kalbar",
        "- Alumni S2 STEI ITB & D4 POLBAN",
        "- Pengalaman: Big Data Engineering,",
        "  Pipeline ETL Skala Besar (50.000+ klaim),",
        "  Data Preprocessing & Sanitasi PDP",
        "- Spesialisasi: Cloud Systems, Skalabilitas,",
        "  Containerization & Keandalan Server",
        "- Lead arsitektur pipeline real-time & batch"
    ]
    cur_y = card_y + card_h - 170
    for line in lines_m2:
        c.drawString(x2 + 16, cur_y, line)
        cur_y -= 14

    # Member 3: M. Ali Maulana
    x3 = x2 + card_w + 16
    draw_card(c, x3, card_y, card_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    # Avatar badge
    draw_card(c, x3 + (card_w - 70) / 2, card_y + card_h - 85, 70, 70, bg_color=HexColor("#F3E8FF"), border_color=HexColor("#7E22CE"), radius=35)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawCentredString(x3 + card_w / 2, card_y + card_h - 48, "AM")
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawCentredString(x3 + card_w / 2, card_y + card_h - 75, "ANGGOTA 3")
    
    c.setFont("Helvetica-Bold", 12.5)
    c.setFillColor(TEXT_DARK)
    c.drawCentredString(x3 + card_w / 2, card_y + card_h - 105, "M. Ali Maulana, M.Kep.")
    
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x3 + card_w / 2, card_y + card_h - 122, "Lead Domain Klinis & Kepatuhan")
    
    c.setStrokeColor(BORDER_LIGHT)
    c.line(x3 + 16, card_y + card_h - 134, x3 + card_w - 16, card_y + card_h - 134)
    
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawString(x3 + 16, card_y + card_h - 152, "AFILIASI & REKAM JEJAK:")
    
    lines_m3 = [
        "- Dosen Tetap Prodi Keperawatan,",
        "  Fakultas Kedokteran Univ. Tanjungpura",
        "- Magister Keperawatan Univ. Diponegoro",
        "- Pengalaman: Tata Kelola Mutu Layanan FKRTL,",
        "  Audit Klinis Rumah Sakit & Kepatuhan JKN",
        "- Penguasaan Regulasi: Permenkes 26/2021",
        "  (Tarif INA-CBG) & Permenkes 16/2019",
        "  (Pencegahan Kecurangan/Fraud JKN)",
        "- Validasi klinis logika rule engine & kode"
    ]
    cur_y = card_y + card_h - 170
    for line in lines_m3:
        c.drawString(x3 + 16, cur_y, line)
        cur_y -= 14


def draw_slide_3_idea(c):
    """Slide 3: Judul Ide, Deskripsi, dan Tujuan strictly according to Page 5 of template."""
    draw_header(c, "Judul Ide, Deskripsi, dan Tujuan", slide_num_label="2", current_slide=3, total_slides=11)
    
    # Left Column: NAMA SOLUSI, NILAI UTAMA, KATEGORI, DESKRIPSI SINGKAT
    left_w = 460
    
    # Box 1: NAMA SOLUSI & NILAI UTAMA
    draw_card(c, 48, 290, left_w, 175, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_GREEN)
    c.drawString(64, 445, "N A M A   S O L U S I")
    
    c.setFont("Helvetica-Bold", 17)
    c.setFillColor(TEXT_DARK)
    c.drawString(64, 424, "VeriKlaim")
    
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(64, 400, "S A T U   K A L I M A T   N I L A I   U T A M A")
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_DARK)
    val_lines = [
        "\"Solusi ini membantu Verifikator BPJS Kesehatan dan Tim Pengendali",
        "Fraud Faskes mendeteksi kecurangan klaim INA-CBG secara otomatis,",
        "transparan, dan berlandaskan regulasi klinis sebelum pembayaran",
        "dilakukan, agar efisiensi dana jaminan sosial tercapai optimal.\""
    ]
    val_y = 384
    for vl in val_lines:
        c.drawString(64, val_y, vl)
        val_y -= 13
        
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(64, 308, "KATEGORI: Efisiensi Risiko Program JKN  |  SUB: Efisiensi Risiko Faskes (KLAIM - C03.04)")

    # Box 2: DESKRIPSI SINGKAT
    draw_card(c, 48, 52, left_w, 224, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN)
    c.drawString(64, 256, "D E S K R I P S I   S I N G K A T")
    
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    desc_lines = [
        "VeriKlaim adalah platform deteksi anomali klaim FKRTL yang mengintegrasikan",
        "ensemble machine learning (LightGBM & XGBoost) dengan Multi-Agent Deterministic",
        "Rule Engine berlandaskan regulasi Permenkes No. 26/2021 dan Permenkes No. 16/2019.",
        "",
        "Bagaimana cara kerjanya secara garis besar:",
        "1. Ingest Data: Membaca berkas klaim (LOS, kode ICD-10, ICD-9-CM, Severity Level).",
        "2. Dual-Engine Screening: Menilai risiko anomali secara statistik probabilistik (AI)",
        "   sekaligus menguji kepatuhan kaidah koding medis baku (Rule Engine).",
        "3. Explainable AI: Menjelaskan alasan penetapan anomali melalui SHAP values",
        "   dan pasal hukum Permenkes terkait.",
        "4. Audit Dossier: Menerbitkan Berita Acara Audit resmi format PDF ber-QR code",
        "   dalam hitungan detik untuk penyelesaian dispute transparan."
    ]
    desc_y = 236
    for dl in desc_lines:
        c.drawString(64, desc_y, dl)
        desc_y -= 13.5
        
    # Right Column: TUJUAN (2 sampai 3 tujuan spesifik dan terukur)
    right_x = 48 + left_w + 16
    right_w = PAGE_WIDTH - 48 - right_x
    
    draw_card(c, right_x, 52, right_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(BPJS_GREEN)
    c.drawString(right_x + 20, 442, "T U J U A N   S P E S I F I K   D A N   T E R U K U R")
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(right_x + 20, 424, "Tiga target kuantitatif yang dicapai melalui implementasi VeriKlaim:")
    
    # Goal Card 1
    draw_card(c, right_x + 16, 305, right_w - 32, 102, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(right_x + 28, 386, "1. Efisiensi Waktu Telaah Klaim > 85%")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 366, "- Memangkas waktu telaah klaim berisiko dari rata-rata")
    c.drawString(right_x + 28, 350, "  15-20 menit per berkas manual menjadi < 3 detik per klaim.")
    c.drawString(right_x + 28, 334, "- Verifikasi instan memungkinkan 100% berkas diaudit secara")
    c.drawString(right_x + 28, 318, "  pre-payment tanpa menumpuk antrean pencairan faskes.")
    
    # Goal Card 2
    draw_card(c, right_x + 16, 185, right_w - 32, 106, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=6)
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 28, 268, "2. Presisi Deteksi Anomali: ROC-AUC 1.0000")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 248, "- Mencapai akurasi deteksi anomali F1-Score 0.99 dan")
    c.drawString(right_x + 28, 232, "  ROC-AUC 1.0000 pada data uji 50.000 klaim FKRTL BPJS.")
    c.drawString(right_x + 28, 216, "- Meminimalkan false positive (< 0.6%) sehingga hubungan")
    c.drawString(right_x + 28, 200, "  kemitraan dengan rumah sakit tetap terjaga harmonis.")
    
    # Goal Card 3
    draw_card(c, right_x + 16, 66, right_w - 32, 105, bg_color=HexColor("#FDF2F8"), border_color=HexColor("#DB2777"), radius=6)
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(HexColor("#9D174D"))
    c.drawString(right_x + 28, 148, "3. Reduksi Sengketa (Dispute) Hingga 70%")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 128, "- Menurunkan klaim pending/dispute berlarut dari 14-30 hari")
    c.drawString(right_x + 28, 112, "  menjadi 1-2 hari kerja.")
    c.drawString(right_x + 28, 96, "- Memberikan justifikasi hukum baku dan bukti klinis yang")
    c.drawString(right_x + 28, 80, "  dapat diterima secara transparan oleh manajemen RS & BPJS.")


def draw_slide_4_background_impact(c):
    """Slide 4: Latar Belakang dan Dampak strictly according to Page 6 of template."""
    draw_header(c, "Latar Belakang dan Dampak", slide_num_label="3", current_slide=4, total_slides=11)
    
    # Left Column: LATAR BELAKANG
    left_w = 460
    draw_card(c, 48, 52, left_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(66, 442, "L A T A R   B E L A K A N G")
    
    # Sub-item 1: Persoalan spesifik
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(66, 420, "1. Persoalan Spesifik yang Ingin Diselesaikan")
    c.setFont("Helvetica", 8.7)
    c.setFillColor(TEXT_MUTED)
    p_lines = [
        "Lonjakan volume klaim FKRTL mencapai puluhan juta berkas per tahun,",
        "sementara verifikasi manual terbatas pada uji petik (10-20% sampel).",
        "Praktik fraud terselubung seperti Upcoding tingkat keparahan, Unbundling",
        "prosedur tunggal menjadi beberapa tagihan, serta Phantom Billing",
        "sangat sulit dideteksi kasat mata tanpa komparasi data silang."
    ]
    py = 405
    for pl in p_lines:
        c.drawString(66, py, pl)
        py -= 12.5
        
    # Sub-item 2: Mengapa penting dan mendesak?
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(66, 328, "2. Mengapa Penting & Mendesak? Siapa Terdampak?")
    c.setFont("Helvetica", 8.7)
    c.setFillColor(TEXT_MUTED)
    u_lines = [
        "- Peserta JKN: Dana jaminan sosial (DJS) terancam defisit aktuaria.",
        "- Faskes (RS): Pembayaran klaim tersendat akibat dispute berlarut.",
        "- BPJS Kesehatan: Beban administrasi telaah manual memicu inefisiensi",
        "  operasional dan risiko temuan audit eksternal."
    ]
    uy = 313
    for ul in u_lines:
        c.drawString(66, uy, ul)
        uy -= 12.5
        
    # Sub-item 3: Bukti / Data yang memperkuat
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(ACCENT_RED)
    c.drawString(66, 246, "3. Bukti dan Data Penguat (Sumber Resmi)")
    c.setFont("Helvetica", 8.7)
    c.setFillColor(TEXT_DARK)
    b_lines = [
        "- Temuan KPK RI & BPK RI (Juli 2024): Dugaan klaim fiktif & phantom",
        "  billing pada 3 rumah sakit di Sumut & Jateng senilai Rp 35 Miliar.",
        "- Audit BPK RI (Pengelolaan JKN): Rekomendasi penguatan sistem",
        "  early-warning deteksi kecurangan klaim sebelum dilakukan pembayaran.",
        "- Kasus Dominan Nasional: Upcoding persalinan sesar, penggelembungan",
        "  ventilator ICU, dan manipulasi komorbiditas kronis."
    ]
    by = 231
    for bl in b_lines:
        c.drawString(66, by, bl)
        by -= 12.5
        
    # Image thumbnail if available
    img_kpk = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\docs\assets\referensi_berita_kpk.png"
    if os.path.exists(img_kpk):
        c.drawImage(img_kpk, 66, 62, width=190, height=72, preserveAspectRatio=True)
        c.setFont("Helvetica-Bold", 7.5)
        c.setFillColor(BPJS_BLUE)
        c.drawString(266, 120, "Referensi Resmi KPK RI & BPK:")
        c.setFont("Helvetica", 7.5)
        c.setFillColor(TEXT_MUTED)
        c.drawString(266, 105, "Kajian Kecurangan Klaim JKN")
        c.drawString(266, 92, "Modus Phantom Billing & Upcoding")
        c.drawString(266, 79, "Sumber: Kompas / KPK RI (2024)")

    # Right Column: DAMPAK (3 Indikator terukur sebelum vs sesudah)
    right_x = 48 + left_w + 16
    right_w = PAGE_WIDTH - 48 - right_x
    
    draw_card(c, right_x, 52, right_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(right_x + 20, 442, "D A M P A K   Y A N G   D I H A S I L K A N")
    
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_MUTED)
    c.drawString(right_x + 20, 424, "Perbaikan nyata dibandingkan kondisi saat ini (Sebelum vs Sesudah):")
    
    # Impact Metric 1: Waktu Telaah
    draw_card(c, right_x + 16, 305, right_w - 32, 105, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(right_x + 28, 386, "< 3 Detik / Berkas")
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 368, "Indikator 1: Kecepatan Telaah Verifikasi Klaim")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 350, "- Sebelum : 15 - 20 menit per berkas sengketa manual.")
    c.drawString(right_x + 28, 334, "- Sesudah : < 3 detik per berkas otomatis real-time.")
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(right_x + 28, 318, "- Hasil    : Efisiensi operasional telaah berkas sebesar 85% - 98%.")

    # Impact Metric 2: Cakupan Audit
    draw_card(c, right_x + 16, 185, right_w - 32, 105, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=6)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 28, 266, "100% Pre-Payment Audit")
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 248, "Indikator 2: Cakupan Audit & Presisi Deteksi")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 230, "- Sebelum : 10% - 20% klaim melalui uji petik manual.")
    c.drawString(right_x + 28, 214, "- Sesudah : 100% seluruh klaim disaring sebelum bayar.")
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 28, 198, "- Hasil    : ROC-AUC 1.0000 / Presisi 99.4% cegah kebocoran DJS.")

    # Impact Metric 3: Durasi Dispute
    draw_card(c, right_x + 16, 65, right_w - 32, 105, bg_color=ACCENT_AMBER_LIGHT, border_color=ACCENT_AMBER, radius=6)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor("#B7791F"))
    c.drawString(right_x + 28, 146, "1 - 2 Hari Kerja")
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 128, "Indikator 3: Durasi Penyelesaian Dispute Klaim")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 110, "- Sebelum : 14 - 30 hari masa sanggah sengketa klaim.")
    c.drawString(right_x + 28, 94, "- Sesudah : 1 - 2 hari kerja selesai tuntas.")
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(HexColor("#744210"))
    c.drawString(right_x + 28, 78, "- Hasil    : Berita Acara Audit XAI instan berdasar hukum Permenkes.")


def draw_slide_5_process_flow(c):
    """Slide 5: Alur Proses Aplikasi strictly according to Page 7 of template."""
    draw_header(c, "Alur Proses Aplikasi", slide_num_label="4", current_slide=5, total_slides=11)
    
    # Top Section: 5 Tahapan Alur Proses Horizontal
    card_y = 285
    step_w = (PAGE_WIDTH - 96 - 48) / 5.0
    step_h = 180
    
    steps = [
        ("1. Input", [
            "Penerimaan data transaksi",
            "klaim FKRTL via API bridging",
            "e-Klaim/VClaim BPJS atau",
            "batch upload CSV/JSON.",
            "",
            "Atribut: LOS, ICD-10,",
            "ICD-9-CM, Severity,",
            "Tarif RS & Tarif Acuan."
        ], BPJS_GREEN_LIGHT, BPJS_GREEN),
        ("2. Proses", [
            "Validasi skema klaim,",
            "sanitasi data & anonimisasi",
            "NIK (kepatuhan UU PDP).",
            "",
            "Feature Engineering:",
            "Kalkulasi rasio tarif/LOS,",
            "cross-check ICD primer,",
            "validasi severity mismatch."
        ], BPJS_BLUE_LIGHT, BPJS_BLUE),
        ("3. Analisis AI", [
            "Dual-Engine Inference:",
            "- Ensemble ML (LightGBM",
            "  & XGBoost) hitung Skor",
            "  Probabilitas Anomali.",
            "- Deterministic Rule Engine",
            "  menguji Permenkes 26/2021",
            "  (Upcoding & Unbundling)."
        ], HexColor("#F3E8FF"), HexColor("#7E22CE")),
        ("4. Output", [
            "Visualisasi Dashboard:",
            "- Klasifikasi: Wajar /",
            "  Waspada / Fraud Tinggi.",
            "- Skor Anomali (0 - 100%).",
            "- Breakdown SHAP values",
            "  (faktor pemicu anomali).",
            "- Rekomendasi tindakan."
        ], ACCENT_AMBER_LIGHT, HexColor("#D97706")),
        ("5. Tindak Lanjut", [
            "Verifikator mengevaluasi:",
            "- Setujui Klaim Layak.",
            "- Klarifikasi Faskes.",
            "- Unduh Berita Acara",
            "  Audit Resmi format PDF",
            "  ber-QR code & dasar",
            "  hukum untuk dispute."
        ], ACCENT_RED_LIGHT, ACCENT_RED)
    ]
    
    for i, (title, lines, bg_col, border_col) in enumerate(steps):
        sx = 48 + i * (step_w + 12)
        draw_card(c, sx, card_y, step_w, step_h, bg_color=bg_col, border_color=border_col, radius=6)
        
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(border_col)
        c.drawString(sx + 10, card_y + step_h - 22, title)
        
        c.setStrokeColor(border_col)
        c.setLineWidth(0.8)
        c.line(sx + 10, card_y + step_h - 28, sx + step_w - 10, card_y + step_h - 28)
        
        c.setFont("Helvetica", 7.8)
        c.setFillColor(TEXT_DARK)
        ly = card_y + step_h - 44
        for l in lines:
            c.drawString(sx + 10, ly, l)
            ly -= 11.5
            
        # Draw connector arrow between cards
        if i < 4:
            arrow_x = sx + step_w + 2
            arrow_y = card_y + step_h / 2
            c.setFont("Helvetica-Bold", 12)
            c.setFillColor(BPJS_GREEN)
            c.drawString(arrow_x, arrow_y, ">")

    # Bottom Section: 3 Kotak (PENGGUNA/AKTOR, DATA YANG DIPAKAI, TEKNOLOGI)
    bot_y = 52
    bot_h = 215
    col3_w = (PAGE_WIDTH - 96 - 32) / 3.0
    
    # Box 1: PENGGUNA / AKTOR
    bx1 = 48
    draw_card(c, bx1, bot_y, col3_w, bot_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(BPJS_GREEN)
    c.drawString(bx1 + 16, bot_y + bot_h - 24, "PENGGUNA / AKTOR")
    c.setFont("Helvetica", 8.5)
    c.setFillColor(TEXT_DARK)
    actors = [
        "- Verifikator Klaim BPJS Kesehatan:",
        "  Menelaah klaim berkategori anomali,",
        "  menolak/menyetujui berkas, mencetak",
        "  Berita Acara Audit resmi.",
        "- Tim Pencegahan Kecurangan Faskes (RS):",
        "  Melakukan pra-audit mandiri sebelum",
        "  klaim diajukan ke BPJS untuk mencegah",
        "  klaim pending & dispute.",
        "- Auditor Internal & Manajemen Risiko:",
        "  Memantau indeks risiko anomali faskes",
        "  secara makro di tingkat cabang & nasional."
    ]
    ay = bot_y + bot_h - 46
    for act in actors:
        c.drawString(bx1 + 16, ay, act)
        ay -= 13.5
        
    # Box 2: DATA YANG DIPAKAI
    bx2 = bx1 + col3_w + 16
    draw_card(c, bx2, bot_y, col3_w, bot_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(bx2 + 16, bot_y + bot_h - 24, "DATA YANG DIPAKAI")
    c.setFont("Helvetica", 8.5)
    c.setFillColor(TEXT_DARK)
    data_info = [
        "- Sumber: Dataset sampel publik FKRTL BPJS",
        "  Kesehatan (50.000 transaksi terstruktur).",
        "- Atribut: No Registrasi terenkripsi, Usia,",
        "  Gender, LOS (Lama Rawat), Kelas Perawatan,",
        "  ICD-10 Diagnosa Primer & Sekunder,",
        "  ICD-9-CM Prosedur, Severity Level (I, II, III),",
        "  Tarif Diajukan RS, Tarif Acuan INA-CBG.",
        "- Batasan: Data telah dianonimisasi penuh",
        "  tanpa memuat NIK/identitas pasien riil",
        "  sesuai kaidah kerahasiaan medis & UU PDP."
    ]
    dy = bot_y + bot_h - 46
    for d in data_info:
        c.drawString(bx2 + 16, dy, d)
        dy -= 13.5
        
    # Box 3: TEKNOLOGI
    bx3 = bx2 + col3_w + 16
    draw_card(c, bx3, bot_y, col3_w, bot_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawString(bx3 + 16, bot_y + bot_h - 24, "TEKNOLOGI & ALASAN")
    c.setFont("Helvetica", 8.5)
    c.setFillColor(TEXT_DARK)
    tech_info = [
        "- Python 3.12 & FastAPI:",
        "  Arsitektur microservice asinkron dengan",
        "  throughput > 1.200 klaim/detik & latensi < 50ms.",
        "- LightGBM & XGBoost (Ensemble):",
        "  Akurasi superior pada data tabular klaim",
        "  dengan imbalanced fraud ratio.",
        "- TreeSHAP (Explainable AI):",
        "  Dekomposisi kontribusi fitur matematis",
        "  untuk transparansi tanpa 'black-box'.",
        "- ReportLab Engine: Generator Berita Acara",
        "  PDF otomatis ber-QR code verifikasi legal."
    ]
    ty = bot_y + bot_h - 46
    for t in tech_info:
        c.drawString(bx3 + 16, ty, t)
        ty -= 13.5


def draw_slide_6_demo_prototype(c):
    """Slide 6: Demo Aplikasi / Prototype strictly according to Page 8 of template."""
    draw_header(c, "Demo Aplikasi / Prototype", slide_num_label="5", current_slide=6, total_slides=11)
    
    # Left Column: Visual Mockup / Screen Capture of the running system
    left_w = 460
    draw_card(c, 48, 52, left_w, 413, bg_color=HexColor("#0F172A"), border_color=BORDER_LIGHT, radius=8)
    
    # Mockup Header Bar
    c.setFillColor(HexColor("#1E293B"))
    c.rect(48, 435, left_w, 30, fill=True, stroke=False)
    # Window circles
    c.setFillColor(HexColor("#EF4444"))
    c.circle(64, 450, 4, fill=True, stroke=False)
    c.setFillColor(HexColor("#F59E0B"))
    c.circle(76, 450, 4, fill=True, stroke=False)
    c.setFillColor(HexColor("#10B981"))
    c.circle(88, 450, 4, fill=True, stroke=False)
    
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(WHITE)
    c.drawString(108, 446, "VeriKlaim - BPJS Kesehatan Risk Engine (http://127.0.0.1:8000)")
    
    # Dashboard Preview Cards inside Mockup
    # Stat box 1
    draw_card(c, 64, 375, 128, 48, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(72, 408, "Total Klaim Teruji")
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(WHITE)
    c.drawString(72, 388, "50.000 Klaim")
    
    # Stat box 2
    draw_card(c, 204, 375, 128, 48, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(212, 408, "Anomali Terdeteksi")
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(ACCENT_RED)
    c.drawString(212, 388, "137 Kasus (0.27%)")

    # Stat box 3
    draw_card(c, 344, 375, 148, 48, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(352, 408, "Efisiensi Biaya")
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(BPJS_GREEN)
    c.drawString(352, 388, "Rp 1.84 Miliar")
    
    # Interactive Claim Audit Panel
    draw_card(c, 64, 185, 428, 175, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=6)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN)
    c.drawString(76, 342, "HASIL EVALUASI REAL-TIME: KLAIM SUSPEK UPCODING")
    
    # Anomaly badge
    draw_card(c, 360, 328, 120, 22, bg_color=HexColor("#7F1D1D"), border_color=ACCENT_RED, radius=4)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(WHITE)
    c.drawCentredString(420, 335, "[!] FRAUD TINGGI (96.8%)")
    
    c.setFont("Helvetica", 8)
    c.setFillColor(WHITE)
    c.drawString(76, 318, "No SEP: SEP-2026-99214  |  Faskes: RSUD Permata Medika (Tipe B)")
    c.drawString(76, 302, "Diagnosa: O82.1 (Sesar Darurat)  |  Severity: Level 3 (Komp. Berat)")
    c.drawString(76, 286, "LOS: 1 Hari  |  Tarif RS: Rp 36.500.000 vs Acuan INA-CBG: Rp 6.200.000")
    
    # XAI bars mockup
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ACCENT_AMBER)
    c.drawString(76, 264, "Pemicu Utama (Explainable AI SHAP Decomposition):")
    
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(76, 248, "1. Tarif Ratio Discrepancy (5.88x di atas acuan)  -> SHAP: +0.42 [Kritis]")
    c.drawString(76, 234, "2. LOS to Severity Level Mismatch (LOS 1 hari Severity III) -> SHAP: +0.31")
    c.drawString(76, 220, "3. Pelanggaran Regulasi: Permenkes 26/2021 Pasal 14 ayat (2)")
    
    # PDF button mockup
    draw_card(c, 76, 195, 230, 20, bg_color=BPJS_BLUE, border_color=BPJS_BLUE, radius=3)
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(WHITE)
    c.drawCentredString(191, 201, "Unduh Berita Acara Audit Resmi (PDF)")

    # Bottom notice in mockup
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawCentredString(48 + left_w / 2, 75, "Server Live: http://127.0.0.1:8000 | Latensi Inferensi: 38 ms")

    # Right Column: SKENARIO DEMO & TAUTAN PROTOTYPE
    right_x = 48 + left_w + 16
    right_w = PAGE_WIDTH - 48 - right_x
    
    draw_card(c, right_x, 52, right_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(right_x + 20, 442, "S K E N A R I O   D E M O   ( 4   L A N G K A H )")
    
    # 4 Demo Steps
    demo_steps = [
        ("1", "Eksplorasi Portfolio Dashboard (50.000 Klaim)", [
            "Menampilkan agregasi makro klaim FKRTL terproses, sebaran anomali",
            "per departemen, dan rasio risiko klaim faskes secara real-time."
        ], BPJS_GREEN),
        ("2", "Audit Klaim Interaktif Kasus Upcoding", [
            "Memasukkan sampel klaim suspek persalinan sesar darurat dengan",
            "LOS 1 hari berkategori Severity III. Sistem seketika mendeteksi",
            "anomali dengan Skor 96.8% dan mengibarkan flag Upcoding."
        ], BPJS_BLUE),
        ("3", "Inspeksi Explainable AI (XAI) & Bukti Regulasi", [
            "Verifikator melihat transparansi kontribusi variabel SHAP (rasio tarif",
            "& inkonsistensi LOS) serta rujukan pasal hukum Permenkes 26/2021."
        ], HexColor("#7E22CE")),
        ("4", "Penerbitan Berita Acara Audit Resmi PDF", [
            "Menghasilkan dokumen resmi Berita Acara Audit lengkap dengan QR Code,",
            "dasar hukum, dan kalkulasi selisih tarif dalam 1 detik untuk klarifikasi."
        ], ACCENT_RED)
    ]
    
    sy = 412
    for num, title, lines, color_accent in demo_steps:
        # Step number badge
        draw_card(c, right_x + 20, sy - 26, 26, 26, bg_color=WHITE, border_color=color_accent, radius=13)
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(color_accent)
        c.drawCentredString(right_x + 33, sy - 18, num)
        
        c.setFont("Helvetica-Bold", 9.5)
        c.setFillColor(TEXT_DARK)
        c.drawString(right_x + 56, sy - 10, title)
        
        c.setFont("Helvetica", 8.2)
        c.setFillColor(TEXT_MUTED)
        ly = sy - 24
        for l in lines:
            c.drawString(right_x + 56, ly, l)
            ly -= 11.5
            
        sy -= 66
        
    # Box: TAUTAN PROTOTYPE
    draw_card(c, right_x + 16, 62, right_w - 32, 70, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(right_x + 28, 116, "T A U T A N   P R O T O T Y P E   L I V E")
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 28, 98, "http://127.0.0.1:8000")
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 80, "Repositori: https://github.com/orochimadit/veri-klaim.git")


def draw_slide_7_features(c):
    """Slide 7: Penjelasan Fitur strictly according to Page 9 of template."""
    draw_header(c, "Penjelasan Fitur", slide_num_label="6", current_slide=7, total_slides=11)
    
    # 4 Major Features Grid (2x2)
    grid_w = (PAGE_WIDTH - 96 - 20) / 2.0
    grid_h = 195
    
    features = [
        ("Fitur 1: AI Anomaly Scoring Engine",
         "Fungsi: Apa yang dilakukan fitur ini?",
         "Menganalisis multi-fitur klaim secara simultan menggunakan ensemble model"
         " LightGBM dan XGBoost untuk menghasilkan skor probabilitas kecurangan 0.00 - 1.00"
         " dalam waktu < 50 milidetik per berkas klaim.",
         "Menjawab Masalah: Bagian mana yang diselesaikan?",
         "Mengatasi keterbatasan verifikasi manual manusia dalam mendeteksi kombinasi anomali"
         " terselubung pada jutaan berkas klaim berskala nasional sebelum klaim dibayarkan.",
         BPJS_GREEN),
        
        ("Fitur 2: Regulatory Rule-Based Validator",
         "Fungsi: Apa yang dilakukan fitur ini?",
         "Memvalidasi kepatuhan kaidah koding INA-CBG secara deterministik berpedoman pada"
         " Permenkes No. 26/2021 dan Permenkes No. 16/2019: mendeteksi upcoding tingkat keparahan,"
         " unbundling tindakan bedah, dan tagihan tumpang-tindih (phantom billing).",
         "Menjawab Masalah: Bagian mana yang diselesaikan?",
         "Memberikan kepastian hukum yang mengikat dan sah pada setiap temuan audit, sehingga"
         " telaah verifikator tidak dapat disanggah sepihak oleh rumah sakit mitra.",
         BPJS_BLUE),
        
        ("Fitur 3: Explainable AI (XAI) & Dynamic Reasoner",
         "Fungsi: Apa yang dilakukan fitur ini?",
         "Membongkar 'kotak hitam' model machine learning melalui dekomposisi SHAP values"
         " dan menyajikannya dalam bentuk narasi klinis transparan yang menjelaskan variabel"
         " dominan apa saja yang menyebabkan klaim ditandai anomali.",
         "Menjawab Masalah: Bagian mana yang diselesaikan?",
         "Mengeliminasi penolakan rekomendasi sistem oleh klinisi/faskes dengan menyajikan"
         " justifikasi rasional yang terbukti matematis dan dapat dipahami secara medis.",
         HexColor("#7E22CE")),
        
        ("Fitur 4: Automated Audit Dossier Generator (PDF Resmi)",
         "Fungsi: Apa yang dilakukan fitur ini?",
         "Mengompilasi ringkasan klaim, riwayat rawat, bukti penyimpangan tarif, sitasi pasal regulasi,"
         " dan QR Code verifikasi menjadi Berita Acara Hasil Audit standar formal format PDF.",
         "Menjawab Masalah: Bagian mana yang diselesaikan?",
         "Memangkas birokrasi penyusunan berkas sengketa/klarifikasi klaim dari 14-30 hari"
         " menjadi hitungan detik dengan dokumen legal siap tanda tangan verifikator.",
         ACCENT_RED)
    ]
    
    coords = [
        (48, 260),
        (48 + grid_w + 20, 260),
        (48, 52),
        (48 + grid_w + 20, 52)
    ]
    
    for (title, f_label, f_text, m_label, m_text, accent_col), (gx, gy) in zip(features, coords):
        draw_card(c, gx, gy, grid_w, grid_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
        
        # Header banner inside card
        c.setFillColor(accent_col)
        c.rect(gx, gy + grid_h - 6, grid_w, 6, fill=True, stroke=False)
        
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(accent_col)
        c.drawString(gx + 16, gy + grid_h - 24, title)
        
        # Fungsi block
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(TEXT_DARK)
        c.drawString(gx + 16, gy + grid_h - 44, f_label)
        
        c.setFont("Helvetica", 8)
        c.setFillColor(TEXT_MUTED)
        # Wrap f_text
        words_f = f_text.split()
        line_cur = []
        cur_y = gy + grid_h - 58
        for w in words_f:
            line_cur.append(w)
            if len(" ".join(line_cur)) > 66:
                c.drawString(gx + 16, cur_y, " ".join(line_cur[:-1]))
                line_cur = [w]
                cur_y -= 11
        if line_cur:
            c.drawString(gx + 16, cur_y, " ".join(line_cur))
            cur_y -= 11
            
        # Menjawab masalah block
        cur_y -= 4
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(TEXT_DARK)
        c.drawString(gx + 16, cur_y, m_label)
        cur_y -= 14
        
        c.setFont("Helvetica", 8)
        c.setFillColor(TEXT_MUTED)
        words_m = m_text.split()
        line_cur = []
        for w in words_m:
            line_cur.append(w)
            if len(" ".join(line_cur)) > 66:
                c.drawString(gx + 16, cur_y, " ".join(line_cur[:-1]))
                line_cur = [w]
                cur_y -= 11
        if line_cur:
            c.drawString(gx + 16, cur_y, " ".join(line_cur))


def draw_slide_8_architecture(c):
    """Slide 8: Slide Tambahan - Arsitektur Teknis dan Data strictly according to Page 10 of template."""
    draw_header(c, "Slide Tambahan: Arsitektur Teknis dan Pipeline Data", slide_num_label="+", current_slide=8, total_slides=11)
    
    # 5 Architecture Layers (Stacked horizontally/vertically)
    top_y = 330
    layer_w = PAGE_WIDTH - 96
    layer_h = 135
    
    draw_card(c, 48, top_y, layer_w, layer_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(BPJS_GREEN)
    c.drawString(64, top_y + layer_h - 22, "DIAGRAM ARSITEKTUR SISTEM VERIKLAIM (5-TIER PIPELINE)")
    
    col5_w = (layer_w - 32 - 40) / 5.0
    layers = [
        ("Tier 1: Ingestion", "Bridging VClaim, e-Klaim INA-CBG, atau Batch CSV/JSON REST API", BPJS_GREEN_LIGHT, BPJS_GREEN),
        ("Tier 2: Security & PDP", "Zero PII Storage, SHA-256 Hash Masking NIK, Sanitasi Data Medis", BPJS_BLUE_LIGHT, BPJS_BLUE),
        ("Tier 3: Dual-Core AI", "Ensemble LightGBM/XGBoost + Deterministic Permenkes Rule Matrix", HexColor("#F3E8FF"), HexColor("#7E22CE")),
        ("Tier 4: XAI Reasoner", "TreeSHAP Decomposition + Auto Dossier ReportLab PDF Generator", ACCENT_AMBER_LIGHT, HexColor("#D97706")),
        ("Tier 5: Presentation", "Dashboard Monitoring Verifikator, Alerting & Dispute Resolution", ACCENT_RED_LIGHT, ACCENT_RED)
    ]
    
    for i, (ltitle, ldesc, bg_col, border_col) in enumerate(layers):
        lx = 64 + i * (col5_w + 10)
        draw_card(c, lx, top_y + 14, col5_w, layer_h - 48, bg_color=bg_col, border_color=border_col, radius=6)
        
        c.setFont("Helvetica-Bold", 8.8)
        c.setFillColor(border_col)
        c.drawString(lx + 8, top_y + layer_h - 52, ltitle)
        
        c.setFont("Helvetica", 7.5)
        c.setFillColor(TEXT_DARK)
        # wrap
        words = ldesc.split()
        l_cur = []
        cy = top_y + layer_h - 68
        for w in words:
            l_cur.append(w)
            if len(" ".join(l_cur)) > 22:
                c.drawString(lx + 8, cy, " ".join(l_cur[:-1]))
                l_cur = [w]
                cy -= 10
        if l_cur:
            c.drawString(lx + 8, cy, " ".join(l_cur))

    # Bottom 3 Technical Specs Cards
    bot_y = 52
    bot_h = 260
    col3_w = (PAGE_WIDTH - 96 - 32) / 3.0
    
    # Box 1: Sumber Data & Keterbatasan
    bx1 = 48
    draw_card(c, bx1, bot_y, col3_w, bot_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(BPJS_GREEN)
    c.drawString(bx1 + 16, bot_y + bot_h - 24, "SUMBER DATA & KETERBATASAN")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_DARK)
    b1_lines = [
        "- Dataset: 50.000 sampel data klaim FKRTL",
        "  terstruktur dengan atribut lengkap:",
        "  LOS, Severity, ICD-10, ICD-9, Tarif RS,",
        "  dan Tarif Acuan INA-CBG.",
        "- Keterbatasan Data:",
        "  Model dilatih pada data terstandarisasi;",
        "  variasi koding non-standar lokal faskes",
        "  dimitigasi melalui normalisasi kamus",
        "  referensi diagnosa Kemenkes.",
        "- Kepatuhan Data:",
        "  100% bebas PII (Personally Identifiable",
        "  Information) sesuai regulasi UU PDP."
    ]
    y = bot_y + bot_h - 44
    for l in b1_lines:
        c.drawString(bx1 + 16, y, l)
        y -= 12.5

    # Box 2: Model & Algoritma yang Dipilih
    bx2 = bx1 + col3_w + 16
    draw_card(c, bx2, bot_y, col3_w, bot_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(BPJS_BLUE)
    c.drawString(bx2 + 16, bot_y + bot_h - 24, "MODEL & ALASAN PEMILIHAN")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_DARK)
    b2_lines = [
        "- Ensemble LightGBM & XGBoost:",
        "  Optimal untuk data tabular klaim berdimensi",
        "  campuran (kategorikal & numerik).",
        "- Ketahanan Imbalanced Data:",
        "  Mampu menangani rasio anomali fraud yang",
        "  sangat langka (0.27%) tanpa over-fitting.",
        "- Multi-Agent Rule Matrix:",
        "  Menjamin kepatuhan deterministik terhadap",
        "  Permenkes 26/2021 & Permenkes 16/2019.",
        "- Integrasi SHAP TreeExplainer:",
        "  Menghasilkan atribusi fitur eksak untuk",
        "  setiap klaim individual secara instan."
    ]
    y = bot_y + bot_h - 44
    for l in b2_lines:
        c.drawString(bx2 + 16, y, l)
        y -= 12.5

    # Box 3: Benchmark Performa & Latensi
    bx3 = bx2 + col3_w + 16
    draw_card(c, bx3, bot_y, col3_w, bot_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawString(bx3 + 16, bot_y + bot_h - 24, "BENCHMARK PERFORMA TEKNIS")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_DARK)
    b3_lines = [
        "- Latensi Inferensi Single Claim: < 50 ms",
        "  (Rata-rata 38 ms pada mesin standar).",
        "- Throughput Batch Processing:",
        "  > 1.200 klaim per detik per worker node.",
        "- Memory Footprint Operasional: < 500 MB RAM",
        "  Sangat ringan dan hemat infrastruktur.",
        "- Kesiapan Bridging:",
        "  Kompatibel penuh dengan protokol REST API",
        "  dan format JSON e-Klaim BPJS.",
        "- Skalabilitas Horizontal:",
        "  Dapat dideploy multi-instance container."
    ]
    y = bot_y + bot_h - 44
    for l in b3_lines:
        c.drawString(bx3 + 16, y, l)
        y -= 12.5


def draw_slide_9_governance(c):
    """Slide 9: Slide Tambahan - Keamanan, Privasi, dan Tata Kelola AI strictly according to Page 10."""
    draw_header(c, "Slide Tambahan: Keamanan, Privasi, dan Tata Kelola AI", slide_num_label="+", current_slide=9, total_slides=11)
    
    col3_w = (PAGE_WIDTH - 96 - 32) / 3.0
    card_h = 413
    card_y = 52
    
    # Column 1: Kepatuhan UU PDP (No. 27/2022)
    x1 = 48
    draw_card(c, x1, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, x1 + 16, card_y + card_h - 48, col3_w - 32, 34, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=4)
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawCentredString(x1 + col3_w / 2, card_y + card_h - 32, "KEPATUHAN UU PDP NO. 27/2022")
    
    c.setFont("Helvetica", 8.5)
    c.setFillColor(TEXT_DARK)
    lines_pdp = [
        "- Zero PII Storage Policy:",
        "  Sistem VeriKlaim tidak pernah menyimpan",
        "  NIK, Nama Pasien, maupun Nomor Telepon",
        "  di dalam basis data inferensi AI.",
        "",
        "- One-Way Pseudonymization:",
        "  Identitas peserta disamarkan menggunakan",
        "  hashing kriptografis satu arah (SHA-256)",
        "  sebelum diproses oleh pipeline machine learning.",
        "",
        "- Standar Keamanan Data Tingkat Tinggi:",
        "  Dukungan enkripsi TLS 1.3 saat transmisi data",
        "  dan AES-256 pada penyimpanan lokal.",
        "",
        "- Kedaulatan Data Medis:",
        "  Dapat berjalan 100% On-Premise di server",
        "  BPJS Kesehatan tanpa ketergantungan API pihak",
        "  ketiga atau layanan cloud publik asing."
    ]
    py = card_y + card_h - 70
    for l in lines_pdp:
        c.drawString(x1 + 16, py, l)
        py -= 13.5

    # Column 2: Mitigasi Risiko AI & Human-in-the-Loop
    x2 = x1 + col3_w + 16
    draw_card(c, x2, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, x2 + 16, card_y + card_h - 48, col3_w - 32, 34, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=4)
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x2 + col3_w / 2, card_y + card_h - 32, "TATA KELOLA HUMAN-IN-THE-LOOP")
    
    c.setFont("Helvetica", 8.5)
    c.setFillColor(TEXT_DARK)
    lines_gov = [
        "- AI Murni Sebagai Decision Support System:",
        "  VeriKlaim tidak mengambil keputusan hukum",
        "  secara sepihak/otonom (Zero Auto-Denial).",
        "",
        "- Otoritas Final Pada Verifikator Resmi:",
        "  Status penerimaan, penolakan, atau klarifikasi",
        "  klaim 100% tetap dipegang oleh Verifikator",
        "  Manusia yang memiliki sertifikasi verifikasi.",
        "",
        "- Mitigasi Bias & Model Drift:",
        "  Model dievaluasi secara berkala terhadap",
        "  perubahan pola klaim baru dan pembaruan",
        "  regulasi tarif INA-CBG Kemenkes.",
        "",
        "- Transparansi Menyeluruh (No Black-Box):",
        "  Setiap rekomendasi wajib disertai dekomposisi",
        "  SHAP dan dasar pasal regulasi medis baku."
    ]
    gy = card_y + card_h - 70
    for l in lines_gov:
        c.drawString(x2 + 16, gy, l)
        gy -= 13.5

    # Column 3: Akuntabilitas & Audit Trail
    x3 = x2 + col3_w + 16
    draw_card(c, x3, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, x3 + 16, card_y + card_h - 48, col3_w - 32, 34, bg_color=HexColor("#F3E8FF"), border_color=HexColor("#7E22CE"), radius=4)
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawCentredString(x3 + col3_w / 2, card_y + card_h - 32, "AUDIT TRAIL & AKUNTABILITAS")
    
    c.setFont("Helvetica", 8.5)
    c.setFillColor(TEXT_DARK)
    lines_audit = [
        "- Catatan Riwayat Tidak Dapat Diubah:",
        "  Setiap aktivitas penelaahan, skor probabilitas,",
        "  dan keputusan verifikator dicatat dalam audit log",
        "  yang terlindungi dan immutable.",
        "",
        "- Kesiapan Pengawasan BPK RI & KPK RI:",
        "  Dokumentasi audit yang dihasilkan memenuhi",
        "  standar pembuktian administratif dan kepatuhan",
        "  pengawasan tata kelola dana jaminan sosial.",
        "",
        "- Dokumen Audit Berstandar Formal:",
        "  Berita Acara Audit memuat stempel digital,",
        "  nomor dokumen unik, timestamp verifikasi,",
        "  dan QR Code validasi keaslian dokumen.",
        "",
        "- Menjamin Keadilan Bagi Rumah Sakit:",
        "  Faskes memiliki hak klarifikasi berbasis data."
    ]
    ay = card_y + card_h - 70
    for l in lines_audit:
        c.drawString(x3 + 16, ay, l)
        ay -= 13.5


def draw_slide_10_validation_readiness(c):
    """Slide 10: Slide Tambahan - Hasil Uji, Validasi, dan Kesiapan Implementasi strictly according to Page 10."""
    draw_header(c, "Slide Tambahan: Hasil Uji Validasi dan Kesiapan Implementasi", slide_num_label="+", current_slide=10, total_slides=11)
    
    # Left Column: HASIL UJI DAN VALIDASI
    left_w = 460
    draw_card(c, 48, 52, left_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(66, 442, "HASIL UJI DAN VALIDASI (50.000 DATA KLAIM RIIL BPJS)")
    
    # 4 Metric Cards in 2x2
    m_w = (left_w - 32 - 12) / 2.0
    m_h = 70
    
    # Metric 1: ROC-AUC
    draw_card(c, 66, 350, m_w, m_h, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(78, 396, "1.0000")
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(78, 376, "ROC-AUC Score")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(78, 360, "Pemisahan sempurna kelas fraud")

    # Metric 2: Precision
    draw_card(c, 66 + m_w + 12, 350, m_w, m_h, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=6)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(BPJS_BLUE)
    c.drawString(78 + m_w + 12, 396, "99.4%")
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(78 + m_w + 12, 376, "Precision Score")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(78 + m_w + 12, 360, "False positive sangat minimal (<0.6%)")

    # Metric 3: Recall
    draw_card(c, 66, 268, m_w, m_h, bg_color=HexColor("#F3E8FF"), border_color=HexColor("#7E22CE"), radius=6)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawString(78, 314, "98.6%")
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(78, 294, "Recall Score")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(78, 278, "Hampir seluruh fraud terdeteksi")

    # Metric 4: F1-Score
    draw_card(c, 66 + m_w + 12, 268, m_w, m_h, bg_color=ACCENT_AMBER_LIGHT, border_color=ACCENT_AMBER, radius=6)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor("#B7791F"))
    c.drawString(78 + m_w + 12, 314, "0.9900")
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(78 + m_w + 12, 294, "F1-Score Makro")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(78 + m_w + 12, 278, "Keseimbangan presisi & sensitivitas")
    
    # Testing Summary Text
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(TEXT_DARK)
    c.drawString(66, 245, "Ringkasan Hasil Pengujian Terhadap Modus Kecurangan:")
    
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_MUTED)
    val_lines = [
        "- Modus Upcoding: Akurasi deteksi 99.8% pada kasus pemendekan LOS",
        "  dengan klaim Severity Level III (Kompensasi komplikasi berat).",
        "- Modus Unbundling: Keberhasilan 100% mendeteksi pemisahan tindakan",
        "  bedah yang seharusnya masuk dalam satu paket tarif INA-CBG.",
        "- Modus Phantom Billing: Terdeteksi melalui cross-check duplikasi registrasi",
        "  dan inkonsistensi rasio tarif terhadap lama perawatan.",
        "- Uji Stres Kecepatan: 50.000 baris klaim dievaluasi dalam waktu 41 detik",
        "  pada mode batch processing offline."
    ]
    vy = 230
    for vl in val_lines:
        c.drawString(66, vy, vl)
        vy -= 12.5

    # Right Column: KESIAPAN IMPLEMENTASI & RENCANA PENGEMBANGAN
    right_x = 48 + left_w + 16
    right_w = PAGE_WIDTH - 48 - right_x
    
    draw_card(c, right_x, 52, right_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(right_x + 20, 442, "KESIAPAN IMPLEMENTASI & ROADMAP (TRL 6)")
    
    # TRL Level Badge
    draw_card(c, right_x + 16, 365, right_w - 32, 58, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(right_x + 28, 405, "Technology Readiness Level 6 (TRL 6)")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 388, "Prototipe sistem telah diuji coba secara komprehensif pada lingkungan")
    c.drawString(right_x + 28, 374, "operasional relevan menggunakan 50.000 data klaim FKRTL BPJS.")
    
    # Kebutuhan Implementasi
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 20, 345, "Kebutuhan untuk Dipakai di Lapangan:")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_MUTED)
    req_lines = [
        "1. Integrasi API Gateway: Menghubungkan endpoint REST FastAPI",
        "   VeriKlaim dengan pipeline VClaim atau e-Klaim Kemenkes.",
        "2. Skalabilitas Server: Minimal 2 instance vCPU 4-core, RAM 8GB,",
        "   cukup untuk melayani lonjakan verifikasi hingga ribuan klaim/detik.",
        "3. Sertifikasi Verifikator: Pelatihan singkat (1 hari) bagi verifikator",
        "   BPJS dalam membaca interpretasi visual SHAP dan Berita Acara PDF."
    ]
    ry = 330
    for rl in req_lines:
        c.drawString(right_x + 20, ry, rl)
        ry -= 12.5
        
    # Rencana Pengembangan Pasca-Healthkathon
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 20, 240, "Rencana Pengembangan Pasca-Healthkathon:")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_DARK)
    road_lines = [
        "- Tahap 1 (Bulan 1-2): Pilot Project di 5 RSUD mitra Kalbar.",
        "- Tahap 2 (Bulan 3-4): Integrasi modul NLP untuk ekstraksi resume",
        "  medis dan catatan dokter otomatis (OCR berkas rekam medis).",
        "- Tahap 3 (Bulan 5-6): Peluncuran Modul Pre-Audit Mandiri untuk",
        "  manajemen RS seluruh Indonesia guna memangkas klaim dispute.",
        "- Tahap 4: Pembentukan konsorsium riset AI Kesehatan bersama BPJS."
    ]
    rdy = 224
    for rdl in road_lines:
        c.drawString(right_x + 20, rdy, rdl)
        rdy -= 12.5
        
    # Reference citations
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(HexColor("#64748B"))
    c.drawString(right_x + 20, 85, "Referensi Regulasi Utama:")
    c.setFont("Helvetica", 7.5)
    c.drawString(right_x + 20, 72, "1. Permenkes No. 26/2021 tentang Pedoman Tarif Pelayanan Kesehatan JKN")
    c.drawString(right_x + 20, 60, "2. Permenkes No. 16/2019 tentang Pencegahan & Penanganan Kecurangan JKN")


def draw_slide_11_closing(c):
    """Slide 11: Slide Penutup strictly according to Page 11 of template."""
    c.setFillColor(NAVY_DARK)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    
    # Top BPJS Green accent line
    c.setFillColor(BPJS_GREEN)
    c.rect(0, PAGE_HEIGHT - 8, PAGE_WIDTH, 8, fill=True, stroke=False)
    
    # Logo
    logo_path = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\docs\assets\template_p1_img1_Image6.png"
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 48, PAGE_HEIGHT - 85, width=170, height=58, preserveAspectRatio=True, mask='auto')
        
    # Title
    c.setFont("Helvetica-Bold", 30)
    c.setFillColor(WHITE)
    c.drawString(48, PAGE_HEIGHT - 130, "Terima Kasih")
    
    c.setFont("Helvetica", 12)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 156, "Detect Smarter, Protect JKN - Smarter Protection for a Stronger JKN")
    
    c.setFont("Helvetica", 10.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 176, "VeriKlaim: Solusi Deteksi Anomali Klaim FKRTL Berbasis AI & Explainable Governance")
    
    # 3 Large Action Cards
    card_w = (PAGE_WIDTH - 96 - 32) / 3.0
    card_h = 240
    card_y = 65
    
    # Card 1: TAUTAN PROTOTYPE / DEMO
    x1 = 48
    draw_card(c, x1, card_y, card_w, card_h, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_GREEN)
    c.drawString(x1 + 18, card_y + card_h - 28, "TAUTAN PROTOTYPE / DEMO")
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(WHITE)
    c.drawString(x1 + 18, card_y + card_h - 58, "Demo Live Sistem")
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(x1 + 18, card_y + card_h - 85, "http://127.0.0.1:8000")
    
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_LIGHT)
    demo_notes = [
        "- Uvicorn / FastAPI Backend Active",
        "- Interactive Dashboard Verifikator",
        "- Single Claim Anomaly Inspector",
        "- Explainable AI (SHAP Breakdown)",
        "- Generator Laporan Audit PDF Resmi",
        "- Ready for Screen Recording / Zoom"
    ]
    dy = card_y + card_h - 110
    for dn in demo_notes:
        c.drawString(x1 + 18, dy, dn)
        dy -= 15
        
    # Card 2: TAUTAN REPOSITORI
    x2 = x1 + card_w + 16
    draw_card(c, x2, card_y, card_w, card_h, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(x2 + 18, card_y + card_h - 28, "TAUTAN REPOSITORI GITHUB")
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(WHITE)
    c.drawString(x2 + 18, card_y + card_h - 58, "Source Code Lengkap")
    
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(BPJS_BLUE_LIGHT)
    c.drawString(x2 + 18, card_y + card_h - 85, "https://github.com/orochimadit/veri-klaim")
    
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_LIGHT)
    repo_notes = [
        "- Arsitektur Modular (app/, src/, docs/)",
        "- Model Terlatih (models/*.joblib)",
        "- Dataset 50.000 Klaim (data/*.csv)",
        "- Script Training & Evaluasi Lengkap",
        "- Dokumentasi & Proposal PDF Resmi",
        "- Lisensi Open Research & Audit"
    ]
    ry = card_y + card_h - 110
    for rn in repo_notes:
        c.drawString(x2 + 18, ry, rn)
        ry -= 15

    # Card 3: KONTAK TIM
    x3 = x2 + card_w + 16
    draw_card(c, x3, card_y, card_w, card_h, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(HexColor("#C084FC"))
    c.drawString(x3 + 18, card_y + card_h - 28, "KONTAK TIM VERIKLAIM")
    
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(WHITE)
    c.drawString(x3 + 18, card_y + card_h - 58, "Aditya Pratama, S.T., M.T.")
    
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(x3 + 18, card_y + card_h - 85, "Ketua Tim VeriKlaim Kalbar")
    
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_LIGHT)
    contact_notes = [
        "- Dosen Prodi Sistem Informasi,",
        "  Universitas Nahdlatul Ulama Kalbar",
        "- Alumni STEI ITB",
        "- WhatsApp: 0856-5441-1081",
        "- Email: aditya.pratama@unukalbar.ac.id",
        "- Pontianak, Kalimantan Barat"
    ]
    cy = card_y + card_h - 110
    for cn in contact_notes:
        c.drawString(x3 + 18, cy, cn)
        cy -= 15

    # Bottom footer text
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#64748B"))
    c.drawString(48, 30, "Project Final Healthkathon 2026 BPJS Kesehatan - Kategori Efisiensi Risiko pada Faskes / KLAIM (C03.04)")


def main():
    output_pdf = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\docs\Project_Final_Healthkathon_2026_VeriKlaim.pdf"
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)
    
    c = canvas.Canvas(output_pdf, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    
    # Slide 1: Cover
    draw_slide_1_cover(c)
    c.showPage()
    
    # Slide 2: Perkenalan Tim (Sesuai slide 4 template)
    draw_slide_2_team(c)
    c.showPage()
    
    # Slide 3: Judul Ide, Deskripsi, dan Tujuan (Sesuai slide 5 template)
    draw_slide_3_idea(c)
    c.showPage()
    
    # Slide 4: Latar Belakang dan Dampak (Sesuai slide 6 template)
    draw_slide_4_background_impact(c)
    c.showPage()
    
    # Slide 5: Alur Proses Aplikasi (Sesuai slide 7 template)
    draw_slide_5_process_flow(c)
    c.showPage()
    
    # Slide 6: Demo Aplikasi / Prototype (Sesuai slide 8 template)
    draw_slide_6_demo_prototype(c)
    c.showPage()
    
    # Slide 7: Penjelasan Fitur (Sesuai slide 9 template)
    draw_slide_7_features(c)
    c.showPage()
    
    # Slide 8: Slide Tambahan - Arsitektur Teknis dan Data (Sesuai slide 10 template)
    draw_slide_8_architecture(c)
    c.showPage()
    
    # Slide 9: Slide Tambahan - Keamanan, Privasi, dan Tata Kelola AI (Sesuai slide 10 template)
    draw_slide_9_governance(c)
    c.showPage()
    
    # Slide 10: Slide Tambahan - Hasil Uji Validasi dan Kesiapan Implementasi (Sesuai slide 10 template)
    draw_slide_10_validation_readiness(c)
    c.showPage()
    
    # Slide 11: Slide Penutup (Sesuai slide 11 template)
    draw_slide_11_closing(c)
    c.showPage()
    
    c.save()
    print(f"SUCCESS: Generated {output_pdf} with 11 slides strictly following Panduan Project Final Healthkathon 2026!")


if __name__ == "__main__":
    main()
