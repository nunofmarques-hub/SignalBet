from __future__ import annotations

from typing import Any, Dict, List


STRICT_MARKETS_REQUIRING_REF = {"match_cards_over", "match_cards_under"}


def decide_eligibility(engine_input: Dict[str, Any], scored: Dict[str, Any]) -> Dict[str, Any]:
    penalties: List[str] = []

    quality = engine_input.get("data_quality_flag")
    sample = engine_input.get("sample_depth_flag")
    consistency = engine_input.get("signal_consistency")
    market = engine_input.get("market")
    projection = float(engine_input.get("projection") or 0.0)
    line = float(engine_input.get("line") or 0.0)
    edge_abs = abs(projection - line)

    if quality == "invalid":
        penalties.append("invalid_data_quality")
    if quality == "fragile":
        penalties.append("fragile_data_quality")
    if sample == "low":
        penalties.append("low_sample_depth")
    if consistency == "low":
        penalties.append("low_signal_consistency")
    if market in STRICT_MARKETS_REQUIRING_REF and not engine_input.get("referee_used"):
        penalties.append("referee_context_missing")
    if edge_abs < 0.30:
        penalties.append("thin_projection_edge")

    eligible = all([
        scored["score_raw"] >= 78,
        quality == "clean",
        sample in {"medium", "high"},
        consistency in {"medium", "high"},
        edge_abs >= 0.30,
        "invalid_data_quality" not in penalties,
        "fragile_data_quality" not in penalties,
        "low_sample_depth" not in penalties,
        "low_signal_consistency" not in penalties,
        "referee_context_missing" not in penalties,
    ])

    status = "candidate" if eligible else "rejected"
    return {
        "eligibility": eligible,
        "status": status,
        "penalties": penalties,
    }
