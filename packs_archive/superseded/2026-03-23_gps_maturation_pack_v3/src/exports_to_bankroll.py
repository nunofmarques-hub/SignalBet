from __future__ import annotations
from datetime import datetime, timezone

def export_frozen_batch(shortlisted: list[dict], selector_run_id: str, normalization_version: str) -> dict:
    exported_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    picks = []
    for pick in shortlisted:
        picks.append({
            "selector_schema_version": "selector_pick.v1.1",
            "pick_id": pick["pick_id"],
            "module_id": pick["module_id"],
            "module_version": pick["module_version"],
            "event_id": pick["event_id"],
            "match_label": pick["match_label"],
            "market_family": pick["market_family"],
            "market": pick["market"],
            "selection": pick["selection"],
            "line": pick.get("line"),
            "odds": pick["odds"],
            "global_score": pick["global_score"],
            "confidence_norm": pick["confidence_norm"],
            "risk_norm": pick["risk_norm"],
            "edge_norm": pick["edge_norm"],
            "priority_tier": pick["priority_tier"],
            "conflict_flags": pick["conflict_flags"],
            "correlation_flags": pick["correlation_flags"],
            "executive_rationale": pick["executive_rationale"],
            "selector_decision_note": pick["selector_decision_note"],
            "pool_status": "exported_to_bankroll",
            "normalization_version": normalization_version,
            "rank_position": pick["rank_position"],
            "shortlist_bucket": pick["shortlist_bucket"],
            "selection_status": pick["selection_status"],
            "exported_at": exported_at,
        })
    return {
        "batch_schema_version": "bankroll_export_batch.frozen.v1",
        "selector_run_id": selector_run_id,
        "generated_at": exported_at,
        "normalization_version": normalization_version,
        "shortlist_size": len(picks),
        "picks": picks,
    }
