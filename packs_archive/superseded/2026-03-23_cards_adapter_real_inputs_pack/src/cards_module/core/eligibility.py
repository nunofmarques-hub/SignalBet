
from __future__ import annotations

from typing import Any, Dict


def decide_eligibility(data: Dict[str, Any], scores: Dict[str, Any]) -> Dict[str, Any]:
    reasons = []
    eligible = True

    if data["data_quality_flag"] == "invalid":
        eligible = False
        reasons.append("invalid_data_quality")
    if data["sample_depth"] < 8:
        eligible = False
        reasons.append("sample_depth_below_minimum")
    if data["market"] in {"match_cards_over", "match_cards_under"} and not data["referee_known"]:
        eligible = False
        reasons.append("missing_referee_for_match_total_market")
    if scores["score_raw"] < 68:
        eligible = False
        reasons.append("score_below_threshold")

    market = data["market"]
    bias = scores["structural_bias"]
    if market.endswith("over") and bias == "under":
        eligible = False
        reasons.append("market_bias_conflict")
    if market.endswith("under") and bias == "over":
        eligible = False
        reasons.append("market_bias_conflict")

    status = "candidate" if eligible else "rejected"
    return {"eligibility": eligible, "status": status, "reasons": reasons}
