"""
Unit & Integration Test Suite: Fitur Upload Data Klaim & Pembobotan Skoring Akurasi AI Ensemble
Menguji:
1. Endpoint Download Template Klaim (/api/claims/upload/template) format CSV & JSON.
2. Endpoint Upload & Audit Berkas Klaim (/api/claims/upload) dengan file CSV, multipart, & JSON.
3. Endpoint Integrasi Batch Klaim SIMRS / Webhook (/api/claims/batch-audit).
4. Verifikasi Pembobotan Skoring Akurasi AI Ensemble (60% XGBoost : 40% Random Forest).
5. Verifikasi Keberadaan Model Random Forest & XGBoost di Joblib Artifacts.
"""

import os
import sys
import json
import joblib
from fastapi.testclient import TestClient

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app.main import app
from app.engine import VeriKlaimEngine

client = TestClient(app)
engine = VeriKlaimEngine()

def test_1_template_download():
    print("\n--- TEST 1: UNDUH TEMPLATE KLAIM (CSV & JSON) ---")
    
    # 1. Template CSV
    resp_csv = client.get("/api/claims/upload/template?format=csv")
    assert resp_csv.status_code == 200
    assert "no_sep" in resp_csv.text
    assert "SEP-CONTOH-2026-0001" in resp_csv.text
    print("1. Template CSV berhasil diunduh ✅")

    # 2. Template JSON
    resp_json = client.get("/api/claims/upload/template?format=json")
    assert resp_json.status_code == 200
    data = resp_json.json()
    assert isinstance(data, list)
    assert len(data) >= 5
    print("2. Template JSON berhasil diunduh ✅")

def test_2_claim_upload_and_audit():
    print("\n--- TEST 2: UPLOAD & AUDIT KLAIM (CSV & MULTIPART) ---")
    
    sample_csv = (
        "no_sep,id_peserta,tipe_faskes,pelayanan,kode_icd10,nama_diagnosa,kode_inacbg,severity_level,los_hari,biaya_tagih,biaya_riil\n"
        "SEP-UP-001,PST-01,RS Kelas B,RJTL,Z09.8,Follow-up,Q-5-44-0,0,0,207900,207900\n"
        "SEP-UP-002,PST-02,RS Kelas C,RITL,J18.9,Pneumonia,J-4-16-III,3,1,15400000,2400000\n"
        "SEP-UP-003,PST-03,RS Kelas B,RITL,I10,Hipertensi,I-4-17-I,1,0,3200000,3200000\n"
    )

    # 1. Upload Direct CSV Content
    resp = client.post("/api/claims/upload", content=sample_csv, headers={"content-type": "text/csv"})
    assert resp.status_code == 200
    res = resp.json()
    assert res["status"] == "success"
    assert res["summary"]["total_claims"] == 3
    assert res["summary"]["total_wajar"] == 1
    assert res["summary"]["total_anomali"] == 2
    assert res["summary"]["total_saving_idr"] > 0
    print("1. Direct CSV Upload & Audit: PASSED ✅")

    # 2. Upload Multipart Form Data
    boundary = "----WebKitFormBoundaryUploadTest123"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="klaim_batch_rs.csv"\r\n'
        f"Content-Type: text/csv\r\n\r\n"
        f"{sample_csv}\r\n"
        f"--{boundary}--\r\n"
    ).encode("utf-8")

    resp_multi = client.post(
        "/api/claims/upload",
        content=body,
        headers={"content-type": f"multipart/form-data; boundary={boundary}"}
    )
    assert resp_multi.status_code == 200
    res_multi = resp_multi.json()
    assert res_multi["filename"] == "klaim_batch_rs.csv"
    assert len(res_multi["claims"]) == 3
    print("2. Multipart Form Upload: PASSED ✅")

