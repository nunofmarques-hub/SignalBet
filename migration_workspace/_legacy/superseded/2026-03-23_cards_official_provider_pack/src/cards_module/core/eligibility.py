from __future__ import annotations

from typing import Any, Dict, List


def evaluate_eligibility(engine_input: Dict[str, Any], score_block: Dict[str, Any], projection: Dict[str, Any]) -> Dict[str, Any]:
    reasons: List[str] = []
    penalties: List[str] = []
    dq = engine_input["data_quality_flag"]
    sample_depth = engine_input["sample_depth_flag"]
    profile = engine_input["discipline_profile"]

    if dq == "invalid":
        reasons.append("data_quality_invalid")
    if sample_depth == "low":
        penalties.append("sample_depth_low")
    if not profile.get("referee_used", False):
        penalties.append("referee_unknown")
    if profile["match_tension_flag"] in {"high", "very_high"}:
        reasons.append("tension_support")
    if profile["competitive_pressure"] == "high":
        reasons.append("competitive_pressure_support")
    if score_block["structural_bias"] == engine_input["market"]["selection"]:
        reasons.append("projection_market_alignment")
    if score_block["score_raw"] >= 75:
        reasons.append("score_threshold_pass")

    eligible = dq in {"clean", "partial"} and len(reasons) >= 3 and score_block["score_raw"] >= 72
    status = "candidate" if eligible else "rejected"
    return {"eligibility": eligible, "status": status, "reasons": reasons, "penalties": penalties}
