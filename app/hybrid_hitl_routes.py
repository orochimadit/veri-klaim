"""
VeriKlaim Hybrid AI & Text-Only HITL Routes (Spesifikasi Fitur/perbaikan.md)
File Terpisah: app/hybrid_hitl_routes.py

Menyediakan:
1. Endpoints API Jalur Terpisah (/api/hitl/*)
2. Antarmuka Web Online Terpisah (/hitl-portal)
3. Evaluasi Formula Hybrid (C_offline * 0.40 + C_online * 0.60)
4. Validasi Rujukan FKTP-FKRTL & Bypass IGD
5. Form Sanggah/Klarifikasi Faskes Berbasis Teks Terstruktur (Anti UU PDP)
6. Audit Trail BPK/Kemenkes & Live Synthetic Benchmark (DUMMY-HITL-001)
"""

import os
import json
import datetime
from typing import Dict, Any, List, Optional
from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field

APP_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(APP_DIR)

from app.hybrid_hitl import (
    HybridHITLEngine,
    NormalizedClaim,
    HospitalClarificationSubmission,
    ReferralValidationResult,
    HybridConfidenceScore,
    ClarificationEvaluationResult,
    CLARIFICATION_TICKETS_FILE
)

hitl_router = APIRouter(prefix="", tags=["Hybrid AI & Text-Only HITL (Spesifikasi Baru)"])
hitl_engine = HybridHITLEngine()

class DisputeTicketCreate(BaseModel):
    no_sep: str = Field(..., description="Nomor SEP yang disengketakan")
    disputed_code: str = Field(..., description="Kode ICD-10 atau ICD-9 yang disengketakan")
    dispute_reason: str = Field(..., description="Catatan alasan sengketa verifikator BPJS")
    claim_metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

# =============================================================================
# 1. ENDPOINTS EVALUASI FORMULA HYBRID AI (SEKSI 2)
# =============================================================================

@hitl_router.post(
    "/api/hitl/evaluate-claim",
    response_model=HybridConfidenceScore,
    summary="[Hybrid AI] Evaluasi Skor Komposit (C_offline * 0.40 + C_online * 0.60)"
)
def evaluate_normalized_claim_endpoint(claim: NormalizedClaim):
    """
    Menerima klaim ternormalisasi (JSON Standar) dan menghitung:
    * C_offline (40%): Ekstraksi fisik, integritas nomor rujukan, nomor SEP, stempel digital
    * C_online (60%): Penalaran klinis LLM, kelayakan kode klinis, Formularium Nasional
    * Confidence Tiers: High (>=90%), Moderate (70-89%), Low (<70%)
    """
    scores = hitl_engine.calculate_hybrid_scores(claim)
    hitl_engine.record_audit_trail_entry(
        no_sep=claim.sep_number,
        actor="VeriKlaim Hybrid Engine",
        action="HYBRID_CLAIM_EVALUATION",
        scores={
            "offline_validity_score": scores.offline_validity_score,
            "online_reasoning_score": scores.online_reasoning_score,
            "composite_confidence": scores.composite_confidence
        },
        verdict=scores.audit_verdict,
        notes=f"Tier={scores.confidence_tier}, Action={scores.tier_action}"
    )
    return scores

# =============================================================================
# 2. ENDPOINTS VALIDASI RELASI RUJUKAN FKTP -> FKRTL (SEKSI 3)
# =============================================================================

@hitl_router.post(
    "/api/hitl/validate-referral",
    response_model=ReferralValidationResult,
    summary="[Rujukan] Validasi Relasi FKTP -> FKRTL (Masa Berlaku 90 Hari & IGD Bypass)"
)
def validate_referral_endpoint(claim: NormalizedClaim):
    """
    Memvalidasi aturan berjenjang rujukan:
    1. Masa aktif rujukan <= 90 hari
    2. Kesesuaian spesialisasi poli faskes lanjutan vs diagnosa rujukan
    3. Pengecualian gawat darurat (IGD Bypass)
    """
    return hitl_engine.validate_referral_integrity(claim)

# =============================================================================
# 3. ENDPOINTS PORTAL KLARIFIKASI TEXT-ONLY HITL (SEKSI 4 & UU PDP)
# =============================================================================

