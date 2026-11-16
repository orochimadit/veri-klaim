from fastapi.testclient import TestClient
import os
import sys
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import app.main as m

client = TestClient(m.app)

def test_swagger_and_openapi_docs():
    """Memastikan endpoint dokumentasi OpenAPI & Swagger UI aktif dengan tag lengkap."""
    res_docs = client.get("/docs")
    assert res_docs.status_code == 200

    res_openapi = client.get("/openapi.json")
    assert res_openapi.status_code == 200
    schema = res_openapi.json()
    assert "VeriKlaim API" in schema["info"]["title"]
    tags = [t["name"] for t in schema.get("tags", [])]
    assert "Verifikasi Manual (Human-in-the-Loop)" in tags
    assert "Klaim FKRTL" in tags
    assert "Audit & Deteksi AI" in tags

def test_get_claim_documents():
    """Menguji endpoint pengambilan dokumen pendukung digital klaim."""
    no_sep = "238520624V001808"
    res = client.get(f"/api/claims/{no_sep}/documents?dataset=real")
    assert res.status_code == 200
    payload = res.json()
    assert payload["status"] == "success"
    data = payload["data"]
    assert data["no_sep"] == no_sep
    
    # Periksa bundel dokumen medis
    docs = data["documents"]
    assert "sep" in docs
    assert "resume_medis" in docs
    assert "billing" in docs
    assert "rujukan" in docs

    # Periksa isi SEP
    assert docs["sep"]["no_sep"] == no_sep
    assert "BPJS KESEHATAN" in docs["sep"]["subtitle"]

    # Periksa isi Resume Medis DPJP
    assert "dr." in docs["resume_medis"]["dpjp"]["nama"]
    assert "tanda_vital" in docs["resume_medis"]

    # Periksa Rincian Biaya
    assert len(docs["billing"]["items"]) >= 5
    assert docs["billing"]["total_tarif_inacbg"] > 0

    # Periksa Cross-Check
    assert "check_diagnosa" in data["cross_check"]
    assert "check_los_rawat" in data["cross_check"]

def test_manual_verification_workflow():
    """Menguji siklus verifikasi manual manusia: telaah -> sign-off -> cek di list klaim."""
    test_sep = "238520624V001808"
    
    # 1. Simpan verifikasi manual APPROVED
    verify_payload = {
        "status": "APPROVED",
        "notes": "Telah diverifikasi silang dengan Resume Medis DPJP. Diagnosa kontrol rawat jalan wajar dan layak bayar.",
        "verified_by": "dr. Ali Maulana, M.Kep. (Verifikator Ahli)",
        "checklist": {
            "check_sep": True,
            "check_diagnosa": True,
            "check_prosedur": True,
            "check_los": True,
            "check_rujukan": True,
            "check_billing": True
        }
    }
    post_res = client.post(f"/api/claims/{test_sep}/verify", json=verify_payload)
    assert post_res.status_code == 200
    res_data = post_res.json()
    assert res_data["success"] is True
    assert res_data["data"]["verification_status"] == "APPROVED"
    assert "Layak Bayar" in res_data["data"]["status_label"]

    # 2. Periksa status verifikasi spesifik SEP
    get_res = client.get(f"/api/verifications/{test_sep}")
    assert get_res.status_code == 200
    assert get_res.json()["verification_status"] == "APPROVED"

    # 3. Periksa list claims mengandung status verifikasi
    claims_res = client.get(f"/api/claims?dataset=real&search={test_sep}")
    assert claims_res.status_code == 200
    records = claims_res.json()["data"]
    assert len(records) >= 1
    target = next((r for r in records if r["NO_SEP"] == test_sep), None)
    assert target is not None
    assert target["verification_status"] == "APPROVED"
    assert "Layak Bayar" in target["verification_label"]
    assert target["verified_by"] == "dr. Ali Maulana, M.Kep. (Verifikator Ahli)"

    # 4. Filter verifikasi APPROVED
    filtered_res = client.get("/api/claims?dataset=real&verification_status=APPROVED")
    assert filtered_res.status_code == 200
    assert filtered_res.json()["total"] >= 1

if __name__ == "__main__":
    test_swagger_and_openapi_docs()
    print("Test Swagger Docs: PASSED ✅")
    test_get_claim_documents()
    print("Test Claim Documents: PASSED ✅")
    test_manual_verification_workflow()
    print("Test Manual Verification Workflow: PASSED ✅")
