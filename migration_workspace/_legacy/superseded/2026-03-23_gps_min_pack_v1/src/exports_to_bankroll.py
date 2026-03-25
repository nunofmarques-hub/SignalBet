"""Export selector output to formal bankroll payload."""
from __future__ import annotations


def export_to_bankroll(payload: dict, normalized: dict, global_score: int, priority_tier: str, flags: dict) -> dict:
    return {
        "selector_schema_version": "selector_pick.v1.1",
        "pick_id": payload["pick_id"],
        "module_id": payload["module_id"],
        "module_version": payload["module_version"],
        "event_id": payload["event_id"],
        "match_label": payload["match_label"],
        "market_family": payload["market_family"],
        "market": payload["market"],
        "selection": payload["selection"],
        "line": payload.get("line"),
        "odds": float(payload["odds"]),
        "global_score": global_score,
        "confidence_norm": normalized["confidence_norm"],
        "risk_norm": normalized["risk_norm"],
        "edge_norm": normalized["edge_norm"],
        "priority_tier": priority_tier,
        "conflict_flags": flags["conflict_flags"],
        "correlation_flags": flags["correlation_flags"],
        "executive_rationale": "Pick comparada e priorizada pelo Global Pick Selector.",
        "selector_decision_note": "Export inicial do pack mínimo funcional.",
        "pool_status": "exported_to_bankroll",
        "normalization_version": normalized["normalization_version"]
    }
