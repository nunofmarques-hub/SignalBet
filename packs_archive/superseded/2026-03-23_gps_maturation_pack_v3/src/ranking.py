from __future__ import annotations
from priority_rules import assign_priority_tier

def compute_final_score(payload: dict, normalized: dict, adjustments: dict, breakdown: dict) -> dict:
    final = round(max(0, min(100, breakdown["global_score_pre_adjustment"] + sum(adjustments.values()))))
    tier = assign_priority_tier(final, normalized["confidence_norm"], normalized["risk_norm"], payload.get("data_quality_flag","clean"), payload.get("eligibility", False))
    return {"global_score_final": int(final), "priority_tier": tier}
