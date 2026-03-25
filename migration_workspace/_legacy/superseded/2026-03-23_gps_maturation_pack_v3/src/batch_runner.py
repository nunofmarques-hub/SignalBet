from __future__ import annotations
from schema_validator import validate_pick
from normalization import build_normalized_fields
from flags import evaluate_pick_flags, apply_theme_cluster
from ranking_breakdown import build_breakdown
from ranking import compute_final_score
from explainability import build_explainability
from shortlist import build_shortlist
from exports_to_bankroll import export_frozen_batch

def run_batch(batch_payload: dict, selector_run_id: str = "gps_run_v3", normalization_version: str = "norm.v1.1") -> dict:
    ranked, raw_history = [], []
    for payload in batch_payload["picks"]:
        validation = validate_pick(payload)
        if not validation["valid"]:
            ranked.append({
                "pick_id": payload.get("pick_id"), "module_id": payload.get("module_id"),
                "module_version": payload.get("module_version"), "event_id": payload.get("event_id"),
                "match_label": payload.get("match_label"), "market_family": payload.get("market_family"),
                "market": payload.get("market"), "selection": payload.get("selection"),
                "line": payload.get("line"), "odds": payload.get("odds"), "global_score": 0,
                "confidence_norm": 1, "risk_norm": 5, "edge_norm": "weak",
                "priority_tier": "Reject", "conflict_flags": ["CONFLICT_SELECTOR_RULE_BLOCK"],
                "correlation_flags": [], "executive_rationale": "Payload rejeitado na validação.",
                "selector_decision_note": "validation_failed", "pool_status": "rejected",
                "normalization_version": normalization_version, "rank_position": 999,
                "shortlist_bucket": "watch", "selection_status": "blocked"
            })
            continue
        normalized = build_normalized_fields(payload)
        flag_result = evaluate_pick_flags(payload, existing_raw=raw_history)
        breakdown = build_breakdown(normalized)
        final_score = compute_final_score(payload, normalized, flag_result["adjustments"], breakdown)
        explain = build_explainability(breakdown, final_score, flag_result)
        ranked.append({
            "pick_id": payload["pick_id"], "module_id": payload["module_id"], "module_version": payload["module_version"],
            "event_id": payload["event_id"], "match_label": payload["match_label"], "market_family": payload["market_family"],
            "market": payload["market"], "selection": payload["selection"], "line": payload.get("line"), "odds": payload["odds"],
            "confidence_norm": normalized["confidence_norm"], "risk_norm": normalized["risk_norm"], "edge_norm": normalized["edge_norm"],
            "conflict_flags": flag_result["conflict_flags"], "correlation_flags": flag_result["correlation_flags"],
            **flag_result["adjustments"], **breakdown, **final_score, "global_score": final_score["global_score_final"], **explain,
            "pool_status": "ranked", "normalization_version": normalization_version,
        })
        raw_history.append(payload)

    ranked = apply_theme_cluster(ranked)
    for pick in ranked:
        if "CORR_THEME_CLUSTER" in pick["correlation_flags"]:
            pick["global_score"] = max(0, pick["global_score"] - 3)
            if pick["global_score"] < 60:
                pick["priority_tier"] = "Reject"
            elif pick["global_score"] < 72 and pick["priority_tier"] in {"Best","Top","Actionable"}:
                pick["priority_tier"] = "Watchlist"

    shortlisted = build_shortlist(ranked)
    exported = export_frozen_batch(shortlisted, selector_run_id=selector_run_id, normalization_version=normalization_version)
    return {"ranked": ranked, "shortlisted": shortlisted, "exported": exported}
