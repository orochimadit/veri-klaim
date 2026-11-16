"""
Unit & Integration Test Suite untuk Hybrid AI & Text-Only HITL
Spesifikasi: Fitur/perbaikan.md
Pengujian Komprehensif:
1. Normalisasi Skema Klaim & Formula Hybrid AI (40:60)
2. Kategori Keyakinan AI (Confidence Tiers)
3. Relasi Rujukan FKTP -> FKRTL (90 Hari, Kesesuaian Poli, IGD Bypass)
4. Evaluasi Semantik Respon RS Ber-Evidens vs Nihil (UU PDP & PMK 24/2022)
5. Audit Trail Log Kemenkes/BPK
6. Benchmark Data Sintetis DUMMY-HITL-001
7. Endpoints REST API & Portal Web Online (/hitl-portal)
"""

import os
import sys
import json
from fastapi.testclient import TestClient

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app.main import app
from app.hybrid_hitl import (
    HybridHITLEngine,
    NormalizedClaim,
    DiagnosesBlock,
    PrescriptionItem,
    HospitalClarificationSubmission
)

client = TestClient(app)
engine = HybridHITLEngine()

def test_1_hybrid_scoring_formula_and_tiers():
    """Menguji formula: Confidence Akhir = (C_offline * 0.40) + (C_online * 0.60)"""
    claim = NormalizedClaim(
        claim_id="TEST-HYBRID-01",
        sep_number="0089R0011126V000123",
        referral_number="0112B0010926P000456",
        faskes_origin_type="FKTP",
        faskes_destination_type="FKRTL",
        tgl_sep="2026-11-10",
        tgl_rujukan="2026-10-10",
        poli_tujuan="Poli Penyakit Dalam",
        flag_igd=False,
        diagnoses=DiagnosesBlock(primary="I10", secondary=["E11.9"]),
        procedures=["89.52"],
        prescriptions=[PrescriptionItem(recipe_id="RXP-01", drug_name="Amlodipine 10mg", qty=30)]
    )

    scores = engine.calculate_hybrid_scores(claim)
    assert 0.0 <= scores.offline_validity_score <= 1.0
    assert 0.0 <= scores.online_reasoning_score <= 1.0
    
    expected_composite = round((scores.offline_validity_score * 0.40) + (scores.online_reasoning_score * 0.60), 3)
    assert abs(scores.composite_confidence - expected_composite) < 0.005

    # Verifikasi Tiers
    if scores.composite_confidence >= 0.90:
        assert scores.confidence_tier == "HIGH_CONFIDENCE"
        assert scores.tier_action == "AUTO_APPROVAL_OR_REJECT"
    elif scores.composite_confidence >= 0.70:
        assert scores.confidence_tier == "MODERATE_CONFIDENCE"
        assert scores.tier_action == "HITL_TRIAGE_L1"
    else:
        assert scores.confidence_tier == "LOW_CONFIDENCE"
        assert scores.tier_action == "FULL_AUDIT_TICKET"
    print("Test 1 (Formula Hybrid 40:60 & Tiers): PASSED ✅")

