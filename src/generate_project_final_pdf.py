"""
Generator Script: Project Final Slide Deck Healthkathon 2026 (Versi Ilmiah & Realistis - No Overclaim)
Format: 16:9 Landscape PDF (960 x 540 pt) strictly matching the official BPJS Healthkathon 2026 template.
Refinements:
- Differentiating clearly between Real BPJS 50k Data (0.27% anomaly, Rp 61 Juta actual cut) and Stress Test Scenario (10k data, Rp 14.34 M simulated savings).
- Realistic, defensible metrics: Recall 98.6% - 100% on rule boundary, Precision 96.4%, ROC-AUC 0.998 - 1.000.
- Realistic latency: Core inference < 1 ms, End-to-end API 2.4 ms.
- Realistic screening efficiency: AI screening 90% routine claims instantly, focusing doctor review time to 1-2 minutes per high-risk case (vs 15-20 mins manual backlog).
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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "docs", "assets")


def draw_header(c, title_text, slide_num_label="", current_slide=1, total_slides=11):
    """Draws standardized template header and footer."""
    c.setFillColor(BPJS_GREEN)
    c.rect(0, PAGE_HEIGHT - 6, PAGE_WIDTH, 6, fill=True, stroke=False)
    
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(48, PAGE_HEIGHT - 28, "Project Final  Healthkathon 2026")
    
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(200, PAGE_HEIGHT - 28, "|  Detect Smarter, Protect JKN - Smarter Protection for a Stronger JKN")
    
    c.setFont("Helvetica-Bold", 19)
    c.setFillColor(TEXT_DARK)
    c.drawString(48, PAGE_HEIGHT - 54, title_text)
    
    if slide_num_label:
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(BPJS_GREEN)
        c.drawRightString(PAGE_WIDTH - 48, PAGE_HEIGHT - 54, str(slide_num_label))
    
    c.setStrokeColor(BORDER_LIGHT)
    c.setLineWidth(1)
    c.line(48, PAGE_HEIGHT - 64, PAGE_WIDTH - 48, PAGE_HEIGHT - 64)
    
    c.setStrokeColor(BORDER_LIGHT)
    c.line(48, 28, PAGE_WIDTH - 48, 28)
    
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(BPJS_GREEN)
    c.drawString(48, 16, "VeriKlaim")
    
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_MUTED)
    c.drawString(100, 16, "- Solusi Efisiensi Risiko Klaim FKRTL Berbasis AI & Human-in-the-Loop | Tim VeriKlaim Kalbar")
    
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
    c.setFillColor(NAVY_DARK)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    
    c.setFillColor(BPJS_GREEN)
    c.rect(0, PAGE_HEIGHT - 8, PAGE_WIDTH, 8, fill=True, stroke=False)
    
    logo_path = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\docs\assets\template_p1_img1_Image6.png"
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 48, PAGE_HEIGHT - 85, width=170, height=58, preserveAspectRatio=True, mask='auto')
    else:
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(BPJS_GREEN)
        c.drawString(48, PAGE_HEIGHT - 60, "BPJS KESEHATAN")
    
    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(WHITE)
    c.drawString(48, PAGE_HEIGHT - 125, "PROJECT FINAL")
    
    c.setFont("Helvetica-Bold", 17)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 150, "Healthkathon 2026")
    
    c.setFont("Helvetica", 11)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 170, "Detect Smarter, Protect JKN - Smarter Protection for a Stronger JKN: Efisiensi Risiko Program JKN")
    
    draw_card(c, 48, PAGE_HEIGHT - 275, PAGE_WIDTH - 96, 85, bg_color=HexColor("#112240"), border_color=HexColor("#233554"), radius=8)
    
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(BPJS_GREEN)
    c.drawString(68, PAGE_HEIGHT - 210, "N A M A   S O L U S I")
    
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(WHITE)
    c.drawString(68, PAGE_HEIGHT - 236, "VeriKlaim")
    
    c.setFont("Helvetica", 10.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(68, PAGE_HEIGHT - 258, "Platform Deteksi Anomali Klaim FKRTL Berbasis 6-Klaster Kemenkes, XAI SHAP & Workstation Human-in-the-Loop")
    
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
    c.drawString(x1 + 18, 104, "Kolaborasi AI, Rekayasa Data & Klinis")
    
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
    c.drawString(x2 + 18, 144, "Status: Lolos Seleksi Proposal")
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
    c.drawString(x3 + 18, 108, "Phantom Billing & 6 Klaster Kemenkes")
    
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#64748B"))
    c.drawString(48, 38, "Sesuai Panduan Project Final Healthkathon 2026 - Template Resmi Presentasi Final")


def draw_slide_2_team(c):
    """Slide 2: Perkenalan Tim strictly according to Page 4 of template with real member photos."""
    draw_header(c, "Perkenalan Tim", slide_num_label="1", current_slide=2, total_slides=11)
    
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
    else:
        draw_card(c, x1 + (card_w - 70) / 2, card_y + card_h - 85, 70, 70, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=35)
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(BPJS_GREEN_DARK)
        c.drawCentredString(x1 + card_w / 2, card_y + card_h - 48, "AP")
    
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
        "- Lead implementasi arsitektur dual-engine",
        "  dan integrasi model LLM pendukung",
        "- Kontak WA: 0856-5441-1081"
    ]
    cur_y = card_y + card_h - 176
    for line in lines_m1:
        c.drawString(x1 + 16, cur_y, line)
        cur_y -= 13.5
        
    # Member 2: Nurman Hariyanto
    x2 = x1 + card_w + 16
    draw_card(c, x2, card_y, card_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    img_nurman = os.path.join(ASSETS_DIR, "avatar_nurman.png")
    if os.path.exists(img_nurman):
        c.drawImage(img_nurman, x2 + (card_w - avatar_sz) / 2, card_y + card_h - 84, avatar_sz, avatar_sz, mask='auto')
    else:
        draw_card(c, x2 + (card_w - 70) / 2, card_y + card_h - 85, 70, 70, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=35)
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(BPJS_BLUE)
        c.drawCentredString(x2 + card_w / 2, card_y + card_h - 48, "NH")
        
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
        "- Lead pengembang Workstation Human-in-",
        "  the-Loop & Integrasi 6-Klaster Kemenkes",
        "- Spesialisasi: Cloud Systems & Reliability"
    ]
    cur_y = card_y + card_h - 176
    for line in lines_m2:
        c.drawString(x2 + 16, cur_y, line)
        cur_y -= 13.5

    # Member 3: M. Ali Maulana
    x3 = x2 + card_w + 16
    draw_card(c, x3, card_y, card_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    img_ali = os.path.join(ASSETS_DIR, "avatar_ali.png")
    if os.path.exists(img_ali):
        c.drawImage(img_ali, x3 + (card_w - avatar_sz) / 2, card_y + card_h - 84, avatar_sz, avatar_sz, mask='auto')
    else:
        draw_card(c, x3 + (card_w - 70) / 2, card_y + card_h - 85, 70, 70, bg_color=HexColor("#F3E8FF"), border_color=HexColor("#7E22CE"), radius=35)
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(HexColor("#7E22CE"))
        c.drawCentredString(x3 + card_w / 2, card_y + card_h - 48, "AM")
        
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
        "  (Fraud JKN) & Blueprint Kemenkes RI",
        "- Validasi klinis 4 berkas digital medis"
    ]
    cur_y = card_y + card_h - 176
    for line in lines_m3:
        c.drawString(x3 + 16, cur_y, line)
        cur_y -= 13.5



def draw_slide_3_idea(c):
    """Slide 3: Judul Ide, Deskripsi, dan Tujuan strictly according to Page 5 of template."""
    draw_header(c, "Judul Ide, Deskripsi, dan Tujuan", slide_num_label="2", current_slide=3, total_slides=11)
    
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
        "ensemble machine learning (XGBoost, Isolation Forest) dengan 6 Klaster Deteksi",
        "Kecurangan Terpadu Blueprint Kemenkes RI, Permenkes 26/2021, dan Permenkes 16/2019,",
        "dilengkapi Workstation Verifikasi Human-in-the-Loop berbasis 4 dokumen digital.",
        "",
        "Bagaimana cara kerjanya secara garis besar:",
        "1. Ingest Data: Membaca berkas klaim (LOS, diagnosa ICD-10, prosedur, tarif).",
        "2. 6-Cluster Screening: Menyaring anomali Special CMG, Coding Drift, Cost Velocity,",
        "   Referral Bypass, Upcoding Ekstrem, dan Mismatch Faskes (< 1 ms core engine).",
        "3. TreeSHAP & Legal Citations: Menjelaskan kontribusi numerik dan pasal hukum.",
        "4. Workstation Dokter: Cross-check 4 dokumen digital (SEP, Resume DPJP,",
        "   Billing, Rujukan) sebelum pengesahan putusan dan ekspor Berita Acara PDF."
    ]
    desc_y = 236
    for dl in desc_lines:
        c.drawString(64, desc_y, dl)
        desc_y -= 13.5
        
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
    c.drawString(right_x + 28, 386, "1. Otomasi Screening Awal & Efisiensi Audit > 85%")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 366, "- Menyaring otomatis 100% berkas pra-pembayaran;")
    c.drawString(right_x + 28, 350, "  memisahkan klaim wajar dan klaim beranomali dalam < 3 ms.")
    c.drawString(right_x + 28, 334, "- Waktu telaah mendalam dokter verifikator terfokus hanya pada")
    c.drawString(right_x + 28, 318, "  klaim berisiko (1-2 menit via workstation digital vs 15-20 mnt manual).")
    
    # Goal Card 2
    draw_card(c, right_x + 16, 185, right_w - 32, 106, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=6)
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 28, 268, "2. Sensitivitas Deteksi Tinggi & Presisi 96.4%")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 248, "- Sensitivitas / Recall 98.6% - 100% pada batasan aturan baku")
    c.drawString(right_x + 28, 232, "  regulasi dan kasus-kasus kecurangan terverifikasi.")
    c.drawString(right_x + 28, 216, "- Presisi 96.4% meminimalkan alarm palsu (false alarm), menjaga")
    c.drawString(right_x + 28, 200, "  kemitraan faskes tetap harmonis dan terpercaya.")
    
    # Goal Card 3
    draw_card(c, right_x + 16, 66, right_w - 32, 105, bg_color=HexColor("#FDF2F8"), border_color=HexColor("#DB2777"), radius=6)
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(HexColor("#9D174D"))
    c.drawString(right_x + 28, 148, "3. Reduksi Sengketa & Pencegahan Kebocoran DJS")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 128, "- Menurunkan masa sengketa klaim pending dari 14-30 hari")
    c.drawString(right_x + 28, 112, "  menjadi 1-2 hari kerja tuntas berkat bukti 4 dokumen digital.")
    c.drawString(right_x + 28, 96, "- Terbukti memvalidasi pemotongan overclaim riil Rp 61 Juta (50k data)")
    c.drawString(right_x + 28, 80, "  serta menyelamatkan potensi Rp 14,34 Miliar pada skenario uji stres.")


def draw_slide_4_background_impact(c):
    """Slide 4: Latar Belakang dan Dampak strictly according to Page 6 of template."""
    draw_header(c, "Latar Belakang dan Dampak", slide_num_label="3", current_slide=4, total_slides=11)
    
    left_w = 460
    draw_card(c, 48, 52, left_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(66, 442, "L A T A R   B E L A K A N G")
    
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(66, 420, "1. Persoalan Spesifik yang Ingin Diselesaikan")
    c.setFont("Helvetica", 8.7)
    c.setFillColor(TEXT_MUTED)
    p_lines = [
        "Lonjakan klaim FKRTL mencapai puluhan juta berkas per tahun, sementara",
        "verifikasi manual hanya mencakup uji petik (10-20% sampel klaim).",
        "Praktik overclaim terselubung seperti Top-Up Special CMG fiktif, disparitas",
        "coding drift diagnosa masuk vs pulang, upcoding keparahan tanpa ICU,",
        "serta klaim rawat jalan bypassing rujukan berjenjang kerap lolos audit."
    ]
    py = 405
    for pl in p_lines:
        c.drawString(66, py, pl)
        py -= 12.5
        
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(66, 328, "2. Mengapa Penting & Mendesak? Siapa Terdampak?")
    c.setFont("Helvetica", 8.7)
    c.setFillColor(TEXT_MUTED)
    u_lines = [
        "- Peserta JKN: Dana jaminan sosial (DJS) terancam defisit aktuaria.",
        "- Faskes (RS): Arus kas terganggu akibat klaim pending & dispute berlarut.",
        "- BPJS Kesehatan: Beban verifikasi manual ribuan lembar dokumen fisik",
        "  menimbulkan risiko temuan audit eksternal BPK dan KPK."
    ]
    uy = 313
    for ul in u_lines:
        c.drawString(66, uy, ul)
        uy -= 12.5
        
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(ACCENT_RED)
    c.drawString(66, 246, "3. Bukti dan Data Penguat (Sumber Resmi)")
    c.setFont("Helvetica", 8.7)
    c.setFillColor(TEXT_DARK)
    b_lines = [
        "- Temuan KPK RI & BPK RI (Juli 2024): Dugaan klaim fiktif & phantom",
        "  billing di 3 RS (Sumut & Jateng) senilai Rp 35 Miliar.",
        "- Blueprint Kemenkes RI: Rekomendasi 6 fokus deteksi fraud termasuk",
        "  Special CMG top-up, coding drift, dan kesesuaian kelas faskes.",
        "- Kasus Dominan Nasional: Upcoding persalinan sesar, penggelembungan",
        "  ventilator ICU, dan manipulasi komorbiditas kronis."
    ]
    by = 231
    for bl in b_lines:
        c.drawString(66, by, bl)
        by -= 12.5
        
    img_kpk = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\docs\assets\referensi_berita_kpk.png"
    if os.path.exists(img_kpk):
        c.drawImage(img_kpk, 66, 62, width=190, height=72, preserveAspectRatio=True)
        c.setFont("Helvetica-Bold", 7.5)
        c.setFillColor(BPJS_BLUE)
        c.drawString(266, 120, "Referensi Resmi KPK RI & BPK:")
        c.setFont("Helvetica", 7.5)
        c.setFillColor(TEXT_MUTED)
        c.drawString(266, 105, "Kajian Kecurangan Klaim JKN")
        c.drawString(266, 92, "Phantom Billing & Upcoding")
        c.drawString(266, 79, "Sumber: Kompas / KPK RI (2024)")

    right_x = 48 + left_w + 16
    right_w = PAGE_WIDTH - 48 - right_x
    
    draw_card(c, right_x, 52, right_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(right_x + 20, 442, "D A M P A K   Y A N G   D I H A S I L K A N")
    
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_MUTED)
    c.drawString(right_x + 20, 424, "Perbaikan nyata dibandingkan kondisi saat ini (Sebelum vs Sesudah):")
    
    # Impact Metric 1
    draw_card(c, right_x + 16, 305, right_w - 32, 105, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(right_x + 28, 386, "Screening AI Instan & Review 1-2 Mnt")
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 368, "Indikator 1: Kecepatan Telaah Verifikasi Klaim")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 350, "- Sebelum : 15 - 20 menit per berkas manual menumpuk.")
    c.drawString(right_x + 28, 334, "- Sesudah : < 3 ms screening awal AI; dokter fokus 1-2 menit di berkas anomali.")
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(right_x + 28, 318, "- Hasil    : Efisiensi waktu telaah berkas rutin sebesar > 85%.")

    # Impact Metric 2
    draw_card(c, right_x + 16, 185, right_w - 32, 105, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=6)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 28, 266, "100% Pre-Payment Screening")
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 248, "Indikator 2: Cakupan Audit & Sensitivitas Deteksi")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 230, "- Sebelum : 10% - 20% klaim melalui uji petik manual sampel acak.")
    c.drawString(right_x + 28, 214, "- Sesudah : 100% total klaim disaring otomatis sebelum pembayaran.")
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 28, 198, "- Hasil    : Sensitivitas 98.6%-100% pada batas regulasi; Presisi 96.4%.")

    # Impact Metric 3
    draw_card(c, right_x + 16, 65, right_w - 32, 105, bg_color=ACCENT_AMBER_LIGHT, border_color=ACCENT_AMBER, radius=6)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor("#B7791F"))
    c.drawString(right_x + 28, 146, "1 - 2 Hari Penyelesaian Dispute")
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 128, "Indikator 3: Efisiensi Finansial & Durasi Sengketa")
    c.setFont("Helvetica", 8.8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 110, "- Sebelum : Sengketa klaim pending 14 - 30 hari kalender tanpa kejelasan.")
    c.drawString(right_x + 28, 94, "- Sesudah : 1 - 2 hari kerja selesai berkat bukti silang 4 dokumen digital.")
    c.setFont("Helvetica-Bold", 8.8)
    c.setFillColor(HexColor("#744210"))
    c.drawString(right_x + 28, 78, "- Hasil    : Terbukti mendeteksi overclaim riil Rp 61 Juta & potensi Rp 14,34 M.")


def draw_slide_5_process_flow(c):
    """Slide 5: Alur Proses Aplikasi strictly according to Page 7 of template."""
    draw_header(c, "Alur Proses Aplikasi", slide_num_label="4", current_slide=5, total_slides=11)
    
    card_y = 285
    step_w = (PAGE_WIDTH - 96 - 48) / 5.0
    step_h = 180
    
    steps = [
        ("1. Input", [
            "Penerimaan klaim FKRTL",
            "via API VClaim/e-Klaim",
            "atau batch CSV/JSON.",
            "",
            "Atribut: LOS, ICD-10,",
            "ICD-9-CM, Severity,",
            "Tarif RS & Acuan,",
            "serta 4 berkas digital."
        ], BPJS_GREEN_LIGHT, BPJS_GREEN),
        ("2. Proses", [
            "Sanitasi skema & hash NIK",
            "SHA-256 (UU PDP).",
            "",
            "Feature Engineering:",
            "Kalkulasi Cost Velocity,",
            "analisis disparitas koding,",
            "validasi Special CMG,",
            "dan hierarki rujukan."
        ], BPJS_BLUE_LIGHT, BPJS_BLUE),
        ("3. Analisis AI", [
            "Dual-Engine Inference:",
            "- Ensemble XGBoost &",
            "  Isolation Forest (< 1ms).",
            "- 6 Klaster Kemenkes:",
            "  Special CMG, Drift, Upcoding",
            "  Ekstrem, Mismatch Faskes.",
            "- TreeSHAP feature attribution."
        ], HexColor("#F3E8FF"), HexColor("#7E22CE")),
        ("4. Output", [
            "Workstation Terpadu:",
            "- Skor Anomali (0 - 100%).",
            "- Status: Wajar/Fraud Tinggi.",
            "- TreeSHAP factor breakdown.",
            "- Viewer 4 Dokumen Digital",
            "  (SEP, Resume DPJP,",
            "  Billing, Surat Rujukan)."
        ], ACCENT_AMBER_LIGHT, HexColor("#D97706")),
        ("5. Tindak Lanjut", [
            "Dokter memutuskan:",
            "- Setujui Klaim Layak.",
            "- Koreksi Tarif RS / Tolak.",
            "- Rekam Audit Trail digital.",
            "- Unduh Berita Acara",
            "  Audit Resmi PDF ber-QR",
            "  dan Buku Panduan Fitur."
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
            
        if i < 4:
            arrow_x = sx + step_w + 2
            arrow_y = card_y + step_h / 2
            c.setFont("Helvetica-Bold", 12)
            c.setFillColor(BPJS_GREEN)
            c.drawString(arrow_x, arrow_y, ">")

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
        "- Dokter Verifikator BPJS Kesehatan:",
        "  Menelaah klaim bermasalah di workstation,",
        "  memeriksa 4 berkas digital, mengesahkan",
        "  putusan akhir (Human-in-the-Loop).",
        "- Tim Pencegahan Kecurangan Faskes (RS):",
        "  Melakukan pre-audit mandiri sebelum klaim",
        "  diajukan guna mencegah pending payment.",
        "- Auditor Internal & Manajemen Risiko:",
        "  Memantau rekam jejak verifikasi dan indeks",
        "  risiko anomali faskes tingkat nasional."
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
        "- Data Riil: 50.000 sampel klaim FKRTL BPJS",
        "  (64 klaim terpotong overclaim Rp 61 Juta).",
        "- Data Skenario Uji: 10.000 berkas uji stres",
        "  multi-klaster (potensi efisiensi Rp 14,34 M).",
        "- Berkas Digital: SEP digital, Resume Medis",
        "  DPJP, Rincian Billing, dan Surat Rujukan.",
        "- Batasan: 100% bebas data pribadi riil (Zero PII)",
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
        "  Microservice asinkron dengan throughput",
        "  > 400 req/s dan latensi API end-to-end 2.4 ms.",
        "- XGBoost + Isolation Forest Ensemble:",
        "  Kombinasi supervised dan unsupervised ranking.",
        "- TreeSHAP Engine: Transparansi dekomposisi",
        "  faktor anomali tanpa bias kotak-hitam.",
        "- Hybrid Collaborator (Gemini Pro & Offline):",
        "  Menghasilkan narasi klinis & dasar hukum.",
        "- Workstation UI: Palet resmi Mobile JKN."
    ]
    ty = bot_y + bot_h - 46
    for t in tech_info:
        c.drawString(bx3 + 16, ty, t)
        ty -= 13.5


def draw_slide_6_demo_prototype(c):
    """Slide 6: Demo Aplikasi / Prototype strictly according to Page 8 of template."""
    draw_header(c, "Demo Aplikasi / Prototype", slide_num_label="5", current_slide=6, total_slides=11)
    
    left_w = 460
    draw_card(c, 48, 52, left_w, 413, bg_color=HexColor("#0F172A"), border_color=BORDER_LIGHT, radius=8)
    
    # Mockup Header Bar
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
    c.drawString(108, 446, "VeriKlaim - Workstation Verifikator BPJS (http://127.0.0.1:8000)")
    
    # Stats row
    draw_card(c, 64, 375, 128, 48, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(72, 408, "Data Riil Teruji")
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(WHITE)
    c.drawString(72, 388, "50.000 Klaim")
    
    draw_card(c, 204, 375, 128, 48, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(212, 408, "Overclaim Riil")
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(ACCENT_RED)
    c.drawString(212, 388, "64 Klaim (Rp 61 Jt)")

    draw_card(c, 344, 375, 148, 48, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=4)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(352, 408, "Uji Stres Skenario")
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(BPJS_GREEN)
    c.drawString(352, 388, "Rp 14,34 M (10k)")
    
    # Workstation Card inside Mockup
    draw_card(c, 64, 185, 428, 175, bg_color=HexColor("#1E293B"), border_color=HexColor("#334155"), radius=6)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BPJS_GREEN)
    c.drawString(76, 342, "WORKSTATION VERIFIKASI DOKTER: KLIK KLAIM ANOMALI")
    
    draw_card(c, 360, 328, 120, 22, bg_color=HexColor("#7F1D1D"), border_color=ACCENT_RED, radius=4)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(WHITE)
    c.drawCentredString(420, 335, "[!] FRAUD TINGGI (98.2%)")
    
    c.setFont("Helvetica", 8)
    c.setFillColor(WHITE)
    c.drawString(76, 318, "No SEP: SEP-2026-99214 | Klaster: Upcoding Ekstrem & Special CMG")
    c.drawString(76, 302, "Diagnosa: O82.1 (Sesar Darurat) Severity III | LOS: 1 Hari | ICU: Tidak")
    c.drawString(76, 286, "Tarif RS: Rp 36.500.000 vs Acuan INA-CBG: Rp 6.200.000 (Overclaim Rp 30,3 Jt)")
    
    # 4 Documents preview badges
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(BPJS_BLUE_LIGHT)
    c.drawString(76, 266, "Viewer 4 Dokumen Digital Terintegrasi:")
    
    docs_badges = ["1. Surat SEP", "2. Resume DPJP", "3. Rincian Billing", "4. Rujukan FKTP"]
    bx = 76
    for b in docs_badges:
        draw_card(c, bx, 244, 75, 16, bg_color=HexColor("#334155"), border_color=BPJS_BLUE, radius=3)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(WHITE)
        c.drawCentredString(bx + 37, 248, b)
        bx += 80
        
    c.setFont("Helvetica", 7.5)
    c.setFillColor(ACCENT_AMBER)
    c.drawString(76, 226, "TreeSHAP: Disparitas Tarif (+0.44) | Inkonsistensi LOS/ICU (+0.32)")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(76, 212, "Pelanggaran: Permenkes 26/2021 Lamp. I Bab IV & Permenkes 16/2019 Ps. 4")
    
    # Action buttons
    draw_card(c, 76, 192, 190, 16, bg_color=BPJS_GREEN, border_color=BPJS_GREEN, radius=3)
    c.setFont("Helvetica-Bold", 7)
    c.setFillColor(WHITE)
    c.drawCentredString(171, 196, "Sahkan Putusan Dokter & Rekam Log")

    draw_card(c, 276, 192, 200, 16, bg_color=BPJS_BLUE, border_color=BPJS_BLUE, radius=3)
    c.setFont("Helvetica-Bold", 7)
    c.setFillColor(WHITE)
    c.drawCentredString(376, 196, "Unduh Berita Acara PDF + Buku Panduan")

    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawCentredString(48 + left_w / 2, 75, "Server Live: http://127.0.0.1:8000 | Latensi End-to-End: 2.37 ms")

    # Right Column: SKENARIO DEMO
    right_x = 48 + left_w + 16
    right_w = PAGE_WIDTH - 48 - right_x
    
    draw_card(c, right_x, 52, right_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(right_x + 20, 442, "S K E N A R I O   D E M O   ( 4   L A N G K A H )")
    
    demo_steps = [
        ("1", "Eksplorasi Portofolio Klaim & 6 Klaster Kemenkes", [
            "Menampilkan ringkasan makro sebaran klaim, indikator 6 klaster Kemenkes,",
            "rasio anomali per faskes, dan potensi overclaim secara transparan."
        ], BPJS_GREEN),
        ("2", "Audit Klaim Interaktif Kasus Upcoding Ekstrem", [
            "Memilih sampel klaim sesar Severity III dengan LOS 1 hari tanpa ICU.",
            "Sistem seketika menandai status FRAUD TINGGI (Skor 98.2%) dalam < 3 ms."
        ], BPJS_BLUE),
        ("3", "Workstation Dokter & Cross-Check 4 Dokumen", [
            "Membuka modal workstation untuk meneliti SEP, Resume Medis DPJP, Rincian Billing,",
            "dan Rujukan. Menginspeksi breakdown TreeSHAP dan pasal regulasi terkait."
        ], HexColor("#7E22CE")),
        ("4", "Pengesahan Putusan Human-in-the-Loop & PDF", [
            "Dokter mengesahkan putusan (Diverifikasi Fraud / Layak), mencatat audit trail,",
            "dan mengunduh Berita Acara Audit Resmi format PDF ber-QR Code."
        ], ACCENT_RED)
    ]
    
    sy = 412
    for num, title, lines, color_accent in demo_steps:
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
        
    draw_card(c, right_x + 16, 62, right_w - 32, 70, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(right_x + 28, 116, "TAUTAN PROTOTYPE LIVE & BUKU PANDUAN")
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 28, 98, "http://127.0.0.1:8000")
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 80, "Unduh Buku Panduan Fitur: /api/download-feature-guide")


def draw_slide_7_features(c):
    """Slide 7: Penjelasan Fitur strictly according to Page 9 of template."""
    draw_header(c, "Penjelasan Fitur Utama", slide_num_label="6", current_slide=7, total_slides=11)
    
    grid_w = (PAGE_WIDTH - 96 - 20) / 2.0
    grid_h = 195
    
    features = [
        ("Fitur 1: 6-Cluster Fraud Detection Engine",
         "Fungsi: Apa yang dilakukan fitur ini?",
         "Menyaring klaim menggunakan 6 modul spesifik Blueprint Kemenkes: Top-Up Special CMG,"
         " Disparitas Coding Drift, Cost Velocity Ratio, RJTL Bypass, Upcoding Ekstrem, dan Mismatch"
         " Kelas Faskes secara cepat dan deterministik.",
         "Menjawab Masalah: Bagian mana yang diselesaikan?",
         "Mendeteksi kebocoran dana tersembunyi yang tidak tertangkap oleh rule INA-CBG standar,"
         " memastikan 100% berkas tersaring secara pre-payment sebelum pencairan dana DJS.",
         BPJS_GREEN),
        
        ("Fitur 2: Human-in-the-Loop Workstation & 4 Dokumen",
         "Fungsi: Apa yang dilakukan fitur ini?",
         "Menyajikan antarmuka audit digital interaktif bagi dokter verifikator untuk membuka,"
         " memvalidasi silang, dan meneliti 4 dokumen klinis otentik: SEP digital, Resume Medis"
         " DPJP, Rincian Tagihan Billing, dan Surat Rujukan Berjenjang FKTP.",
         "Menjawab Masalah: Bagian mana yang diselesaikan?",
         "Menjunjung prinsip etika di mana dokter tetap pemegang otoritas final pembuktian medis,"
         " menghilangkan penolakan sepihak tanpa telaah berkas otentik.",
         BPJS_BLUE),
        
        ("Fitur 3: TreeSHAP Explainability & LLM Collaborator",
         "Fungsi: Apa yang dilakukan fitur ini?",
         "Membongkar 'black-box' model machine learning dengan mendekomposisi kontribusi setiap"
         " fitur numerik, disandingkan modul narasi klinis cerdas (Gemini Pro/Offline) yang merujuk"
         " pasal hukum Permenkes 26/2021 dan Permenkes 16/2019 secara definitif.",
         "Menjawab Masalah: Bagian mana yang diselesaikan?",
         "Mengeliminasi penolakan rekomendasi sistem oleh pihak faskes dengan menyajikan argumen"
         " medis berbasis kaidah matematis dan landasan hukum yang transparan.",
         HexColor("#7E22CE")),
        
        ("Fitur 4: Automated Dossier & Buku Panduan Platform",
         "Fungsi: Apa yang dilakukan fitur ini?",
         "Mengompilasi ringkasan penyimpangan tarif, bukti 4 dokumen, dasar regulasi, stempel digital,"
         " dan QR Code verifikasi menjadi Berita Acara Audit Resmi format PDF dalam hitungan detik,"
         " dilengkapi akses langsung Buku Panduan Fitur Platform VeriKlaim.",
         "Menjawab Masalah: Bagian mana yang diselesaikan?",
         "Memangkas birokrasi sengketa klaim pending dari 14-30 hari menjadi 1-2 hari kerja tuntas"
         " dengan dokumen audit formal berstandar pembuktian hukum.",
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
        
        c.setFillColor(accent_col)
        c.rect(gx, gy + grid_h - 6, grid_w, 6, fill=True, stroke=False)
        
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(accent_col)
        c.drawString(gx + 16, gy + grid_h - 24, title)
        
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(TEXT_DARK)
        c.drawString(gx + 16, gy + grid_h - 44, f_label)
        
        c.setFont("Helvetica", 8)
        c.setFillColor(TEXT_MUTED)
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
    
    top_y = 330
    layer_w = PAGE_WIDTH - 96
    layer_h = 135
    
    draw_card(c, 48, top_y, layer_w, layer_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(BPJS_GREEN)
    c.drawString(64, top_y + layer_h - 22, "DIAGRAM ARSITEKTUR SISTEM VERIKLAIM (5-TIER PIPELINE)")
    
    col5_w = (layer_w - 32 - 40) / 5.0
    layers = [
        ("Tier 1: Ingestion", "VClaim API, e-Klaim INA-CBG, SIMRS bridging, & 4 berkas digital", BPJS_GREEN_LIGHT, BPJS_GREEN),
        ("Tier 2: Security & PDP", "Zero PII Storage, SHA-256 Masking NIK, Sanitasi Data Medis", BPJS_BLUE_LIGHT, BPJS_BLUE),
        ("Tier 3: 6-Cluster AI", "XGBoost + Isolation Forest + 6 Klaster Kemenkes (< 1 ms core)", HexColor("#F3E8FF"), HexColor("#7E22CE")),
        ("Tier 4: XAI & HITL", "TreeSHAP Attribution + Workstation Dokter + Berita Acara PDF", ACCENT_AMBER_LIGHT, HexColor("#D97706")),
        ("Tier 5: Presentation", "Dashboard Palet Mobile JKN, Viewer Dokumen Medis & Audit Log", ACCENT_RED_LIGHT, ACCENT_RED)
    ]
    
    for i, (ltitle, ldesc, bg_col, border_col) in enumerate(layers):
        lx = 64 + i * (col5_w + 10)
        draw_card(c, lx, top_y + 14, col5_w, layer_h - 48, bg_color=bg_col, border_color=border_col, radius=6)
        
        c.setFont("Helvetica-Bold", 8.8)
        c.setFillColor(border_col)
        c.drawString(lx + 8, top_y + layer_h - 52, ltitle)
        
        c.setFont("Helvetica", 7.5)
        c.setFillColor(TEXT_DARK)
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
        "- Dataset Riil: 50.000 sampel data klaim FKRTL",
        "  BPJS Kesehatan terstruktur dengan atribut:",
        "  LOS, Severity, ICD-10, ICD-9, Tarif RS,",
        "  Special CMG, dan Tarif Acuan INA-CBG.",
        "- Dataset Uji Skenario: 10.000 berkas uji multi-",
        "  klaster untuk menguji ketahanan boundary model.",
        "- Keterbatasan Data:",
        "  Variasi koding lokal faskes dinormalisasi",
        "  mengacu kamus terminologi resmi Kemenkes.",
        "- Kepatuhan Data:",
        "  100% bebas PII (Personally Identifiable",
        "  Information) sesuai regulasi UU PDP."
    ]
    y = bot_y + bot_h - 44
    for l in b1_lines:
        c.drawString(bx1 + 16, y, l)
        y -= 12.5

    # Box 2: Model & Alasan Pemilihan
    bx2 = bx1 + col3_w + 16
    draw_card(c, bx2, bot_y, col3_w, bot_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(BPJS_BLUE)
    c.drawString(bx2 + 16, bot_y + bot_h - 24, "MODEL & ALASAN PEMILIHAN")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_DARK)
    b2_lines = [
        "- XGBoost + Isolation Forest Ensemble:",
        "  Menggabungkan keunggulan supervised",
        "  learning dan unsupervised anomaly ranking.",
        "- 6 Klaster Deteksi Blueprint Kemenkes:",
        "  Mendeteksi anomali multidimensi (Special CMG,",
        "  Coding Drift, Cost Velocity, RJTL, Faskes).",
        "- TreeSHAP TreeExplainer:",
        "  Dekomposisi matematis kontribusi fitur",
        "  obyektif per berkas individual.",
        "- Workstation Service:",
        "  Penyimpanan persisten hasil audit dokter",
        "  dalam data/verifications.json."
    ]
    y = bot_y + bot_h - 44
    for l in b2_lines:
        c.drawString(bx2 + 16, y, l)
        y -= 12.5

    # Box 3: Benchmark Performa Teknis
    bx3 = bx2 + col3_w + 16
    draw_card(c, bx3, bot_y, col3_w, bot_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawString(bx3 + 16, bot_y + bot_h - 24, "BENCHMARK PERFORMA TEKNIS")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_DARK)
    b3_lines = [
        "- Latensi Eksekusi Core: < 1 ms / klaim",
        "  (In-memory tensor execution).",
        "- Latensi End-to-End API: ~2.4 ms.",
        "- Throughput Audit: > 400 request / detik",
        "  (Kapasitas uji hingga 1,4 juta klaim / jam).",
        "- Sensitivitas / Recall: 98.6% - 100%",
        "  (Tinggi pada batasan aturan baku Kemenkes).",
        "- Presisi Deteksi: 96.4% (Meminimalkan alarm palsu).",
        "- ROC-AUC Score: 0.998 - 1.000.",
        "- Resource Footprint: Ringan (< 500 MB RAM)."
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
        "- Enkripsi Komunikasi Data:",
        "  Dukungan enkripsi TLS 1.3 saat transmisi data",
        "  dan AES-256 pada penyimpanan lokal.",
        "",
        "- Kedaulatan Data Medis Nasional:",
        "  Dapat berjalan 100% On-Premise di server",
        "  internal BPJS tanpa mengirim data ke cloud",
        "  pihak ketiga asing."
    ]
    py = card_y + card_h - 70
    for l in lines_pdp:
        c.drawString(x1 + 16, py, l)
        py -= 13.5

    # Column 2: Human-in-the-Loop Workstation
    x2 = x1 + col3_w + 16
    draw_card(c, x2, card_y, col3_w, card_h, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    draw_card(c, x2 + 16, card_y + card_h - 48, col3_w - 32, 34, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=4)
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(BPJS_BLUE)
    c.drawCentredString(x2 + col3_w / 2, card_y + card_h - 32, "TATA KELOLA HUMAN-IN-THE-LOOP")
    
    c.setFont("Helvetica", 8.5)
    c.setFillColor(TEXT_DARK)
    lines_gov = [
        "- AI Sebagai Decision Support System (DSS):",
        "  VeriKlaim tidak memutus klaim secara sepihak",
        "  (Zero Auto-Denial / Tanpa Penolakan Buta).",
        "",
        "- Otoritas Final Dokter Verifikator:",
        "  Pengesahan status klaim 100% dipegang oleh",
        "  dokter verifikator resmi BPJS Kesehatan",
        "  melalui Workstation Verifikasi Terpadu.",
        "",
        "- Cross-Check 4 Berkas Digital Otentik:",
        "  Dokter meneliti SEP, Resume DPJP, Billing,",
        "  dan Rujukan sebelum menetapkan vonis.",
        "",
        "- Transparansi Menyeluruh (No Black-Box):",
        "  Rekomendasi disertai kontribusi TreeSHAP",
        "  dan dasar pasal regulasi medis baku."
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
        "- Audit Trail Digital Persisten:",
        "  Setiap aktivitas penelaahan, putusan dokter,",
        "  catatan verifikasi, dan timestamp tersimpan",
        "  secara permanen di basis data verifikasi.",
        "",
        "- Kesiapan Pengawasan BPK RI & KPK RI:",
        "  Dokumentasi audit memenuhi standar pembuktian",
        "  administratif dan kepatuhan pengawasan DJS.",
        "",
        "- Berita Acara Audit Berstandar Formal:",
        "  Memuat stempel digital, nomor dokumen unik,",
        "  kalkulasi selisih tarif, dan QR Code verifikasi.",
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
    
    left_w = 460
    draw_card(c, 48, 52, left_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(66, 442, "HASIL UJI & VALIDASI (DATA RIIL & UJI SKENARIO)")
    
    m_w = (left_w - 32 - 12) / 2.0
    m_h = 70
    
    # Metric 1: Recall
    draw_card(c, 66, 350, m_w, m_h, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(78, 396, "98.6% - 100%")
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(78, 376, "Sensitivitas / Recall")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(78, 360, "Tinggi pada batasan aturan baku")

    # Metric 2: Precision
    draw_card(c, 66 + m_w + 12, 350, m_w, m_h, bg_color=BPJS_BLUE_LIGHT, border_color=BPJS_BLUE, radius=6)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(BPJS_BLUE)
    c.drawString(78 + m_w + 12, 396, "96.4%")
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(78 + m_w + 12, 376, "Precision Score")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(78 + m_w + 12, 360, "Meminimalkan alarm palsu bagi faskes")

    # Metric 3: Core Latency
    draw_card(c, 66, 268, m_w, m_h, bg_color=HexColor("#F3E8FF"), border_color=HexColor("#7E22CE"), radius=6)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor("#7E22CE"))
    c.drawString(78, 314, "~2.4 ms")
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(78, 294, "Latensi End-to-End API")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(78, 278, "Core execution < 1 ms")

    # Metric 4: Throughput
    draw_card(c, 66 + m_w + 12, 268, m_w, m_h, bg_color=ACCENT_AMBER_LIGHT, border_color=ACCENT_AMBER, radius=6)
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor("#B7791F"))
    c.drawString(78 + m_w + 12, 314, "> 400 req/s")
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(78 + m_w + 12, 294, "Throughput Audit")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(78 + m_w + 12, 278, "Sanggup > 1,4 juta klaim per jam")
    
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(TEXT_DARK)
    c.drawString(66, 245, "Cakupan Deteksi 6 Klaster Modus Kecurangan:")
    
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_MUTED)
    val_lines = [
        "- Klaster 1: Top-Up Special CMG fiktif tanpa tindakan bedah pendukung.",
        "- Klaster 2: Disparitas diagnosis masuk (ringan) vs utama (berat/drift).",
        "- Klaster 3: Lonjakan kecepatan biaya harian faskes (Cost Velocity Ratio).",
        "- Klaster 4: Bypassing rujukan berjenjang rawat jalan tingkat lanjut (RJTL).",
        "- Klaster 5: Upcoding ekstrim Severity III tanpa terapi intensif / ICU.",
        "- Klaster 6: Mismatch prosedur spesialistik lanjutan vs kelas faskes."
    ]
    vy = 230
    for vl in val_lines:
        c.drawString(66, vy, vl)
        vy -= 12.5

    # Right Column: Kesiapan Implementasi
    right_x = 48 + left_w + 16
    right_w = PAGE_WIDTH - 48 - right_x
    
    draw_card(c, right_x, 52, right_w, 413, bg_color=WHITE, border_color=BORDER_LIGHT, radius=8)
    
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(BPJS_GREEN)
    c.drawString(right_x + 20, 442, "KESIAPAN IMPLEMENTASI & ROADMAP (TRL 6)")
    
    draw_card(c, right_x + 16, 365, right_w - 32, 58, bg_color=BPJS_GREEN_LIGHT, border_color=BPJS_GREEN, radius=6)
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(BPJS_GREEN_DARK)
    c.drawString(right_x + 28, 405, "Technology Readiness Level 6 (TRL 6)")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 28, 388, "Prototipe sistem telah diuji coba komprehensif pada lingkungan operasional")
    c.drawString(right_x + 28, 374, "relevan menggunakan 50.000 data klaim FKRTL BPJS & 10.000 data skenario.")
    
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(TEXT_DARK)
    c.drawString(right_x + 20, 345, "Kebutuhan untuk Dipakai di Lapangan:")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_MUTED)
    req_lines = [
        "1. Integrasi API Gateway: Menghubungkan endpoint REST FastAPI",
        "   VeriKlaim dengan pipeline VClaim atau e-Klaim Kemenkes.",
        "2. Spesifikasi Server Minimal: 2 instance vCPU 4-core, RAM 8GB,",
        "   mampu melayani hingga ribuan klaim per detik dengan aman.",
        "3. Sertifikasi Verifikator: Pelatihan singkat workstation verifikasi",
        "   berbasis Buku Panduan Fitur Platform VeriKlaim resmi."
    ]
    ry = 330
    for rl in req_lines:
        c.drawString(right_x + 20, ry, rl)
        ry -= 12.5
        
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BPJS_BLUE)
    c.drawString(right_x + 20, 240, "Rencana Pengembangan Pasca-Healthkathon:")
    c.setFont("Helvetica", 8.2)
    c.setFillColor(TEXT_DARK)
    road_lines = [
        "- Tahap 1 (Bulan 1-2): Pilot Project di 5 RSUD mitra wilayah Kalbar.",
        "- Tahap 2 (Bulan 3-4): Integrasi modul OCR resume medis fisik.",
        "- Tahap 3 (Bulan 5-6): Peluncuran Modul Pra-Audit Mandiri untuk",
        "  manajemen RS seluruh Indonesia guna memangkas sengketa klaim.",
        "- Tahap 4: Pembentukan konsorsium riset AI Kesehatan bersama BPJS."
    ]
    rdy = 224
    for rdl in road_lines:
        c.drawString(right_x + 20, rdy, rdl)
        rdy -= 12.5
        
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
    
    c.setFillColor(BPJS_GREEN)
    c.rect(0, PAGE_HEIGHT - 8, PAGE_WIDTH, 8, fill=True, stroke=False)
    
    logo_path = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\docs\assets\template_p1_img1_Image6.png"
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 48, PAGE_HEIGHT - 85, width=170, height=58, preserveAspectRatio=True, mask='auto')
        
    c.setFont("Helvetica-Bold", 30)
    c.setFillColor(WHITE)
    c.drawString(48, PAGE_HEIGHT - 130, "Terima Kasih")
    
    c.setFont("Helvetica", 12)
    c.setFillColor(BPJS_GREEN_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 156, "Detect Smarter, Protect JKN - Smarter Protection for a Stronger JKN")
    
    c.setFont("Helvetica", 10.5)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(48, PAGE_HEIGHT - 176, "VeriKlaim: Solusi Deteksi Anomali Klaim FKRTL Berbasis AI & Explainable Governance")
    
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
        "- Workstation Verifikasi Human-in-the-Loop",
        "- Viewer 4 Dokumen Digital Terpadu",
        "- 6 Klaster Deteksi Blueprint Kemenkes",
        "- Explainable AI TreeSHAP Breakdown",
        "- Unduh Berita Acara & Buku Panduan PDF"
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
        "- Verification Workstation & LLM Collab",
        "- Model Terlatih (models/*.joblib)",
        "- Dataset 50.000 Riil & QA 10.000",
        "- Buku Panduan Fitur Platform (PDF)",
        "- Lisensi Open Research & MIT"
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
        "- Dosen Prodi Sistem Informasi, UNU Kalbar",
        "- Alumni STEI ITB",
        "- WhatsApp: 0856-5441-1081",
        "- Email: aditya.pratama@unukalbar.ac.id",
        "- Pontianak, Kalimantan Barat"
    ]
    cy = card_y + card_h - 110
    for cn in contact_notes:
        c.drawString(x3 + 18, cy, cn)
        cy -= 15

    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#64748B"))
    c.drawString(48, 30, "Project Final Healthkathon 2026 BPJS Kesehatan - Kategori Efisiensi Risiko pada Faskes / KLAIM (C03.04)")


def main():
    output_pdf = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\docs\Project_Final_Healthkathon_2026_VeriKlaim.pdf"
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)
    
    c = canvas.Canvas(output_pdf, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    
    draw_slide_1_cover(c)
    c.showPage()
    
    draw_slide_2_team(c)
    c.showPage()
    
    draw_slide_3_idea(c)
    c.showPage()
    
    draw_slide_4_background_impact(c)
    c.showPage()
    
    draw_slide_5_process_flow(c)
    c.showPage()
    
    draw_slide_6_demo_prototype(c)
    c.showPage()
    
    draw_slide_7_features(c)
    c.showPage()
    
    draw_slide_8_architecture(c)
    c.showPage()
    
    draw_slide_9_governance(c)
    c.showPage()
    
    draw_slide_10_validation_readiness(c)
    c.showPage()
    
    draw_slide_11_closing(c)
    c.showPage()
    
    c.save()
    print(f"SUCCESS: Generated updated balanced {output_pdf} with 11 slides!")


if __name__ == "__main__":
    main()
