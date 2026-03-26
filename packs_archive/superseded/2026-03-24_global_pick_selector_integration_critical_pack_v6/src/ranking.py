from __future__ import annotations

def compute_final_score(payload: dict, normalized: dict, adjustments: dict, breakdown: dict) -> dict:
    final=round(max(0,min(100,breakdown['global_score_pre_adjustment']+sum(adjustments.values()))))
    tier='Best' if final>=90 and normalized['confidence_norm']>=4 and normalized['risk_norm']<=2 else 'Top' if final>=82 else 'Actionable' if final>=72 else 'Watchlist' if final>=60 else 'Reject'
    reason='score>=90_confidence>=4_risk<=2_clean' if tier=='Best' else 'score>=82' if tier=='Top' else 'score>=72' if tier=='Actionable' else 'score>=60' if tier=='Watchlist' else 'score<60'
    return {'global_score_final':int(final),'priority_tier':tier,'priority_tier_reason':reason}