def test_3_batch_audit_integration_api():
    print("\n--- TEST 3: BATCH AUDIT INTEGRASI SIMRS (JSON WEBHOOK) ---")
    
    payload = [
        {
            "no_sep": "SEP-INT-001",
            "id_peserta": "PST-101",
            "tipe_faskes": "RS Kelas B",
            "pelayanan": "RJTL",
            "kode_icd10": "Z50.1",
            "nama_diagnosa": "Other physical therapy",
            "kode_inacbg": "M-3-16-0",
            "nama_inacbg": "PROSEDUR FISIOTERAPI",
            "severity_level": 0,
            "los_hari": 0,
            "biaya_tagih": 139300,
            "biaya_riil": 139300
        },
        {
            "no_sep": "SEP-INT-002",
            "id_peserta": "PST-102",
            "tipe_faskes": "RS Kelas C",
            "pelayanan": "RITL",
            "kode_icd10": "J18.9",
            "nama_diagnosa": "Pneumonia",
            "kode_inacbg": "J-4-16-III",
            "nama_inacbg": "INFEKSI SALURAN PERNAPASAN BERAT",
            "severity_level": 3,
            "los_hari": 1,
            "biaya_tagih": 16000000,
            "biaya_riil": 2400000
        }
    ]

    resp = client.post("/api/claims/batch-audit", json=payload)
    assert resp.status_code == 200
    res = resp.json()
    assert res["total_claims"] == 2
    assert res["total_wajar"] == 1
    assert res["total_anomali"] == 1
    assert "calibrated_accuracy" in res["ensemble_accuracy"]
    print("Batch Audit Webhook SIMRS: PASSED ✅")

def test_4_ensemble_accuracy_weighting():
    print("\n--- TEST 4: PEMBOBOTAN SKORING AKURASI ENSEMBLE (XGBOOST & RANDOM FOREST) ---")
    
    # 1. Verifikasi Model Joblib memuat kedua model dan konfigurasi ensemble
    art_path = os.path.join(ROOT_DIR, "models", "real_veriklaim_model.joblib")
    assert os.path.exists(art_path)
    artifacts = joblib.load(art_path)

    assert "binary_model" in artifacts, "Model XGBoost tidak ditemukan di artifacts"
    assert "random_forest_model" in artifacts, "Model Random Forest tidak ditemukan di artifacts"
    assert "ensemble_config" in artifacts, "Konfigurasi ensemble tidak ditemukan"

    config = artifacts["ensemble_config"]
    assert config["weights"]["xgboost"] == 0.60
    assert config["weights"]["random_forest"] == 0.40
    print("1. Artifacts Joblib Model XGBoost & Random Forest: TERVERIFIKASI ✅")

    # 2. Verifikasi Hasil Inferensi Engine mencantumkan pembobotan
    res = engine.audit_single_claim({
        "no_sep": "SEP-TEST-ENS-01",
        "pelayanan": "RJTL",
        "kode_icd10": "Z09.8",
        "biaya_tagih": 207900,
        "biaya_riil": 207900,
        "los_hari": 0
    })

    assert "ensemble_weighting" in res, "Field ensemble_weighting hilang dari respons audit"
    ens = res["ensemble_weighting"]
    assert ens["xgboost"]["bobot"] == 0.60
    assert ens["random_forest"]["bobot"] == 0.40
    assert ens["calibrated_accuracy"] == 98.44
    assert "Skor AI" in ens["formula"]
    print(f"2. Calibrated Accuracy: {ens['calibrated_accuracy']}% ({ens['formula']}) ✅")
    print(f"   - XGBoost       : Bobot 60% | Akurasi {ens['xgboost']['akurasi_model']}%")
    print(f"   - Random Forest : Bobot 40% | Akurasi {ens['random_forest']['akurasi_model']}%")

    print("\nSELURUH PENGUJIAN UPLOAD & ENSEMBLE WEIGHTING SUKSES 100%! 🎉")

if __name__ == "__main__":
    test_1_template_download()
    test_2_claim_upload_and_audit()
    test_3_batch_audit_integration_api()
    test_4_ensemble_accuracy_weighting()
