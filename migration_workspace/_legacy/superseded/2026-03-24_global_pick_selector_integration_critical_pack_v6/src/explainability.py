from __future__ import annotations

def build_explainability(breakdown: dict, final_score: dict, flags: dict) -> dict:
    return {'executive_rationale': f"Pick {final_score['priority_tier']} com global_score={final_score['global_score_final']} após tradução comparável de score, confiança, risco e edge.",'selector_decision_note': f"score_base={breakdown['score_norm_base']}; pre={breakdown['global_score_pre_adjustment']}; tier={final_score['priority_tier']}; tier_reason={final_score['priority_tier_reason']}"}
