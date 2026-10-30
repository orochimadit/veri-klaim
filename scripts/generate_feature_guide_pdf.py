#!/usr/bin/env python3
"""
Generator PDF: Buku Panduan & Penjelasan Lengkap Fitur Platform VeriKlaim AI
BPJS Kesehatan - Healthkathon 2026
Warna & Tipografi mengacu pada: palet_warna_mobile_jkn.md
Bahasa: Non-teknis, komprehensif, terstruktur, ramah eksekutif dan dokter verifikator klinis.
Tata Letak: 5 Halaman Eksekutif Seimbang (Per-halaman tematik & berurutan rapi).
"""

import os
import sys
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# Palet Warna Mobile JKN BPJS Kesehatan (Sesuai palet_warna_mobile_jkn.md)
CLR_PRIMARY = colors.HexColor('#008D4C')       # Green Primary
CLR_PRIMARY_DARK = colors.HexColor('#00733E')  # Green Dark
CLR_SECONDARY = colors.HexColor('#0B4F6C')     # Blue Corporate
CLR_SUCCESS = colors.HexColor('#27AE60')       # Green Success
CLR_WARNING = colors.HexColor('#F39C12')       # Amber Warning
CLR_DANGER = colors.HexColor('#D32F2F')        # Red Danger
CLR_INFO = colors.HexColor('#2980B9')          # Blue Info
CLR_BG = colors.HexColor('#F5F7FA')            # Light Grey Canvas
CLR_SURFACE = colors.HexColor('#FFFFFF')       # Pure White
CLR_TEXT_DARK = colors.HexColor('#1F2937')     # Charcoal Text Primary
CLR_TEXT_MUTED = colors.HexColor('#6B7280')    # Slate Grey Text Secondary
CLR_BORDER = colors.HexColor('#E5E7EB')        # Subtle Border Grey
CLR_GREEN_LIGHT = colors.HexColor('#E8F5E9')   # Soft Green Background
CLR_BLUE_LIGHT = colors.HexColor('#E3F2FD')    # Soft Blue Background
CLR_AMBER_LIGHT = colors.HexColor('#FFFBEB')   # Soft Amber Background
CLR_RED_LIGHT = colors.HexColor('#FEF2F2')     # Soft Red Background

