import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime

def generate_audit_report_pdf(output_path: str = None, stats: dict = None, flagged_claims: list = None):
    if output_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(base_dir, "Laporan_Resmi_Audit_VeriKlaim_BPJS.pdf")

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom typography
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#0a2540'),
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#009639'),
        spaceAfter=12
    )
    heading_style = ParagraphStyle(
        'SecHead',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#0a2540'),
        spaceBefore=12,
        spaceAfter=6
    )
    body_style = ParagraphStyle(
        'BodyTxt',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155')
    )
    table_cell_style = ParagraphStyle(
        'CellTxt',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1e293b')
    )
    table_hdr_style = ParagraphStyle(
        'HdrTxt',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.white
    )

    story = []

    # Header
    story.append(Paragraph("BPJS KESEHATAN — HEALTHKATHON 2026", subtitle_style))
    story.append(Paragraph("LAPORAN RESMI AUDIT FORENSIK KLAIM FKRTL", title_style))
    story.append(Paragraph("Sistem VeriKlaim (Peta Peluang AI & ML Kode C03.04 - KLAIM)", ParagraphStyle(
        'SubTag', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=9, textColor=colors.HexColor('#64748b'), spaceAfter=8
    )))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#009639'), spaceAfter=14))

    # Metadata Box
    now_str = datetime.now().strftime("%d %B %Y, %H:%M WIB")
    meta_data = [
        [
            Paragraph("<b>Nomor Dokumen:</b> VERIKLAIM/AUDIT/2026/04", body_style),
            Paragraph(f"<b>Tanggal Audit:</b> {now_str}", body_style)
        ],
        [
            Paragraph("<b>Dataset Rujukan:</b> Data Sampel Resmi BPJS 2024 & Modul Sintetis", body_style),
            Paragraph("<b>Engine Evaluasi:</b> XGBoost Ensemble + Isolation Forest", body_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[260, 260])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 14))

    # Executive Summary Stats
    story.append(Paragraph("1. Ringkasan Eksekutif Hasil Verifikasi Klaim", heading_style))

    total_claims = stats.get('total_claims', 50000) if stats else 50000
    total_fraud = stats.get('total_fraud', 1805) if stats else 1805
    fraud_pct = stats.get('fraud_rate_pct', 3.61) if stats else 3.61
    total_saved = stats.get('total_fraud_saved', 14340957729) if stats else 14340957729

    kpi_data = [
        [
            Paragraph("<b>Total Klaim Diperiksa</b>", table_hdr_style),
            Paragraph("<b>Klaim Terindikasi Anomali</b>", table_hdr_style),
            Paragraph("<b>Tingkat Anomali</b>", table_hdr_style),
            Paragraph("<b>Potensi Penghematan Dana</b>", table_hdr_style),
        ],
        [
            Paragraph(f"<b>{total_claims:,} Klaim</b>", ParagraphStyle('Kpi1', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#0f172a'))),
            Paragraph(f"<b>{total_fraud:,} Klaim Ditahan</b>", ParagraphStyle('Kpi2', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#dc2626'))),
            Paragraph(f"<b>{fraud_pct}%</b>", ParagraphStyle('Kpi3', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#d97706'))),
            Paragraph(f"<b>Rp {total_saved:,.0f}</b>", ParagraphStyle('Kpi4', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#009639'))),
        ]
    ]
    kpi_table = Table(kpi_data, colWidths=[130, 130, 100, 160])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0a2540')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#f1f5f9')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 14))

    # Core Module Findings Table
    story.append(Paragraph("2. Rincian Kasus Anomali Berdasarkan Modul Deteksi", heading_style))

    sample_rows = [
        [
            Paragraph("<b>No SEP / Kunjungan</b>", table_hdr_style),
            Paragraph("<b>Diagnosa & CBG</b>", table_hdr_style),
            Paragraph("<b>LOS & Keparahan</b>", table_hdr_style),
            Paragraph("<b>Tarif Tagihan RS</b>", table_hdr_style),
            Paragraph("<b>Klasifikasi Anomali</b>", table_hdr_style),
            Paragraph("<b>Rekomendasi Tindakan</b>", table_hdr_style),
        ],
        [
            Paragraph("420360124V000144<br/>(RS Rujukan)", table_cell_style),
            Paragraph("ISPA Ringan (J06)<br/>U-4-13-I", table_cell_style),
            Paragraph("3 Hari / Level 1", table_cell_style),
            Paragraph("Rp 1.994.100<br/><font color='#dc2626'>Dipangkas Rp 199.410</font>", table_cell_style),
            Paragraph("<font color='#b91c1c'><b>DISPUTED / UPCODING</b></font>", table_cell_style),
            Paragraph("Turunkan tarif klaim sesuai hasil resume verifikasi", table_cell_style),
        ],
        [
            Paragraph("419911224V002625<br/>(RS Kelas C)", table_cell_style),
            Paragraph("Hipertensi Primer (I10)<br/>I-4-17-I", table_cell_style),
            Paragraph("<b>0 Hari</b> / Level 1", table_cell_style),
            Paragraph("Rp 2.223.200", table_cell_style),
            Paragraph("<font color='#7c3aed'><b>PHANTOM BILLING</b></font>", table_cell_style),
            Paragraph("Koreksi ke rawat jalan (RJTL). Tahan pembayaran rawat inap", table_cell_style),
        ],
        [
            Paragraph("92660224V000918<br/>(RS Kelas B)", table_cell_style),
            Paragraph("Diabetes Koma (E11)<br/>J-1-20-III (Severity 3)", table_cell_style),
            Paragraph("<b>1 Hari</b> / Level 3", table_cell_style),
            Paragraph("Rp 33.456.700", table_cell_style),
            Paragraph("<font color='#dc2626'><b>UPCODING EKSTREM</b></font>", table_cell_style),
            Paragraph("Minta audit medis rekam medik penunjang ICU/DPJP", table_cell_style),
        ],
        [
            Paragraph("SEP-UNB-2026-0019<br/>(RS Kelas D)", table_cell_style),
            Paragraph("Apendisitis Akut (K35.8)<br/>K-1-12-I", table_cell_style),
            Paragraph("1 Hari / Kunjungan berulang &lt; 48 jam", table_cell_style),
            Paragraph("Rp 7.500.000", table_cell_style),
            Paragraph("<font color='#d97706'><b>UNBUNDLING / SPLIT</b></font>", table_cell_style),
            Paragraph("Konsolidasi 2 kunjungan menjadi 1 paket klaim INA-CBG", table_cell_style),
        ]
    ]

    claims_table = Table(sample_rows, colWidths=[95, 110, 85, 90, 80, 60])
    claims_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#009639')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(claims_table)
    story.append(Spacer(1, 14))

    # Regulatory Framework
    story.append(Paragraph("3. Landasan Hukum & Regulasi Penindakan", heading_style))
    regulasi_points = [
        "<b>Permenkes No. 26 Tahun 2021:</b> Pedoman Teknis Tarif Pelayanan Kesehatan JKN dan Kaidah Koding INA-CBG.",
        "<b>Permenkes No. 16 Tahun 2019:</b> Pencegahan dan Penanganan Kecurangan (Fraud) dalam Penyelenggaraan Jaminan Kesehatan.",
        "<b>Surat Edaran Dirjen Pelayanan Kesehatan HK.02.02/I/1811/2022:</b> Larangan pemecahan episode tindakan medis berkelanjutan."
    ]
    for r in regulasi_points:
        story.append(Paragraph(f"• {r}", body_style))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 20))

    # Signature Block
    sig_data = [
        [
            Paragraph("<b>Diverifikasi Oleh Engine:</b><br/>VeriKlaim AI Platform v1.2<br/>Healthkathon BPJS Kesehatan 2026", body_style),
            Paragraph("<b>Tim Pengusul Inovasi:</b><br/>• Aditya Pratama, S.T., M.T. (Lead AI / STEI ITB)<br/>• Nurman Hariyanto, S.ST., M.T. (IoT / Data Lead)<br/>• M. Ali Maulana, M.Kep. (Clinical Domain Lead / UNTAN)", body_style)
        ]
    ]
    sig_table = Table(sig_data, colWidths=[260, 260])
    sig_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(sig_table)

    doc.build(story)
    print(f"[PDF Generator] Laporan audit berhasil dibuat di: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_audit_report_pdf()
