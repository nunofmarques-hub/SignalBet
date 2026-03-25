from __future__ import annotations
from normalization_rules import score_rule, level_rule, edge_rule

def build_normalized_fields(payload: dict) -> dict:
    return {
        "score_norm_base": score_rule(payload["module_id"], payload["score_raw"]),
        "confidence_norm": level_rule(payload["confidence_raw"]),
        "risk_norm": level_rule(payload["risk_raw"]),
        "edge_norm": edge_rule(payload.get("edge_raw")),
    }