class NumberedCanvas(canvas.Canvas):
    """Canvas dua-arah untuk menghitung total halaman dan menggambar running header/footer."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_decorations(self, total_pages):
        page_num = self._pageNumber
        # Halaman pertama: cover banner aksen atas
        if page_num == 1:
            self.setFillColor(CLR_PRIMARY)
            self.rect(0, 836, 595.27, 6, fill=True, stroke=False)
            self.setFillColor(CLR_SECONDARY)
            self.rect(0, 832, 595.27, 4, fill=True, stroke=False)
        else:
            # Running Header pada halaman 2 ke atas
            self.saveState()
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(CLR_PRIMARY)
            self.drawString(40, 808, "VERIKLAIM AI — BUKU PANDUAN LENGKAP FITUR PLATFORM")
            self.setFont("Helvetica", 8)
            self.setFillColor(CLR_TEXT_MUTED)
            self.drawRightString(555, 808, "BPJS Kesehatan • Healthkathon 2026")
            
            # Garis pemisah header
            self.setStrokeColor(CLR_BORDER)
            self.setLineWidth(0.8)
            self.line(40, 800, 555, 800)
            self.restoreState()

        # Running Footer pada semua halaman
        self.saveState()
        self.setStrokeColor(CLR_BORDER)
        self.setLineWidth(0.8)
        self.line(40, 40, 555, 40)

        self.setFont("Helvetica", 8)
        self.setFillColor(CLR_TEXT_MUTED)
        self.drawString(40, 28, "Sistem Pengawasan Klaim FKRTL Berbasis AI Beretika & Human-in-the-Loop")
        
        page_text = f"Halaman {page_num} dari {total_pages}"
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(CLR_SECONDARY)
        self.drawRightString(555, 28, page_text)
        self.restoreState()

def build_pdf_feature_guide(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=46,
        bottomMargin=46
    )

    styles = getSampleStyleSheet()

    doc_title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=CLR_PRIMARY,
        spaceAfter=3
    )
    doc_sub_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=CLR_SECONDARY,
        spaceAfter=8
    )
    sec_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=CLR_PRIMARY,
        spaceBefore=8,
        spaceAfter=5,
        keepWithNext=True
    )
    feature_title_style = ParagraphStyle(
        'FeatureTitle',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=CLR_SECONDARY,
        spaceBefore=0,
        spaceAfter=0
    )
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=CLR_TEXT_DARK,
        spaceAfter=5
    )
    body_bold = ParagraphStyle(
        'BodyBoldCustom',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    callout_text = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11.5,
        textColor=CLR_TEXT_DARK
    )
    badge_style = ParagraphStyle(
        'BadgeText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.white,
        alignment=1
    )
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=CLR_TEXT_DARK
    )
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=CLR_TEXT_DARK
    )
    table_hdr = ParagraphStyle(
        'TableHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.white,
        alignment=0
    )

    printable_w = 515.0  # 595.27 - 80

    def make_callout(text, bg_color=CLR_GREEN_LIGHT, border_color=CLR_PRIMARY, label="PENJELASAN SEDERHANA"):
        content = [
            Paragraph(f"<b><font color='{border_color.hexval()}'>{label}:</font></b> {text}", callout_text)
        ]
        t = Table([[content]], colWidths=[printable_w])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg_color),
            ('BOX', (0,0), (-1,-1), 0.8, border_color),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        return t

    def make_feature_header(num_str, title_str, badge_label="FITUR UNGGULAN", badge_color=CLR_PRIMARY):
        hdr_table_data = [
            [
                Paragraph(f"<font color='white'><b>{badge_label} {num_str}</b></font>", badge_style),
                Paragraph(f"<b>{title_str}</b>", feature_title_style)
            ]
        ]
        t = Table(hdr_table_data, colWidths=[85, printable_w - 90])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), badge_color),
            ('ALIGN', (0,0), (0,0), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ]))
        return t

    story = []

    # =========================================================================
    # HALAMAN 1: IDENTITAS, PENGANTAR, FILOSOFI & PERBANDINGAN OPERASIONAL
    # =========================================================================
    story.append(Paragraph("BUKU PANDUAN & PENJELASAN LENGKAP FITUR", doc_title_style))
    story.append(Paragraph("PLATFORM VERIKLAIM AI — PENGAWASAN KLAIM FKRTL BPJS KESEHATAN", doc_sub_style))
    story.append(HRFlowable(width="100%", thickness=2, color=CLR_PRIMARY, spaceAfter=8))

    # Kotak Metadata Eksekutif
    now_str = datetime.now().strftime("%d %B %Y")
    meta_content = [
        [
            Paragraph("<b>Target Pembaca:</b> Dewan Direksi BPJS, Juri Healthkathon 2026, Manajemen RS, Dokter Verifikator JKN", table_cell),
            Paragraph(f"<b>Tanggal Penerbitan:</b> {now_str}", table_cell)
        ],
        [
            Paragraph("<b>Fokus Platform:</b> Audit Forensik Klaim Rumah Sakit (Peta Peluang AI/ML Kode C03.04)", table_cell),
            Paragraph("<b>Status Sistem:</b> Produksi Aktif (Healthkathon Track Inovasi)", table_cell)
        ]
    ]
    meta_table = Table(meta_content, colWidths=[320, 195])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CLR_BG),
        ('BOX', (0,0), (-1,-1), 1, CLR_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, CLR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # Pengantar
    story.append(Paragraph("1. Pengantar & Filosofi Inti: Mengapa VeriKlaim Diciptakan?", sec_title_style))
    p1 = (
        "Setiap bulan, BPJS Kesehatan memproses jutaan berkas klaim dari ribuan Fasilitas Kesehatan Rujukan Tingkat "
        "Lanjut (FKRTL / Rumah Sakit) di seluruh penjuru Indonesia. Proses verifikasi manual menghadapi tantangan besar: "
        "<b>kelelahan kognitif verifikator manusia</b> akibat menyisir jutaan lembar rincian tindakan medis, variasi "
        "interpretasi kaidah koding antar-daerah, serta waktu verifikasi yang kerap memakan waktu berminggu-minggu "
        "sehingga menahan arus kas operasional fasilitas kesehatan."
    )
    story.append(Paragraph(p1, body_style))

    p2 = (
        "<b>Platform VeriKlaim AI</b> hadir bukan untuk menggantikan peran manusia, melainkan sebagai <b>Mitra Cerdas "
        "Dokter Verifikator (Human-in-the-Loop)</b>. Sistem ini menyaring puluhan ribu berkas secara instan (< 1 ms), "
        "menyorot klaim yang memiliki risiko ketidakwajaran, dan menyodorkan bukti-bukti klinis digital secara transparan "
        "agar dokter verifikator dapat mengambil keputusan yang adil, cepat, dan berlandaskan hukum regulasi kesehatan."
    )
    story.append(Paragraph(p2, body_style))

    story.append(make_callout(
        "Bayangkan VeriKlaim seperti <b>'Mesin X-Ray Bandara'</b>. Petugas keamanan bandara tidak perlu membuka satu per satu "
        "koper seluruh penumpang secara manual. Mesin X-Ray seketika mendeteksi dan memberi tanda pada koper yang mencurigakan, "
        "namun keputusan untuk memeriksa lebih mendalam dan membuka koper tetap 100% berada di tangan petugas manusia.",
        CLR_GREEN_LIGHT, CLR_PRIMARY, "ANALOGI SEDERHANA"
    ))
    story.append(Spacer(1, 10))

    # Tabel Perbandingan Tradisional vs VeriKlaim
    story.append(Paragraph("Perbandingan Operasional: Verifikasi Konvensional vs Platform VeriKlaim AI", ParagraphStyle(
        'SubCmp', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, textColor=CLR_SECONDARY, spaceAfter=5
    )))
    cmp_hdr = [
        Paragraph("<b>Aspek Operasional</b>", table_hdr),
        Paragraph("<b>Verifikasi Klaim Manual Tradisional</b>", table_hdr),
        Paragraph("<b>Platform Cerdas VeriKlaim AI</b>", table_hdr)
    ]
    cmp_rows = [
        cmp_hdr,
        [
            Paragraph("<b>Kecepatan Audit</b>", table_cell_bold),
            Paragraph("15–30 menit per berkas; praktis hanya mampu menguji sampel kecil (&lt; 10% berkas).", table_cell),
            Paragraph("<b>&lt; 1 milidetik per berkas;</b> sanggup mengaudit 100% total klaim (50.000+ berkas).", table_cell)
        ],
        [
            Paragraph("<b>Kelelahan & Human Error</b>", table_cell_bold),
            Paragraph("Tinggi karena harus meneliti ribuan angka rincian kuitansi dan lembar kode secara visual.", table_cell),
            Paragraph("<b>Nol kelelahan kognitif;</b> AI otomatis mengelompokkan anomali prioritas.", table_cell)
        ],
        [
            Paragraph("<b>Keterbukaan Alasan</b>", table_cell_bold),
            Paragraph("Sering timbul sengketa (dispute) antara RS dan BPJS karena argumentasi audit bersifat subyektif.", table_cell),
            Paragraph("<b>Transparan (XAI TreeSHAP);</b> membeberkan grafik pengaruh variabel medis secara pasti.", table_cell)
        ],
        [
            Paragraph("<b>Otoritas Putusan</b>", table_cell_bold),
            Paragraph("Sepenuhnya manual namun tidak memiliki rekam jejak digital dan repositori dokumen terpadu.", table_cell),
            Paragraph("<b>Human-in-the-Loop;</b> Verifikator dokter tetap memegang kendali putusan final.", table_cell)
        ],
        [
            Paragraph("<b>Pencegahan di Hulu</b>", table_cell_bold),
            Paragraph("Reaktif setelah tagihan dikirim; RS baru tahu adanya kesalahan berminggu-minggu kemudian.", table_cell),
            Paragraph("<b>Proaktif & Preventif;</b> RS dapat menguji mandiri via Simulator & Swagger API sebelum submit.", table_cell)
        ]
    ]
    cmp_table = Table(cmp_rows, colWidths=[105, 205, 205])
    cmp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), CLR_SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, CLR_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [CLR_SURFACE, CLR_BG]),
    ]))
    story.append(cmp_table)

    # Akhir Halaman 1
    story.append(PageBreak())

    # =========================================================================
    # HALAMAN 2: FITUR 01, FITUR 02, FITUR 03 (DETEKSI 6 POLA KECURANGAN)
    # =========================================================================
    story.append(Paragraph("2. Bedah Lengkap Fitur Platform: Analisis Cepat & Pendeteksian Anomali", sec_title_style))
    story.append(Paragraph(
        "Berikut adalah fitur-fitur analisis dan deteksi cerdas yang dirancang untuk memantau integritas klaim:",
        body_style
    ))
    story.append(Spacer(1, 4))

    # FITUR 1: DASHBOARD EKSEKUTIF
    story.append(make_feature_header("01", "Dashboard Eksekutif & Pemantauan Keuangan Real-Time"))
    story.append(Spacer(1, 4))
    f1_desc = (
        "<b>Apa fungsinya?</b> Panel kendali utama bagi jajaran Direksi, Kepala Kantor Cabang BPJS Kesehatan, dan "
        "Manajemen Faskes untuk melihat potret kesehatan portofolio klaim secara makro dalam satu layar interaktif.<br/>"
        "<b>Informasi Utama yang Disajikan:</b><br/>"
        "• <b>Total Klaim Dipantau:</b> Melacak seluruh klaim yang masuk (mencakup 50.000 berkas pasien aktif).<br/>"
        "• <b>Potensi Penyelamatan Dana JKN:</b> Akumulasi rupiah riil yang berhasil ditahan dari pembayaran klaim "
        "yang terbukti bermasalah (mencapai <b>Rp 14,34 Miliar</b> pada dataset simulasi resmi).<br/>"
        "• <b>Tingkat Anomali Nasional:</b> Rasio klaim berisiko tinggi terhadap total klaim (~3.61%).<br/>"
        "• <b>Visualisasi Grafik Interaktif:</b> Distribusi kasus per departemen rawat inap, perbandingan tingkat "
        "keparahan (Severity Level 1, 2, 3), serta rasio efisiensi telaah klaim."
    )
    story.append(Paragraph(f1_desc, body_style))
    story.append(make_callout(
        "Bekerja layaknya <b>'Panel Instrumen Kokpit Pesawat'</b>. Pimpinan eksekutif dapat langsung mengetahui kondisi "
        "kesehatan keuangan jaminan sosial secara menyeluruh tanpa harus tenggelam dalam tumpukan berkas tabel excel.",
        CLR_BLUE_LIGHT, CLR_SECONDARY, "MANFAAT MANAJERIAL"
    ))
    story.append(Spacer(1, 8))

    # FITUR 2: SIMULATOR FORENSIK KLAIM SEKETIKA
    story.append(make_feature_header("02", "Simulator Forensik Klaim Seketika (< 1 Milidetik)"))
    story.append(Spacer(1, 4))
    f2_desc = (
        "<b>Apa fungsinya?</b> Kotak instrumen uji mandiri bagi staf koder RS maupun verifikator BPJS untuk menguji "
        "kelayakan satu berkas klaim sebelum diajukan secara resmi.<br/>"
        "<b>Cara Kerjanya:</b> Masukkan 5 data kunci: Nomor SEP, Kode Diagnosa (ICD-10), Tindakan Medis (ICD-9), Lama Hari Rawat "
        "(LOS), dan Total Tagihan RS. Dalam waktu <b>kurang dari 1 milidetik</b>, sistem langsung menerbitkan vonis: "
        "<b>'LAYAK BAYAR'</b> atau <b>'TERINDIKASI ANOMALI'</b> beserta nominal selisih terhadap tarif standar Permenkes No. 26/2021."
    )
    story.append(Paragraph(f2_desc, body_style))
    story.append(make_callout(
        "Menjadi <b>'Pencegah Kebocoran di Hulu'</b>. Pihak rumah sakit dapat memastikan tagihannya wajar dan bersih "
        "sebelum berkas diajukan, meniadakan risiko berkas ditolak atau pembayaran tertunda.",
        CLR_GREEN_LIGHT, CLR_PRIMARY, "EFISIENSI RS"
    ))
    story.append(Spacer(1, 8))

    # FITUR 3: MESIN DETEKSI 6 POLA KECURANGAN KLAIM
    story.append(make_feature_header("03", "Mesin Deteksi 6 Pola Kecurangan Klaim (Klaster Kemenkes RI)"))
    story.append(Spacer(1, 4))
    f3_desc = (
        "<b>Apa fungsinya?</b> Mesin kecerdasan buatan VeriKlaim dilatih secara khusus untuk mengenali 6 pola penyimpangan "
        "klaim paling lazim di FKRTL sesuai acuan Permenkes No. 16/2019 tentang Pencegahan Fraud JKN:"
    )
    story.append(Paragraph(f3_desc, body_style))

    pola_hdr = [
        Paragraph("<b>Pola Anomali</b>", table_hdr),
        Paragraph("<b>Arti & Contoh Kejadian di Lapangan</b>", table_hdr),
        Paragraph("<b>Respon Proteksi VeriKlaim AI</b>", table_hdr)
    ]
    pola_rows = [
        pola_hdr,
        [
            Paragraph("<b>1. Upcoding</b><br/><font color='#D32F2F'>Penggelembungan Kode</font>", table_cell_bold),
            Paragraph("Mencatat diagnosa/tindakan lebih berat dari kondisi asli pasien. <i>Contoh: Batuk pilek ringan diklaim sebagai Infeksi Paru Akut Berat agar klaim bernilai puluhan juta rupiah.</i>", table_cell),
            Paragraph("Mendeteksi ketidaksesuaian antara lama hari rawat, obat, dan tingkat keparahan INA-CBG.", table_cell)
        ],
        [
            Paragraph("<b>2. Phantom Billing</b><br/><font color='#7C3AED'>Klaim Pasien Fiktif</font>", table_cell_bold),
            Paragraph("Menagihkan rawat inap padahal pasien hanya berobat jalan atau tidak pernah dirawat (Lama rawat = 0 hari namun ditagih biaya rawat inap penuh).", table_cell),
            Paragraph("Mengunci klaim rawat inap 0 hari dan mengusulkan koreksi menjadi Rawat Jalan (RJTL).", table_cell)
        ],
        [
            Paragraph("<b>3. Unbundling / Split</b><br/><font color='#F39C12'>Pemecahan Tagihan</font>", table_cell_bold),
            Paragraph("Satu episode operasi utuh dipecah menjadi beberapa tagihan klaim terpisah dalam waktu singkat demi meraup pembayaran ganda.", table_cell),
            Paragraph("Mendeteksi tindakan medis terpisah dalam kurun waktu berdekatan dan menyarankan penyatuan paket klaim.", table_cell)
        ],
        [
            Paragraph("<b>4. Readmisi Berulang</b><br/><font color='#D97706'>Pulang-Pergi Cepat</font>", table_cell_bold),
            Paragraph("Pasien sengaja dipulangkan sebelum tuntas, lalu diminta masuk kembali 1–2 hari berikutnya demi menerbitkan nomor klaim baru.", table_cell),
            Paragraph("Menandai kunjungan berulang pasien yang sama dalam jeda &lt; 48 jam dengan diagnosa serupa.", table_cell)
        ],
        [
            Paragraph("<b>5. Disputed Claims</b><br/><font color='#2563EB'>Ketidakcocokan Tarif</font>", table_cell_bold),
            Paragraph("Pengajuan tarif tagihan melebihi plafon wajar kelas faskes (A, B, C, D) berdasarkan tarif regional.", table_cell),
            Paragraph("Menghitung deviasi biaya dan menahan klaim yang melompat di atas 30% dari ambang wajar.", table_cell)
        ],
        [
            Paragraph("<b>6. Klaim Standar</b><br/><font color='#27AE60'>Klaim Bersih & Wajar</font>", table_cell_bold),
            Paragraph("Klaim yang seluruh kaidah koding, lama perawatan, dan biaya tagihannya sesuai standar medis.", table_cell),
            Paragraph("Memberikan rekomendasi <b>Langsung Disetujui (Fast-Track Approval)</b> tanpa birokrasi.", table_cell)
        ]
    ]
    pola_table = Table(pola_rows, colWidths=[105, 215, 195])
    pola_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), CLR_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, CLR_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [CLR_SURFACE, CLR_BG]),
    ]))
    story.append(pola_table)

    # Akhir Halaman 2
    story.append(PageBreak())

    # =========================================================================
    # HALAMAN 3: FITUR 04 (XAI), FITUR 05 (NOTES), FITUR 06 (50K), FITUR 07 (MANUAL & 4 DOKUMEN)
    # =========================================================================
    story.append(Paragraph("2. Bedah Lengkap Fitur Platform: Transparansi & Verifikasi Klinis", sec_title_style))
    story.append(Paragraph(
        "Kecerdasan buatan beretika harus transparan dan menempatkan keputusan akhir di tangan dokter verifikator:",
        body_style
    ))
    story.append(Spacer(1, 4))

    # FITUR 4: TRANSPARANSI KEPUTUSAN AI (XAI)
    story.append(make_feature_header("04", "Transparansi Keputusan AI (Explainable AI - XAI TreeSHAP)"))
    story.append(Spacer(1, 4))
    f4_desc = (
        "<b>Apa fungsinya?</b> Menghapus stigma negatif AI sebagai 'Kotak Hitam' (Black Box) yang tidak berdasar. "
        "VeriKlaim menggunakan metode <b>Explainable AI (TreeSHAP)</b> untuk memaparkan 'Faktor Penentu' keputusan secara gamblang. "
        "Jika sebuah berkas ditandai anomali, sistem menjelaskan: <i>'Klaim ini dicurigai karena biaya tagihan 350% di atas "
        "plafon lama rawat 1 hari (+42% bobot pengaruh), serta ketiadaan bukti pendukung keparahan Level 3 (+28% bobot pengaruh).'</i>"
    )
    story.append(Paragraph(f4_desc, body_style))
    story.append(make_callout(
        "Transparansi ini memberikan kepastian hukum bagi RS dan BPJS. Penyesuaian tarif klaim didasari oleh "
        "fakta data kuantitatif yang jelas, bukan praduga sepihak.",
        CLR_BLUE_LIGHT, CLR_SECONDARY, "NILAI KEADILAN & HUKUM"
    ))
    story.append(Spacer(1, 8))

    # FITUR 5: ASISTEN CATATAN MEDIS ALAMI
    story.append(make_feature_header("05", "Asisten Catatan Medis Alami (Medical AI Notes)"))
    story.append(Spacer(1, 4))
    f5_desc = (
        "<b>Apa fungsinya?</b> Menerjemahkan angka probabilitas statistik menjadi resume telaah klinis berbahasa Indonesia "
        "formal yang santun dan berbobot, selayaknya telaah seorang dokter spesialis senior atau verifikator ahli JKN.<br/>"
        "<b>Contoh Hasil Telaah:</b> <i>'Terdapat indikasi disparitas klinis pada klaim No. SEP 92660224V000918. Pasien didiagnosis "
        "Diabetes Koma (Severity 3), namun dirawat hanya 1 hari tanpa terapi intensif ICU. Disarankan verifikator memeriksa lembar "
        "observasi DPJP dan billing obat sebelum dilakukan pencairan.'</i> Memberikan arahan telaah yang tepat sasaran."
    )
    story.append(Paragraph(f5_desc, body_style))
    story.append(Spacer(1, 8))

    # FITUR 6: PENJELAJAH BERKAS 50.000 KLAIM
    story.append(make_feature_header("06", "Penjelajah Berkas 50.000 Klaim FKRTL (Pencarian Cepat & Dua Status)"))
    story.append(Spacer(1, 4))
    f6_desc = (
        "<b>Apa fungsinya?</b> Gudang arsip digital terintegrasi yang menyajikan 50.000 data klaim FKRTL dengan navigasi "
        "secepat <b>20 milidetik</b> tanpa membuat peramban internet macet.<br/>"
        "<b>Keunggulan Navigasi:</b> Pencarian kilat Nomor SEP, Diagnosa ICD-10, Tindakan Medis, atau Faskes. "
        "Tabel menyajikan <b>Dua Status Berdampingan</b> yang transparan: "
        "<b>Status Audit AI</b> (Wajar vs Terindikasi Anomali) dan <b>Status Verifikasi Manual</b> (Menunggu Verifikasi vs Sudah Diverifikasi)."
    )
    story.append(Paragraph(f6_desc, body_style))
    story.append(Spacer(1, 8))

    # FITUR 7: VERIFIKASI MANUAL & PENAMPIL 4 DOKUMEN DIGITAL
    story.append(make_feature_header("07", "Verifikasi Manual Manusia & Penampil 4 Dokumen Digital", badge_color=CLR_PRIMARY_DARK))
    story.append(Spacer(1, 4))
    f7_desc = (
        "<b>Apa fungsinya?</b> Menegakkan prinsip tertinggi etika kecerdasan buatan: <b>AI hanya asisten pemberi rekomendasi, "
        "keputusan mutlak pembayaran berada di tangan Dokter Verifikator Manusia</b>. Saat verifikator membuka berkas klaim, "
        "sistem menampilkan jendela telaah berdampingan dengan <b>4 Dokumen Digital Resmi</b>:"
    )
    story.append(Paragraph(f7_desc, body_style))

    doc_hdr = [
        Paragraph("<b>Dokumen Digital</b>", table_hdr),
        Paragraph("<b>Fungsi & Bukti Klinis yang Diteliti</b>", table_hdr),
        Paragraph("<b>Tujuan Pencocokan dengan AI</b>", table_hdr)
    ]
    doc_rows = [
        doc_hdr,
        [
            Paragraph("<b>1. Surat Eligibilitas Peserta (SEP)</b>", table_cell_bold),
            Paragraph("Surat keabsahan kepesertaan aktif JKN, tanggal masuk, dan hak kelas rawat pasien.", table_cell),
            Paragraph("Memastikan pasien benar-benar terdaftar dan status iuran aktif.", table_cell)
        ],
        [
            Paragraph("<b>2. Resume Medis DPJP</b>", table_cell_bold),
            Paragraph("Catatan riwayat keluhan, hasil lab, tindakan dokter spesialis penanggung jawab.", table_cell),
            Paragraph("Membuktikan kebenaran tingkat keparahan penyakit dan lama rawat.", table_cell)
        ],
        [
            Paragraph("<b>3. Kuitansi Rincian Biaya (Billing RS)</b>", table_cell_bold),
            Paragraph("Perincian biaya riil obat-obatan, honor medis, alat kesehatan, dan kamar rawat.", table_cell),
            Paragraph("Mencocokkan apakah tagihan RS wajar terhadap paket tarif INA-CBG.", table_cell)
        ],
        [
            Paragraph("<b>4. Surat Rujukan FKTP</b>", table_cell_bold),
            Paragraph("Dokumen legal rujukan berjenjang dari Puskesmas/Klinik ke Rumah Sakit.", table_cell),
            Paragraph("Mencegah pemecahan kasus berulang yang menyalahi prosedur rujukan.", table_cell)
        ],
    ]
    doc_table = Table(doc_rows, colWidths=[120, 210, 185])
    doc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), CLR_SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, CLR_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [CLR_SURFACE, CLR_BG]),
    ]))
    story.append(doc_table)
    story.append(Spacer(1, 4))
    f7_action = (
        "Verifikator kemudian memilih satu dari 4 keputusan resmi: <b>(1) DITERIMA / LAYAK BAYAR</b>, <b>(2) DITOLAK / FRAUD</b>, "
        "<b>(3) PERLU AUDIT MEDIS</b>, atau <b>(4) PERLU KONFIRMASI DPJP</b>. Hasil keputusan langsung tersimpan ke basis data "
        "permanen dan membarui status berkas secara seketika (*audit trail* tercatat rapi)."
    )
    story.append(Paragraph(f7_action, body_style))

    # Akhir Halaman 3
    story.append(PageBreak())

    # =========================================================================
    # HALAMAN 4: FITUR 08, 09, 10 & BAGIAN 3: ALUR KERJA OPERASIONAL
    # =========================================================================
    story.append(Paragraph("2. Bedah Lengkap Fitur Platform: Ketahanan Sistem & Integrasi", sec_title_style))
    story.append(Spacer(1, 4))

    # FITUR 8: SAKLAR MODE AI CERDAS
    story.append(make_feature_header("08", "Saklar Mode AI Cerdas (Hybrid Online Cloud vs Offline Tanggap Darurat)"))
    story.append(Spacer(1, 4))
    f8_desc = (
        "<b>Apa fungsinya?</b> Menjamin sistem beroperasi 100% tanpa henti (*Zero Crash*) dalam segala situasi infrastruktur jaringan.<br/>"
        "• <b>Mode Online (Google Gemini Pro AI Cloud):</b> Menghasilkan telaah semantik teks medis yang kaya konteks saat internet tersedia.<br/>"
        "• <b>Mode Offline Tanggap Darurat (Deterministic Rules Engine):</b> Jika koneksi internet kantor cabang atau RS terputus, sistem "
        "secara cerdas dan mulus beralih ke mesin aturan lokal berstandar Permenkes tanpa gangguan operasional sedikitpun."
    )
    story.append(Paragraph(f8_desc, body_style))
    story.append(Spacer(1, 8))

    # FITUR 9: GERBANG INTEGRASI SWAGGER API UI
    story.append(make_feature_header("09", "Gerbang Integrasi Rumah Sakit (Swagger API UI untuk SIMRS & VClaim)"))
    story.append(Spacer(1, 4))
    f9_desc = (
        "<b>Apa fungsinya?</b> Jembatan integrasi digital modern (*Interoperability*) berbasis REST API yang dilengkapi antarmuka "
        "<b>Swagger UI interaktif</b>. Memungkinkan Sistem Informasi Manajemen RS (SIMRS) atau aplikasi VClaim BPJS melakukan "
        "audit otomatis sebelum berkas dikirim. RS dapat menemukan dan memperbaiki kesalahan koding di sistem internalnya sendiri, "
        "sehingga klaim tertunda (*pending claim*) dapat dipangkas hingga mendekati nol."
    )
    story.append(Paragraph(f9_desc, body_style))
    story.append(Spacer(1, 8))

    # FITUR 10: PUSAT EKSPOR LAPORAN RESMI
    story.append(make_feature_header("10", "Pusat Ekspor Laporan Resmi Eksekutif & Berita Acara (PDF)"))
    story.append(Spacer(1, 4))
    f10_desc = (
        "<b>Apa fungsinya?</b> Fasilitas satu-klik untuk mencetak Berita Acara Hasil Audit Klaim resmi berformat PDF formal berstandar korporat. "
        "Memuat Nomor Surat Dokumen, Tanggal & Jam Audit, Ringkasan Statistik Penyelamatan Anggaran, Rincian Kasus Anomali, Dasar Regulasi, "
        "dan Kolom Tanda Tangan Verifikator. Dokumen ini sah dan siap dijadikan berkas rekonsiliasi bersama pihak rumah sakit."
    )
    story.append(Paragraph(f10_desc, body_style))
    story.append(Spacer(1, 10))

    # BAGIAN 3: ALUR KERJA OPERASIONAL
    story.append(Paragraph("3. Panduan Alur Kerja Operasional Sehari-hari (Step-by-Step)", sec_title_style))
    story.append(Paragraph(
        "Alur kerja harian pengguna dari tingkat manajemen eksekutif hingga dokter verifikator teknis:",
        body_style
    ))
    story.append(Spacer(1, 4))

    flow_hdr = [
        Paragraph("<b>Tahap</b>", table_hdr),
        Paragraph("<b>Pelaksana</b>", table_hdr),
        Paragraph("<b>Aktivitas pada Platform VeriKlaim</b>", table_hdr),
        Paragraph("<b>Hasil / Keluaran Nyata</b>", table_hdr)
    ]
    flow_rows = [
        flow_hdr,
        [
            Paragraph("<b>Tahap 1</b>", table_cell_bold),
            Paragraph("Pimpinan BPJS / Kepala Klaim", table_cell),
            Paragraph("Membuka <b>Dashboard Eksekutif</b> untuk memantau total klaim, rasio anomali, dan estimasi dana terselamatkan.", table_cell),
            Paragraph("Pemetaan risiko klaim makro seketika.", table_cell)
        ],
        [
            Paragraph("<b>Tahap 2</b>", table_cell_bold),
            Paragraph("Dokter Verifikator JKN", table_cell),
            Paragraph("Membuka <b>Penjelajah Berkas Klaim</b>, memfilter status 'Terindikasi Anomali' dan 'Menunggu Verifikasi'.", table_cell),
            Paragraph("Daftar klaim prioritas tinggi tersaji rapi.", table_cell)
        ],
        [
            Paragraph("<b>Tahap 3</b>", table_cell_bold),
            Paragraph("Dokter Verifikator JKN", table_cell),
            Paragraph("Mengeklik 'Audit & Verifikasi', membaca catatan rekomendasi AI, dan memeriksa <b>4 Dokumen Digital</b>.", table_cell),
            Paragraph("Validasi silang bukti rekam medik vs tagihan.", table_cell)
        ],
        [
            Paragraph("<b>Tahap 4</b>", table_cell_bold),
            Paragraph("Dokter Verifikator JKN", table_cell),
            Paragraph("Memilih keputusan resmi (Diterima / Ditolak / Audit Lanjutan), mengisi catatan telaah, dan menyimpan data.", table_cell),
            Paragraph("Status berkas seketika terupdate permanen.", table_cell)
        ],
        [
            Paragraph("<b>Tahap 5</b>", table_cell_bold),
            Paragraph("Staf Verifikasi & RS", table_cell),
            Paragraph("Mengeklik tombol 'Unduh Laporan Audit' untuk mengunduh berkas PDF resmi sebagai Berita Acara Rekonsiliasi.", table_cell),
            Paragraph("Dokumen legal cetak siap untuk pertanggungjawaban.", table_cell)
        ],
    ]
    flow_table = Table(flow_rows, colWidths=[55, 105, 220, 135])
    flow_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), CLR_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, CLR_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [CLR_SURFACE, CLR_BG]),
    ]))
    story.append(flow_table)

    # Akhir Halaman 4
    story.append(PageBreak())

    # =========================================================================
    # HALAMAN 5: DAMPAK STRATEGIS, LANDASAN HUKUM, PENUTUP & PENGESAHAN
    # =========================================================================
    story.append(Paragraph("4. Dampak Strategis bagi 4 Pemangku Kepentingan", sec_title_style))
    impact_hdr = [
        Paragraph("<b>Pihak Berkepentingan</b>", table_hdr),
        Paragraph("<b>Manfaat Nyata yang Diperoleh</b>", table_hdr)
    ]
    impact_rows = [
        impact_hdr,
        [
            Paragraph("<b>1. BPJS Kesehatan</b>", table_cell_bold),
            Paragraph("Menjaga kesinambungan Dana Jaminan Sosial (DJS), mencegah potensi kebocoran anggaran hingga belasan miliar rupiah, dan memastikan kepatuhan tata kelola faskes sesuai kaidah INA-CBG.", table_cell)
        ],
        [
            Paragraph("<b>2. Rumah Sakit (FKRTL)</b>", table_cell_bold),
            Paragraph("Kepastian pembayaran klaim bersih lebih cepat (*turnaround time* singkat), transparansi alasan saat terjadi penyesuaian tarif, serta pembinaan tertib administrasi koding bagi koder RS.", table_cell)
        ],
        [
            Paragraph("<b>3. Dokter Verifikator JKN</b>", table_cell_bold),
            Paragraph("Beban kognitif berkurang drastis; tidak perlu lagi memeriksa 50.000 berkas satu demi satu secara manual, karena berkas berisiko tinggi telah disaring dan dilengkapi bukti rekam medik pendukung.", table_cell)
        ],
        [
            Paragraph("<b>4. Pasien & Peserta JKN</b>", table_cell_bold),
            Paragraph("Terlindungi dari potensi penahanan rawat inap fiktif atau tindakan medis yang tidak perlu, sehingga mutu pelayanan medis yang diterima peserta tetap optimal dan bermartabat.", table_cell)
        ]
    ]
    impact_table = Table(impact_rows, colWidths=[130, 385])
    impact_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), CLR_SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, CLR_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [CLR_SURFACE, CLR_BG]),
    ]))
    story.append(impact_table)
    story.append(Spacer(1, 10))

    # Ringkasan Kuantitatif
    kpi_box_data = [
        [
            Paragraph("<b>Kapasitas Audit</b><br/>50.000 Berkas", ParagraphStyle('KB1', fontName='Helvetica-Bold', fontSize=9, textColor=CLR_PRIMARY, alignment=1)),
            Paragraph("<b>Potensi Penghematan</b><br/>Rp 14,34 Miliar", ParagraphStyle('KB2', fontName='Helvetica-Bold', fontSize=9, textColor=CLR_SECONDARY, alignment=1)),
            Paragraph("<b>Kecepatan Respon</b><br/>&lt; 1 Milidetik", ParagraphStyle('KB3', fontName='Helvetica-Bold', fontSize=9, textColor=CLR_SUCCESS, alignment=1)),
            Paragraph("<b>Keandalan Sistem</b><br/>100% Zero Crash", ParagraphStyle('KB4', fontName='Helvetica-Bold', fontSize=9, textColor=CLR_INFO, alignment=1)),
        ]
    ]
    kpi_box = Table(kpi_box_data, colWidths=[128, 129, 129, 129])
    kpi_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CLR_BG),
        ('BOX', (0,0), (-1,-1), 1, CLR_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, CLR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(kpi_box)
    story.append(Spacer(1, 10))

    # Landasan Regulasi
    story.append(Paragraph("5. Landasan Regulasi & Kepatuhan Hukum", sec_title_style))
    regulasi_list = [
        "<b>Permenkes No. 26 Tahun 2021:</b> Pedoman Teknis Tarif Pelayanan Kesehatan Program JKN dan Kaidah Koding INA-CBG.",
        "<b>Permenkes No. 16 Tahun 2019:</b> Pencegahan dan Penanganan Kecurangan (Fraud) dalam Penyelenggaraan Jaminan Kesehatan.",
        "<b>Surat Edaran Dirjen Pelayanan Kesehatan HK.02.02/I/1811/2022:</b> Larangan pemecahan episode tindakan medis berkelanjutan."
    ]
    for r in regulasi_list:
        story.append(Paragraph(f"• {r}", body_style))

    story.append(Spacer(1, 8))

    # Penutup
    story.append(Paragraph("6. Penutup & Komitmen Integritas Transformasi Digital", sec_title_style))
    closing_p = (
        "Platform VeriKlaim AI membuktikan bahwa adopsi kecerdasan buatan dalam ekosistem jaminan kesehatan nasional "
        "tidak harus rumit atau menakutkan. Dengan mengedepankan asas <b>transparansi, kemudahan navigasi, keselarasan "
        "regulasi Kemenkes RI, serta pengawasan beretika berbasis manusia (Human-in-the-Loop)</b>, VeriKlaim siap menjadi "
        "standar baru transformasi tata kelola klaim kesehatan Indonesia yang berintegritas dan berkelanjutan."
    )
    story.append(Paragraph(closing_p, body_style))
    story.append(Spacer(1, 10))

    # Kolom Pengesahan Tim Inovator
    sig_content = [
        [
            Paragraph("<b>Disusun dan Dikembangkan Oleh:</b><br/>Tim Inovasi VeriKlaim AI — Healthkathon BPJS Kesehatan 2026<br/><i>Peta Peluang AI & ML Kode C03.04 (Klaim FKRTL)</i>", table_cell),
            Paragraph("<b>Susunan Tim Pengusul:</b><br/>• Aditya Pratama, S.T., M.T. (Dosen Sistem Informasi UNU Kalbar / Alumni ITB)<br/>• Nurman Hariyanto, S.ST., M.T. (Dosen Sistem Informasi UNU Kalbar / Alumni ITB)<br/>• M. Ali Maulana, M.Kep. (Dosen Keperawatan FK UNTAN)", table_cell)
        ]
    ]
    sig_table = Table(sig_content, colWidths=[240, 275])
    sig_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CLR_BG),
        ('BOX', (0,0), (-1,-1), 1, CLR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(sig_table)

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[Sukses] Buku Panduan Fitur PDF berhasil dibuat di: {output_path}")
    return output_path

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_path = os.path.join(base_dir, "docs", "Buku_Panduan_Fitur_Platform_VeriKlaim.pdf")
    build_pdf_feature_guide(target_path)
