import pandas as pd
import numpy as np
from datetime import datetime
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

fkrtl_path = os.path.join(ROOT_DIR, "Data sampel 2015-2024 (1)", "2025", "Data Sampel Reguler Edisi 2025", "data", "202403_fkrtl.dta")
out_csv_path = os.path.join(ROOT_DIR, "data", "real_fkrtl_sample_50k.csv")
out_stats_path = os.path.join(ROOT_DIR, "data", "stats", "real_fkrtl_eda_stats.json")

print("Memulai eksplorasi aman dataset real BPJS FKRTL 2024...")

selected_cols = [
    'PSTV01', 'FKL02', 'FKL03', 'FKL04', 'FKL05', 'FKL06', 'FKL08', 'FKL09',
    'FKL10', 'FKL11', 'FKL12', 'FKL13', 'FKL14', 'FKL17A', 'FKL18', 'FKL18A',
    'FKL19', 'FKL19A', 'FKL23', 'FKL30', 'FKL31', 'FKL47', 'FKL48'
]

total_scanned = 0
dispute_count = 0
total_tagih = 0
total_verifikasi = 0
total_selisih_dispute = 0

ritl_count = 0
rjtl_count = 0

hospital_type_counts = {}
severity_counts = {}
top_diagnoses = {}
top_dispute_diagnoses = {}

sample_records = []
TARGET_SAMPLE_SIZE = 50000

chunk_size = 25000
reader = pd.read_stata(fkrtl_path, columns=selected_cols, iterator=True)

chunk_idx = 0
while total_scanned < 100000:
    try:
        chunk = reader.get_chunk(chunk_size)
    except StopIteration:
        break

    chunk_idx += 1
    total_scanned += len(chunk)
    
    tgl_masuk = pd.to_datetime(chunk['FKL03'], errors='coerce')
    tgl_pulang = pd.to_datetime(chunk['FKL04'], errors='coerce')
    chunk['LOS_HARI'] = (tgl_pulang - tgl_masuk).dt.days.fillna(0).astype(int)
    
    total_tagih += int(chunk['FKL47'].sum())
    total_verifikasi += int(chunk['FKL48'].sum())
    
    disputes = chunk[chunk['FKL47'] != chunk['FKL48']]
    dispute_count += len(disputes)
    diffs = (disputes['FKL47'] - disputes['FKL48']).apply(lambda x: max(0, x))
    total_selisih_dispute += int(diffs.sum())
    
    for diag, c in disputes['FKL18A'].value_counts().head(5).items():
        top_dispute_diagnoses[str(diag)] = top_dispute_diagnoses.get(str(diag), 0) + int(c)
        
    s_counts = chunk['FKL10'].value_counts()
    ritl_count += int(s_counts.get('RITL', 0))
    rjtl_count += int(s_counts.get('RJTL', 0))
    
    for ht, c in chunk['FKL09'].value_counts().items():
        hospital_type_counts[str(ht)] = hospital_type_counts.get(str(ht), 0) + int(c)

    for sev, c in chunk['FKL23'].value_counts().items():
        severity_counts[str(sev)] = severity_counts.get(str(sev), 0) + int(c)
        
    for d, c in chunk['FKL18A'].value_counts().head(10).items():
        top_diagnoses[str(d)] = top_diagnoses.get(str(d), 0) + int(c)

    if len(sample_records) * chunk_size < TARGET_SAMPLE_SIZE:
        sample_records.append(chunk)

print(f"Selesai membaca {total_scanned:,} baris klaim nyata!")

df_sample = pd.concat(sample_records, ignore_index=True).iloc[:TARGET_SAMPLE_SIZE]
df_sample.to_csv(out_csv_path, index=False)
print(f"Sample 50.000 baris tersimpan di: {out_csv_path}")

top_10_diag = sorted(top_diagnoses.items(), key=lambda x: x[1], reverse=True)[:10]
top_disputes = sorted(top_dispute_diagnoses.items(), key=lambda x: x[1], reverse=True)[:10]

summary = {
    "total_scanned_claims": int(total_scanned),
    "service_distribution": {
        "Rawat Jalan (RJTL)": int(rjtl_count),
        "Rawat Inap (RITL)": int(ritl_count)
    },
    "financials": {
        "total_biaya_tagih_rs": int(total_tagih),
        "total_biaya_verifikasi_bpjs": int(total_verifikasi),
        "total_koreksi_dispute_idr": int(total_selisih_dispute)
    },
    "audit_findings": {
        "total_klaim_dikoreksi_bpjs": int(dispute_count),
        "dispute_rate_pct": round(float(dispute_count) / total_scanned * 100, 2),
        "top_dispute_diagnoses": {k: int(v) for k, v in top_disputes}
    },
    "severity_distribution": {k: int(v) for k, v in severity_counts.items()},
    "hospital_distribution": {k: int(v) for k, v in hospital_type_counts.items()},
    "top_10_diagnoses": {k: int(v) for k, v in top_10_diag}
}

with open(out_stats_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print("Ringkasan statistik berhasil disimpan di:", out_stats_path)
