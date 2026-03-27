from __future__ import annotations

def assign_priority_tier(global_score: int, confidence_norm: int, risk_norm: int, data_quality_flag: str, eligibility: bool):
    if not eligibility: return "Reject", "not_eligible"
    if global_score >= 90 and confidence_norm >= 4 and risk_norm <= 2 and data_quality_flag == "clean":
        return "Best", "score>=90_confidence>=4_risk<=2_clean"
    if global_score >= 82: return "Top", "score>=82"
    if global_score >= 72: return "Actionable", "score>=72"
    if global_score >= 60: return "Watchlist", "score>=60"
    return "Reject", "score<60"