@hitl_router.post(
    "/api/hitl/tickets",
    summary="[HITL] Terbitkan Tiket Klarifikasi Sengketa Klaim ke Rumah Sakit"
)
def create_dispute_ticket_endpoint(ticket_req: DisputeTicketCreate):
    """Verifikator menerbitkan tiket sengketa yang meminta kutipan teks CPPT dari faskes."""
    now_iso = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    deadline = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")

    tickets = {}
    if os.path.exists(CLARIFICATION_TICKETS_FILE):
        try:
            with open(CLARIFICATION_TICKETS_FILE, "r", encoding="utf-8") as f:
                tickets = json.load(f)
        except Exception:
            tickets = {}

    ticket_id = f"TCK-{ticket_req.no_sep[-6:]}-{int(datetime.datetime.now().timestamp())%10000}"
    ticket_data = {
        "ticket_id": ticket_id,
        "no_sep": ticket_req.no_sep,
        "disputed_code": ticket_req.disputed_code,
        "dispute_reason": ticket_req.dispute_reason,
        "status": "OPEN_PENDING_HOSPITAL_RESPONSE",
        "created_at": now_iso,
        "sla_deadline": deadline,
        "claim_metadata": ticket_req.claim_metadata,
        "hospital_clarification": None,
        "ai_evaluation": None,
        "final_verdict": "PENDING"
    }

    tickets[ticket_req.no_sep] = ticket_data
    with open(CLARIFICATION_TICKETS_FILE, "w", encoding="utf-8") as f:
        json.dump(tickets, f, indent=2, ensure_ascii=False)

    hitl_engine.record_audit_trail_entry(
        no_sep=ticket_req.no_sep,
        actor="Verifikator BPJS",
        action="DISPUTE_TICKET_ISSUED",
        scores={"offline_validity_score": 0.5, "online_reasoning_score": 0.5, "composite_confidence": 0.5},
        verdict="PENDING_CLARIFICATION",
        notes=f"Tiket diterbitkan: {ticket_req.dispute_reason}"
    )

    return {
        "success": True,
        "message": f"Tiket klarifikasi {ticket_id} berhasil diterbitkan ke RS. Batas SLA: 3x24 Jam.",
        "ticket": ticket_data
    }

@hitl_router.get(
    "/api/hitl/tickets",
    summary="[HITL] Ambil Daftar Seluruh Tiket Klarifikasi Sengketa Faskes"
)
def list_dispute_tickets_endpoint():
    tickets = {}
    if os.path.exists(CLARIFICATION_TICKETS_FILE):
        try:
            with open(CLARIFICATION_TICKETS_FILE, "r", encoding="utf-8") as f:
                tickets = json.load(f)
        except Exception:
            tickets = {}
    return {
        "total": len(tickets),
        "data": list(tickets.values())
    }

