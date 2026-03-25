from __future__ import annotations

CONFIDENCE_POINTS = {1:20, 2:40, 3:60, 4:80, 5:100}
RISK_SAFETY_POINTS = {1:100, 2:80, 3:60, 4:40, 5:20}
EDGE_POINTS = {"weak":35, "acceptable":55, "strong":75, "very_strong":90}

def build_breakdown(normalized: dict) -> dict:
    score_norm_base = normalized["score_norm_base"]
    confidence_norm = normalized["confidence_norm"]
    risk_norm = normalized["risk_norm"]
    edge_norm = normalized["edge_norm"]
    confidence_points = CONFIDENCE_POINTS[confidence_norm]
    risk_safety_points = RISK_SAFETY_POINTS[risk_norm]
    edge_points = EDGE_POINTS[edge_norm]
    pre = 0.50*score_norm_base + 0.20*confidence_points + 0.15*risk_safety_points + 0.15*edge_points
    return {
        "score_norm_base": score_norm_base,
        "confidence_points": confidence_points,
        "risk_safety_points": risk_safety_points,
        "edge_points": edge_points,
        "global_score_pre_adjustment": round(pre, 2),
    }
