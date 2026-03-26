from __future__ import annotations
CONFIDENCE_POINTS={1:20,2:40,3:60,4:80,5:100}
RISK_SAFETY_POINTS={1:100,2:80,3:60,4:40,5:20}
EDGE_POINTS={'weak':35,'acceptable':55,'strong':75,'very_strong':90}
def build_breakdown(n: dict) -> dict:
    pre=0.50*n['score_norm_base']+0.20*CONFIDENCE_POINTS[n['confidence_norm']]+0.15*RISK_SAFETY_POINTS[n['risk_norm']]+0.15*EDGE_POINTS[n['edge_norm']]
    return {'score_norm_base':n['score_norm_base'],'confidence_points':CONFIDENCE_POINTS[n['confidence_norm']],'risk_safety_points':RISK_SAFETY_POINTS[n['risk_norm']],'edge_points':EDGE_POINTS[n['edge_norm']],'global_score_pre_adjustment':round(pre,2)}
