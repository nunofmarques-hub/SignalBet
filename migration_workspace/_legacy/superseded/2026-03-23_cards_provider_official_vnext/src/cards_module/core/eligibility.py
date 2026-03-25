from __future__ import annotations

from typing import Any, Dict, List


def decide_eligibility(engine_input: Dict[str, Any], scored: Dict[str, Any]) -> Dict[str, Any]:
    penalties: List[str] = []
    if engine_input.get("data_quality_flag") == "invalid":
        penalties.append("invalid_data_quality")
    if engine_input.get("sample_depth_flag") == "low":
        penalties.append("low_sample_depth")
    if engine_input.get("signal_consistency") == "low":
        penalties.append("low_signal_consistency")
    if not engine_input.get("referee_used"):
        penalties.append("referee_context_missing")

    eligible = scored["score_raw"] >= 74 and engine_input.get("data_quality_flag") in {"clean", "partial"} and "invalid_data_quality" not in penalties
    status = "candidate" if eligible else "rejected"
    return {
        "eligibility": eligible,
        "status": status,
        "penalties": penalties,
    }
