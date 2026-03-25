from __future__ import annotations

def assign_priority_tier(global_score: int, confidence_norm: int, risk_norm: int, data_quality_flag: str, eligibility: bool) -> str:
    if not eligibility:
        return "Reject"
    if global_score >= 90 and confidence_norm >= 4 and risk_norm <= 2 and data_quality_flag == "clean":
        return "Best"
    if global_score >= 82:
        return "Top"
    if global_score >= 72:
        return "Actionable"
    if global_score >= 60:
        return "Watchlist"
    return "Reject"
