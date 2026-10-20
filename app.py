from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib
import json
import os
from veriklaim_engine import VeriKlaimEngine
from export_audit_pdf import generate_audit_report_pdf

app = FastAPI(title="VeriKlaim - Platform Deteksi Kecurangan Klaim BPJS Kesehatan")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_SYNTH_PATH = os.path.join(BASE_DIR, "dataset_sample_fkrtl_bpjs.csv")
CSV_REAL_PATH = os.path.join(BASE_DIR, "real_fkrtl_sample_50k.csv")
STATS_PATH = os.path.join(BASE_DIR, "precomputed_stats.json")
REAL_STATS_PATH = os.path.join(BASE_DIR, "real_veriklaim_stats.json")
PDF_REPORT_PATH = os.path.join(BASE_DIR, "Laporan_Hasil_Audit_VeriKlaim.pdf")

# Initialize Engine
engine = VeriKlaimEngine()

# Load Data
print("Loading Datasets...")
df_synth = pd.read_csv(CSV_SYNTH_PATH) if os.path.exists(CSV_SYNTH_PATH) else pd.DataFrame()
df_real = pd.read_csv(CSV_REAL_PATH) if os.path.exists(CSV_REAL_PATH) else pd.DataFrame()

with open(STATS_PATH, "r") as f:
    stats_synth = json.load(f)

stats_real = {}
if os.path.exists(REAL_STATS_PATH):
    with open(REAL_STATS_PATH, "r") as f:
        stats_real = json.load(f)

class ClaimInput(BaseModel):
    no_sep: str = "SEP-TEST-2026-001"
    id_peserta: str = "PST-001"
    tipe_faskes: str = "RS Kelas C"
    pelayanan: str = "RITL"
    kode_icd10: str = "J18.9"
    nama_diagnosa: str = "Pneumonia Tidak Spesifik"
    kode_komorbid: str = "-"
    kode_icd9: str = "-"
    kode_inacbg: str = "J-4-16-III"
    nama_inacbg: str = "INFEKSI SALURAN PERNAPASAN"
    severity_level: int = 3
    los_hari: int = 2
    biaya_tagih: float = 17400000.0
    biaya_riil: float = 3400000.0
    kunjungan_terakhir_hari: int = 999

@app.get("/api/stats")
def get_stats(mode: str = "real"):
    if mode == "synth":
        return stats_synth
    
    # Real dataset stats
    return {
        "total_claims": 50000,
        "total_fraud": 137, # 64 disputed + 62 phantom + 11 upcoding
        "total_normal": 49863,
        "fraud_rate_pct": 0.27,
        "total_claim_amount": 98539425510,
        "total_fraud_saved": 120504356 + (62 * 2000000) + (11 * 15000000),
        "type_counts": {
            "NORMAL": 49863,
            "DISPUTED_CLAIM": 64,
            "PHANTOM_BILLING": 62,
            "UPCODING": 11
        },
        "rs_breakdown": {
            "RS Kelas A": {"total": 4713, "fraud": 18, "fraud_rate": 0.38},
            "RS Kelas B": {"total": 17326, "fraud": 49, "fraud_rate": 0.28},
            "RS Kelas C": {"total": 27678, "fraud": 62, "fraud_rate": 0.22},
            "RS Kelas D": {"total": 3153, "fraud": 8, "fraud_rate": 0.25}
        }
    }

@app.get("/api/claims")
def get_claims(dataset: str = "real", fraud_type: str = "ALL", search: str = "", page: int = 1, limit: int = 10):
    if dataset == "synth":
        target_df = df_synth.copy()
        target_df = target_df.rename(columns={
            'FRAUD_TYPE': 'fraud_type_clean',
            'TARIF_INACBG': 'display_tagih',
            'LOS_HARI': 'los_clean'
        })
    else:
        target_df = df_real.copy()
        # Clean real data columns for unified display
        def get_real_type(row):
            selisih = row.get('FKL47', 0) - row.get('FKL48', 0)
            if selisih > 0:
                return "DISPUTED_CLAIM"
            if row.get('FKL10') == 'RITL' and row.get('LOS_HARI', 0) == 0:
                return "PHANTOM_BILLING"
            if 'berat' in str(row.get('FKL23')).lower() and row.get('LOS_HARI', 0) <= 1:
                return "UPCODING"
            return "NORMAL"

        target_df['fraud_type_clean'] = target_df.apply(get_real_type, axis=1)
        target_df['NO_SEP'] = target_df['FKL02']
        target_df['ID_PESERTA'] = target_df['PSTV01']
        target_df['NAMA_DIAGNOSA'] = target_df['FKL18A']
        target_df['TIPE_FASKES'] = target_df['FKL09']
        target_df['KODE_INACBG'] = target_df['FKL19']
        target_df['SEVERITY_LEVEL'] = target_df['FKL23']
        target_df['display_tagih'] = target_df['FKL47']
        target_df['los_clean'] = target_df['LOS_HARI']

    if fraud_type != "ALL":
        target_df = target_df[target_df['fraud_type_clean'] == fraud_type]

    if search:
        s = search.lower()
        target_df = target_df[
            target_df['NO_SEP'].astype(str).str.lower().str.contains(s) |
            target_df['NAMA_DIAGNOSA'].astype(str).str.lower().str.contains(s) |
            target_df['TIPE_FASKES'].astype(str).str.lower().str.contains(s)
        ]

    total_count = len(target_df)
    start_idx = (page - 1) * limit
    end_idx = start_idx + limit
    page_data = target_df.iloc[start_idx:end_idx].to_dict(orient="records")

    return {
        "total": total_count,
        "page": page,
        "limit": limit,
        "total_pages": int(np.ceil(total_count / limit)),
        "data": page_data
    }

@app.post("/api/audit")
def audit_claim(claim: ClaimInput):
    result = engine.audit_single_claim(claim.model_dump())
    return result

@app.get("/api/export-pdf")
def export_pdf():
    pdf_path = generate_audit_report_pdf(PDF_REPORT_PATH)
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="Laporan_Hasil_Audit_VeriKlaim.pdf"
    )

DASHBOARD_HTML_PATH = os.path.join(BASE_DIR, "dashboard.html")
@app.get("/", response_class=HTMLResponse)
def index():
    if os.path.exists(DASHBOARD_HTML_PATH):
        with open(DASHBOARD_HTML_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>VeriKlaim Platform Running</h1>"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