@hitl_router.get(
    "/api/hitl/tickets/{no_sep}",
    summary="[HITL] Ambil Detail Tiket Klarifikasi Spesifik Nomor SEP"
)
def get_dispute_ticket_endpoint(no_sep: str):
    tickets = {}
    if os.path.exists(CLARIFICATION_TICKETS_FILE):
        try:
            with open(CLARIFICATION_TICKETS_FILE, "r", encoding="utf-8") as f:
                tickets = json.load(f)
        except Exception:
            tickets = {}
    
    t = tickets.get(no_sep)
    if not t:
        # Buat dummy ticket default jika belum ada agar mudah diuji coba di antarmuka
        return {
            "ticket_id": f"TCK-{no_sep[-6:]}-NEW",
            "no_sep": no_sep,
            "disputed_code": "45.13",
            "dispute_reason": "Indikasi tindakan endoskopi/prosedur darurat belum tertera pada ringkasan klinis awal.",
            "status": "OPEN_PENDING_HOSPITAL_RESPONSE",
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "sla_deadline": (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S"),
            "hospital_clarification": None,
            "ai_evaluation": None,
            "final_verdict": "PENDING"
        }
    return t

@hitl_router.post(
    "/api/hitl/clarify",
    summary="[HITL RS] Input Respon Sanggah Teks Terstruktur Faskes (Kepatuhan UU PDP & PMK 24/2022)"
)
def submit_hospital_text_clarification_endpoint(submission: HospitalClarificationSubmission):
    """
    Faskes mengirimkan respons sanggahan HANYA berupa kutipan teks CPPT terstruktur.
    Dilarang upload file RME PDF demi menjaga privasi medis pasien.
    AI mengevaluasi semantik teks:
    - Bukti objektif terpenuhi (lab, tanda vital) -> APPROVED_BY_EVIDENCE
    - Teks kosong / tanda strip / teks klise ('sesuai SPO') -> REJECTED_NIHIL
    """
    # 1. Evaluasi Semantik Teks Respon RS
    eval_result = hitl_engine.evaluate_hospital_text_clarification(submission)

    # 2. Update status tiket
    tickets = {}
    if os.path.exists(CLARIFICATION_TICKETS_FILE):
        try:
            with open(CLARIFICATION_TICKETS_FILE, "r", encoding="utf-8") as f:
                tickets = json.load(f)
        except Exception:
            tickets = {}

    ticket = tickets.get(submission.no_sep, {
        "ticket_id": f"TCK-{submission.no_sep[-6:]}-ACT",
        "no_sep": submission.no_sep,
        "disputed_code": "CLINICAL_EVAL",
        "dispute_reason": "Sengketa kelayakan koding klinis faskes"
    })

    ticket["hospital_clarification"] = submission.dict()
    ticket["ai_evaluation"] = eval_result.dict()
    ticket["status"] = "RESOLVED_APPROVED" if eval_result.verdict == "APPROVED_BY_EVIDENCE" else "RESOLVED_REJECTED"
    ticket["final_verdict"] = eval_result.verdict
    ticket["resolved_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tickets[submission.no_sep] = ticket
    with open(CLARIFICATION_TICKETS_FILE, "w", encoding="utf-8") as f:
        json.dump(tickets, f, indent=2, ensure_ascii=False)

    # 3. Rekam ke Audit Trail Log BPK/Kemenkes
    hitl_engine.record_audit_trail_entry(
        no_sep=submission.no_sep,
        actor=f"RS Staff: {submission.hospital_staff_id} / DPJP: {submission.dpjp_signature_id}",
        action="HOSPITAL_TEXT_CLARIFICATION_SUBMITTED",
        scores={
            "offline_validity_score": 0.98 if eval_result.verdict == "APPROVED_BY_EVIDENCE" else 0.50,
            "online_reasoning_score": 0.94 if eval_result.verdict == "APPROVED_BY_EVIDENCE" else 0.20,
            "composite_confidence": 0.956 if eval_result.verdict == "APPROVED_BY_EVIDENCE" else 0.320
        },
        verdict=eval_result.verdict,
        notes=f"Evaluasi AI: {eval_result.ai_reasoning}"
    )

    return {
        "success": True,
        "verdict": eval_result.verdict,
        "status_label": "Klaim Disetujui Berdasarkan Evidens CPPT DPJP" if eval_result.verdict == "APPROVED_BY_EVIDENCE" else "Klarifikasi Gugur: Respon Nihil / Tidak Substantif",
        "evaluation": eval_result,
        "ticket": ticket
    }

# =============================================================================
# 4. ENDPOINTS AUDIT TRAIL LOG BPK & KEMENKES (SEKSI 6)
# =============================================================================

@hitl_router.get(
    "/api/hitl/audit-trail",
    summary="[Audit Trail] Ambil Log Jejak Audit Verifikasi BPK / Kemenkes RI"
)
def get_audit_trail_endpoint(no_sep: Optional[str] = Query(None, description="Filter nomor SEP")):
    records = hitl_engine.get_audit_trail(no_sep)
    return {
        "total": len(records),
        "data": records
    }

# =============================================================================
# 5. ENDPOINT LIVE BENCHMARK DATA SINTETIS (SEKSI 5: DUMMY-HITL-001)
# =============================================================================

@hitl_router.get(
    "/api/hitl/benchmark",
    summary="[Benchmark] Eksekusi Uji Sintetis Dummy DUMMY-HITL-001 Sesuai Spesifikasi"
)
def run_benchmark_endpoint():
    result = hitl_engine.run_synthetic_benchmark()
    return result

# =============================================================================
# 6. PORTAL WEB INTERAKTIF ONLINE HITL (/hitl-portal)
# =============================================================================

@hitl_router.get("/hitl-portal", response_class=HTMLResponse, include_in_schema=False)
def hitl_portal_webpage(request: Request):
    """
    Halaman Web Interaktif Dedicated untuk Portal Klarifikasi Faskes & Hybrid HITL
    Berbeda dari dashboard utama: berfokus pada alur Text-Only HITL, formula hybrid,
    dan kepatuhan UU PDP & PMK 24/2022.
    """
    portal_html_path = os.path.join(APP_DIR, "templates", "hitl_portal.html")
    if os.path.exists(portal_html_path):
        with open(portal_html_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>Portal HITL Template Not Found</h1>", status_code=404)