def test_2_referral_integrity_rules():
    """Menguji aturan rujukan: masa aktif 90 hari, kesesuaian poli, dan bypass IGD"""
    # Kasus A: Rujukan Valid (30 hari, diagnosa I10 ke Poli Penyakit Dalam)
    claim_valid = NormalizedClaim(
        claim_id="TEST-REF-VALID",
        sep_number="0089R0011126V000100",
        referral_number="0112B0010926P000200",
        tgl_sep="2026-11-10",
        tgl_rujukan="2026-10-10",
        poli_tujuan="Poli Penyakit Dalam",
        flag_igd=False,
        diagnoses=DiagnosesBlock(primary="I10", secondary=[])
    )
    res_valid = engine.validate_referral_integrity(claim_valid)
    assert res_valid.is_valid is True
    assert res_valid.within_90_days is True
    assert res_valid.status_code == "REFERRAL_VALID"

    # Kasus B: Rujukan Kedaluwarsa (> 90 hari, misal 120 hari)
    claim_expired = NormalizedClaim(
        claim_id="TEST-REF-EXPIRED",
        sep_number="0089R0011126V000101",
        referral_number="0112B0010926P000201",
        tgl_sep="2026-11-10",
        tgl_rujukan="2026-06-01",
        poli_tujuan="Poli Penyakit Dalam",
        flag_igd=False,
        diagnoses=DiagnosesBlock(primary="I10", secondary=[])
    )
    res_expired = engine.validate_referral_integrity(claim_expired)
    assert res_expired.is_valid is False
    assert res_expired.within_90_days is False
    assert "EXPIRED" in res_expired.status_code

    # Kasus C: IGD Emergency Bypass (Rujukan > 90 hari tetapi flag_igd = True)
    claim_igd = NormalizedClaim(
        claim_id="TEST-REF-IGD",
        sep_number="0089R0011126V000102",
        referral_number="0112B0010926P000202",
        tgl_sep="2026-11-10",
        tgl_rujukan="2026-05-01",
        poli_tujuan="Instalasi Gawat Darurat",
        flag_igd=True,
        diagnoses=DiagnosesBlock(primary="I21.9", secondary=[])
    )
    res_igd = engine.validate_referral_integrity(claim_igd)
    assert res_igd.is_valid is True
    assert res_igd.igd_bypass is True
    assert res_igd.status_code == "IGD_EMERGENCY_BYPASS"
    print("Test 2 (Relasi Rujukan 90 Hari & IGD Bypass): PASSED ✅")

def test_3_semantic_evidence_evaluation():
    """Menguji pembedaan teks respon ber-evidens vs nihil (Kepatuhan UU PDP)"""
    # Kasus A: Ada Evidens Klinis Objektif (Hb drop, hematemesis, tindakan EGD darurat)
    sub_evidence = HospitalClarificationSubmission(
        no_sep="0089R0011126V999001",
        timestamp_entry="2026-11-10T10:15:00+07:00",
        dpjp_signature_id="DPJP-SPPD-8821",
        clinical_evidence_snippet="Pasien mengalami hematemesis melena, Hb turun ke 7.8 g/dL, TD 90/60 mmHg. Dilakukan EGD hemostasis darurat injeksi adrenalin."
    )
    res_ev = engine.evaluate_hospital_text_clarification(sub_evidence)
    assert res_ev.is_nihil is False
    assert res_ev.verdict == "APPROVED_BY_EVIDENCE"
    assert "hemoglobin" in res_ev.lab_values_found
    assert res_ev.compliance_score_adjustment > 0

    # Kasus B: Nihil 1 (Hanya Strip '-')
    sub_dash = HospitalClarificationSubmission(
        no_sep="0089R0011126V999002",
        timestamp_entry="2026-11-10T10:15:00+07:00",
        dpjp_signature_id="DPJP-SPPD-8821",
        clinical_evidence_snippet="-"
    )
    res_dash = engine.evaluate_hospital_text_clarification(sub_dash)
    assert res_dash.is_nihil is True
    assert res_dash.verdict == "REJECTED_NIHIL"

    # Kasus C: Nihil 2 (Teks Klise Formalitas 'Sudah sesuai SPO')
    sub_cliche = HospitalClarificationSubmission(
        no_sep="0089R0011126V999003",
        timestamp_entry="2026-11-10T10:15:00+07:00",
        dpjp_signature_id="DPJP-SPPD-8821",
        clinical_evidence_snippet="Sudah sesuai SPO"
    )
    res_cliche = engine.evaluate_hospital_text_clarification(sub_cliche)
    assert res_cliche.is_nihil is True
    assert res_cliche.verdict == "REJECTED_NIHIL"
    print("Test 3 (Evaluasi Semantik Respon Evidens vs Nihil): PASSED ✅")

def test_4_synthetic_dummy_benchmark():
    """Menguji eksekusi benchmark data sintetis DUMMY-HITL-001 dari Seksi 5 Fitur/perbaikan.md"""
    res = engine.run_synthetic_benchmark()
    assert res["test_case_id"] == "DUMMY-HITL-001"
    assert res["benchmark_status"] == "PASSED"
    assert res["evaluated_result"]["audit_verdict"] == "APPROVED_BY_EVIDENCE"
    assert res["evaluated_result"]["composite_confidence"] >= 0.90
    print("Test 4 (Benchmark DUMMY-HITL-001): PASSED ✅")

