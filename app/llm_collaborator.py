"""
VeriKlaim LLM Collaborator Module (Kolaborasi ML + LLM & Graceful Fallback)
Mengimplementasikan Fitur 02 dan Fitur 04:
- Fitur 02: Kolaborasi ML + LLM (ML menghitung angka, LLM menerjemahkan hasil angka & teks medis jadi narasi mudah dibaca).
- Fitur 04: Sistem Tetap Jalan Meski API LLM Mati (Graceful Fallback menjamin respons HTTP 200 OK jika API key kosong/koneksi gagal).
"""

import os
import time
import json
import logging
from typing import Dict, Any, Optional

try:
    import httpx
except ImportError:
    httpx = None

logger = logging.getLogger("veriklaim.llm")

DEFAULT_GEMINI_KEY = "AQ.Ab8RN6JUxwdaI2adp4JJAXIylvoQQfqcX-qjEc05OJDyF8-kgQ"

class LLMCollaborator:
    """
    Orkestrator Kolaborasi ML + LLM dengan Fallback Otomatis & Manual Toggle Switch
    """

    def __init__(self, timeout_sec: float = 3.5):
        self.gemini_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or DEFAULT_GEMINI_KEY
        self.openai_key = os.environ.get("OPENAI_API_KEY", "")
        self.timeout_sec = timeout_sec
        self.mode = "ONLINE"  # Pilihan: 'ONLINE', 'OFFLINE', 'AUTO'

    def set_mode(self, mode: str) -> str:
        """
        Mengubah mode AI secara manual ('ONLINE', 'OFFLINE', 'AUTO')
        """
        m = str(mode).strip().upper()
        if m in ["ONLINE", "OFFLINE", "AUTO"]:
            self.mode = m
        return self.mode

    def get_status(self) -> Dict[str, Any]:
        """
        Mengambil status kesiapan LLM dan mode yang sedang aktif
        """
        is_online = self.mode in ["ONLINE", "AUTO"]
        has_key = bool(self.gemini_key or self.openai_key)
        return {
            "mode": self.mode,
            "is_online_mode": is_online,
            "has_api_key": has_key,
            "active_provider": "Gemini-1.5-Flash (LLM Cloud)" if (is_online and has_key) else "Deterministic Permenkes Rule Engine (Offline Fallback)",
            "timeout_sec": self.timeout_sec
        }

    def is_llm_available(self) -> bool:
        if self.mode == "OFFLINE":
            return False
        return bool(self.gemini_key or self.openai_key)

    def generate_clinical_narrative(
        self,
        claim: Dict[str, Any],
        audit_result: Dict[str, Any],
        force_mode: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Menghasilkan narasi audit forensik medis.
        Mendukung Manual Toggle (ONLINE vs OFFLINE) & Graceful Fallback otomatis.
        """
        t0 = time.perf_counter()
        active_mode = (force_mode or self.mode).upper()

        # 1. Jika mode manual OFFLINE dipilih, langsung gunakan Deterministic Permenkes Engine
        if active_mode == "OFFLINE":
            fallback_narrative = self._generate_fallback_narrative(claim, audit_result)
            latency = (time.perf_counter() - t0) * 1000
            return {
                "narrative": fallback_narrative,
                "provider": "Deterministic Permenkes Rule Engine (Manual Offline Mode)",
                "is_fallback": True,
                "status_badge": "AI Offline (Manual Mode)",
                "mode": "OFFLINE",
                "latency_ms": round(latency, 2)
            }

        # 2. Mode ONLINE: Coba panggil Gemini Cloud LLM
        gemini_error = None
        if self.gemini_key and httpx:
            try:
                narrative = self._call_gemini(claim, audit_result)
                if narrative:
                    latency = (time.perf_counter() - t0) * 1000
                    return {
                        "narrative": narrative,
                        "provider": "Gemini-3.5-Flash (LLM Cloud)",
                        "is_fallback": False,
                        "status_badge": "AI Online (Gemini Active)",
                        "mode": "ONLINE",
                        "latency_ms": round(latency, 2)
                    }
            except Exception as e:
                gemini_error = str(e)
                logger.warning(f"[LLMCollaborator] Gemini call failed: {e}. Activating graceful fallback.")

        # Coba OpenAI jika Gemini tidak tersedia atau gagal
        if self.openai_key and httpx:
            try:
                narrative = self._call_openai(claim, audit_result)
                if narrative:
                    latency = (time.perf_counter() - t0) * 1000
                    return {
                        "narrative": narrative,
                        "provider": "OpenAI GPT (LLM Cloud)",
                        "is_fallback": False,
                        "status_badge": "AI Online (OpenAI Active)",
                        "mode": "ONLINE",
                        "latency_ms": round(latency, 2)
                    }
            except Exception as e:
                logger.warning(f"[LLMCollaborator] OpenAI call failed: {e}. Activating graceful fallback.")

        # 3. Fitur 04: Graceful Fallback Engine (Deterministik, Cepat, Tanpa Crash)
        fallback_narrative = self._generate_fallback_narrative(claim, audit_result)
        latency = (time.perf_counter() - t0) * 1000
        return {
            "narrative": fallback_narrative,
            "provider": "Deterministic Permenkes Rule Engine (Graceful Fallback)",
            "is_fallback": True,
            "status_badge": "Graceful Fallback (HTTP 200 OK)",
            "mode": active_mode,
            "fallback_reason": gemini_error or "LLM Offline / Unreachable",
            "latency_ms": round(latency, 2)
        }

    def _call_gemini(self, claim: Dict[str, Any], audit: Dict[str, Any]) -> Optional[str]:
        # Gunakan model generasi terkini yang didukung API key: gemini-3.5-flash-lite
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={self.gemini_key}"
        prompt = self._build_prompt(claim, audit)
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "maxOutputTokens": 280,
                "temperature": 0.2
            }
        }
        with httpx.Client(timeout=self.timeout_sec) as client:
            resp = client.post(url, json=payload)
            if resp.status_code == 200:
                data = resp.json()
                return data["candidates"][0]["content"]["parts"][0]["text"].strip()
            else:
                logger.warning(f"[Gemini API Error] status={resp.status_code}: {resp.text[:200]}")
                raise RuntimeError(f"Gemini API status {resp.status_code}: {resp.text[:100]}")

    def _call_openai(self, claim: Dict[str, Any], audit: Dict[str, Any]) -> Optional[str]:
        url = "https://api.openai.com/v1/chat/completions"
        prompt = self._build_prompt(claim, audit)
        headers = {
            "Authorization": f"Bearer {self.openai_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "Anda adalah asisten audit klaim BPJS Kesehatan yang bertugas menerjemahkan temuan numerik model AI menjadi ringkasan klinis yang ringkas, tegas, dan mudah dipahami verifikator."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 250,
            "temperature": 0.2
        }
        with httpx.Client(timeout=self.timeout_sec) as client:
            resp = client.post(url, headers=headers, json=payload)
            if resp.status_code == 200:
                data = resp.json()
                return data["choices"][0]["message"]["content"].strip()
        return None

    def _build_prompt(self, claim: Dict[str, Any], audit: Dict[str, Any]) -> str:
        extra_info = []
        if audit.get("topup_flag"):
            extra_info.append(f"Top-Up Special CMG: {claim.get('topup_special_cmg')} senilai Rp {claim.get('biaya_topup', 0):,}")
        if audit.get("coding_drift_flag"):
            extra_info.append(f"Disparitas Koding: Masuk IGD diagnosa {claim.get('diag_masuk_icd10')}, keluar klaim diagnosa {claim.get('kode_icd10')}")
        if audit.get("cost_velocity_ratio", 1.0) >= 3.0:
            extra_info.append(f"Cost Velocity: {audit.get('cost_velocity_ratio')}x di atas rata-rata RS sekelas")
        if audit.get("unreferral_flag"):
            extra_info.append("Bypass Rujukan: Rawat Jalan non-darurat tanpa surat rujukan FKTP yang sah")
        if audit.get("capability_mismatch"):
            extra_info.append(f"Mismatch Kewenangan: Tindakan canggih diajukan faskes tipe {claim.get('tipe_faskes')} / {claim.get('jenis_faskes')}")

        extra_text = ("\n- Indikasi Khusus: " + " | ".join(extra_info)) if extra_info else ""

        return (
            f"Anda adalah dokter verifikator senior BPJS Kesehatan. Buat catatan telaah medis singkat dan wajar (2-3 kalimat santai tapi profesional, seperti catatan verifikator rumah sakit sungguhan, jangan kaku atau terdengar seperti robot/AI) untuk klaim ini:\n"
            f"- Nomor SEP: {claim.get('no_sep')}\n"
            f"- Status: {audit.get('status_label')} ({audit.get('fraud_type')})\n"
            f"- Diagnosa: {claim.get('nama_diagnosa')} ({claim.get('kode_icd10')})\n"
            f"- INA-CBG: {claim.get('kode_inacbg')} (Level {claim.get('severity_level')})\n"
            f"- Lama Rawat: {claim.get('los_hari')} hari | Pelayanan: {claim.get('pelayanan', 'RITL')}\n"
            f"- Biaya Tagih: Rp {claim.get('biaya_tagih', 0):,} | Biaya Riil RS: Rp {claim.get('biaya_riil', 0):,}\n"
            f"- Temuan: {'; '.join(audit.get('audit_findings', []))}{extra_text}\n\n"
            "Tulis langsung intinya: kenapa klaim ini lolos atau ditahan, dan apa langkah konkret yang harus diambil petugas (misal: minta berkas DPJP, turunkan level, batalkan biaya implan, atau setujui klaim). Hindari kata-kata klise robot seperti 'Berdasarkan analisis machine learning'."
        )

    def _generate_fallback_narrative(self, claim: Dict[str, Any], audit: Dict[str, Any]) -> str:
        """
        Fallback Engine: Menghasilkan catatan telaah verifikator yang wajar dan mudah dibaca
        mencakup 6 klaster deteksi fraud sesuai Permenkes.
        """
        is_fraud = audit.get("is_fraud", 0)
        fraud_type = audit.get("fraud_type", "NORMAL")
        no_sep = claim.get("no_sep", "SEP")
        diagnosa = claim.get("nama_diagnosa", claim.get("kode_icd10", "Medis"))
        tagih = claim.get("biaya_tagih", 0)
        riil = claim.get("biaya_riil", 0)
        los = claim.get("los_hari", 0)
        sev = claim.get("severity_level", 1)

        if not is_fraud or fraud_type == "NORMAL":
            return (
                f"Klaim SEP {no_sep} dinyatakan sesuai standar. Diagnosa {diagnosa} dengan rawat inap {los} hari "
                f"dan biaya riil Rp {riil:,.0f} selaras dengan tarif INA-CBG. Klaim layak disetujui (FPK diterbitkan)."
            )

        # Klaster 1: Special CMG Top-Up
        if audit.get("topup_flag"):
            topup_name = claim.get("topup_special_cmg", "Special CMG")
            topup_val = claim.get("biaya_topup", 0)
            return (
                f"Klaim SEP {no_sep} ditahan (Phantom Top-Up): Ada tagihan tambahan {topup_name} senilai Rp {topup_val:,.0f}, "
                f"tapi tidak tercatat prosedur operasi atau intervensi klinis yang sesuai di lembar tindakan. Batalkan komponen Special CMG "
                f"dan kembalikan ke tarif paket dasar sesuai Permenkes 26/2021 Pasal 16."
            )

        # Klaster 2: Coding Drift
        if audit.get("coding_drift_flag"):
            diag_masuk = claim.get("diag_masuk_icd10", "gejala awal")
            return (
                f"Klaim SEP {no_sep} ditahan (Disparitas Koding Masuk vs Keluar): Pasien masuk dengan diagnosa ringan {diag_masuk}, "
                f"namun ditagihkan sebagai diagnosa berat {diagnosa} tanpa hasil penunjang/endoskopi pendukung dan rawat inap hanya {los} hari. "
                f"Lakukan koreksi koding ke diagnosa awal sesuai resume medis DPJP (Permenkes 26/2021 Pasal 14)."
            )

        # Klaster 4: Bypass Rujukan RJTL
        if audit.get("unreferral_flag"):
            return (
                f"Klaim SEP {no_sep} ditahan (Bypass Rujukan Berjenjang): Pelayanan rawat jalan di rumah sakit tidak menyertakan "
                f"surat rujukan FKTP yang sah untuk kasus non-darurat. Klaim ditolak sementara merujuk Permenkes 001/2012 dan Peraturan BPJS No. 1/2014."
            )

        # Klaster 6: Hospital Capability Mismatch
        if audit.get("capability_mismatch"):
            proc = claim.get("kode_icd9", "Tindakan canggih")
            tipe_rs = claim.get("tipe_faskes", "RS")
            return (
                f"Klaim SEP {no_sep} ditahan (Mismatch Sarana Faskes): Prosedur bedah canggih ({proc}) diajukan oleh faskes tipe {tipe_rs} "
                f"yang tidak memenuhi izin kamar operasi atau tenaga sub-spesialis sesuai Permenkes 3/2020. Blokir persetujuan klaim dan alihkan ke Tim Satgas Anti-Fraud."
            )

        # Klaster 3: Cost Velocity
        if audit.get("cost_velocity_ratio", 1.0) >= 3.0:
            ratio = audit.get("cost_velocity_ratio", 3.0)
            return (
                f"Klaim SEP {no_sep} ditahan (Intensitas Biaya Ekstrem): Kecepatan biaya tagihan mencapai {ratio:.1f}x lipat dari batas wajar faskes sekelas "
                f"dengan rawat hanya {los} hari tanpa rawat ICU. Periksa rincian lembar pemakaian obat dan BHP di rekam medis."
            )

        if fraud_type == "UPCODING":
            return (
                f"Klaim SEP {no_sep} ditahan (Upcoding): Diagnosa {diagnosa} diajukan Severity Level {sev} (berat), "
                f"padahal rawat inap cuma {los} hari tanpa bukti tindakan ICU atau operasi, serta biaya riil cuma Rp {riil:,.0f} "
                f"(tagihan Rp {tagih:,.0f}). Disarankan turunkan ke Level 1 atau minta lembar instruksi dokter penanggung jawab (DPJP) sesuai Permenkes 26/2021."
            )

        if fraud_type == "UNBUNDLING":
            return (
                f"Klaim SEP {no_sep} ditahan (Unbundling / Pemecahan Kasus): Pasien terdata berkunjung ulang dalam waktu singkat "
                f"untuk penanganan keluhan yang sama. Sesuai SE Kemenkes HK.02.02/2022, episode perawatan berulang wajib digabung ke 1 nomor SEP utama."
            )

        if fraud_type == "PHANTOM_BILLING":
            return (
                f"Klaim SEP {no_sep} ditahan (Tagihan Fiktif / Phantom): Ditagihkan sebagai rawat inap, tapi lama rawat 0 hari atau "
                f"biaya riil Rp 0. Sesuai Permenkes 16/2019, klaim ditolak sementara dan dialihkan ke tim verifikasi lapangan."
            )

        return (
            f"Klaim SEP {no_sep} perlu dicek ulang: ada selisih tarif mencurigakan pada diagnosa {diagnosa}. "
            f"Silakan periksa rekam medis fisik pasien."
        )