def test_5_api_endpoints_and_hitl_portal():
    """Menguji seluruh endpoint REST API dan halaman web /hitl-portal"""
    # 1. Halaman Web Portal HITL
    resp_portal = client.get("/hitl-portal")
    assert resp_portal.status_code == 200
    assert "Portal Klarifikasi Faskes" in resp_portal.text
    assert "UU No. 27/2022" in resp_portal.text

    # 2. Endpoint Evaluasi Hybrid
    payload_claim = {
        "claim_id": "CLM-API-01",
        "sep_number": "0089R0011126V000123",
        "referral_number": "0112B0010926P000456",
        "faskes_origin_type": "FKTP",
        "faskes_destination_type": "FKRTL",
        "tgl_sep": "2026-11-10",
        "tgl_rujukan": "2026-10-10",
        "poli_tujuan": "Poli Penyakit Dalam",
        "flag_igd": False,
        "diagnoses": { "primary": "I10", "secondary": [] }
    }
    resp_eval = client.post("/api/hitl/evaluate-claim", json=payload_claim)
    assert resp_eval.status_code == 200
    assert "composite_confidence" in resp_eval.json()

    # 3. Endpoint Validasi Rujukan
    resp_ref = client.post("/api/hitl/validate-referral", json=payload_claim)
    assert resp_ref.status_code == 200
    assert resp_ref.json()["is_valid"] is True

    # 4. Endpoint Submit Sanggah Teks RS
    payload_clarify = {
        "no_sep": "0089R0011126V000123",
        "timestamp_entry": "2026-11-10T10:15:00+07:00",
        "dpjp_signature_id": "DPJP-TEST-01",
        "hospital_staff_id": "STAFF-01",
        "clinical_evidence_snippet": "Perdarahan gastrointestinal masif, Hb 7.2 g/dL, TD 90/60 mmHg. EGD darurat berhasil hemostasis."
    }
    resp_clarify = client.post("/api/hitl/clarify", json=payload_clarify)
    assert resp_clarify.status_code == 200
    assert resp_clarify.json()["verdict"] == "APPROVED_BY_EVIDENCE"

    # 5. Endpoint Audit Trail Log
    resp_audit = client.get("/api/hitl/audit-trail?no_sep=0089R0011126V000123")
    assert resp_audit.status_code == 200
    assert resp_audit.json()["total"] >= 1

    # 6. Endpoint Live Benchmark
    resp_bm = client.get("/api/hitl/benchmark")
    assert resp_bm.status_code == 200
    assert resp_bm.json()["benchmark_status"] == "PASSED"

    # 7. Endpoint Terima Klarifikasi Teks Faskes Langsung (POST /api/claims/{no_sep}/clarify-text)
    resp_text_claim = client.post("/api/claims/0089R0011126V000123/clarify-text", json={
        "no_sep": "0089R0011126V000123",
        "clinical_evidence_snippet": "Pasien syok hipovolemik, Hb 6.8 g/dL, TD 80/50. Dilakukan transfusi dan hemostasis segera.",
        "dpjp_signature_id": "dr. Sutrisno, Sp.PD (DPJP-SPPD-99)",
        "timestamp_entry": "2026-11-10 11:00:00"
    })
    assert resp_text_claim.status_code == 200
    assert resp_text_claim.json()["success"] is True
    assert resp_text_claim.json()["verdict"] == "APPROVED_BY_EVIDENCE"
    assert resp_text_claim.json()["verification_status"] == "APPROVED"

    print("Test 5 (API Endpoints & HITL Portal): PASSED ✅")

if __name__ == "__main__":
    test_1_hybrid_scoring_formula_and_tiers()
    test_2_referral_integrity_rules()
    test_3_semantic_evidence_evaluation()
    test_4_synthetic_dummy_benchmark()
    test_5_api_endpoints_and_hitl_portal()
    print("\nSELURUH PENGUJIAN HYBRID AI & TEXT-ONLY HITL BERHASIL 100%! 🎉")
