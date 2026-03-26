from __future__ import annotations
from collections import Counter

def evaluate_pick_flags(payload: dict, existing_raw: list[dict] | None = None) -> dict:
    existing_raw = existing_raw or []
    conflict_flags, correlation_flags = [], []
    quality_adjustment = conflict_adjustment = correlation_adjustment = rationale_adjustment = completeness_adjustment = 0

    quality = payload.get("data_quality_flag", "clean")
    if quality == "partial":
        correlation_flags.append("GOV_DATA_PARTIAL")
        quality_adjustment = -4
    elif quality == "fragile":
        correlation_flags.append("GOV_DATA_FRAGILE")
        quality_adjustment = -9
    elif quality == "invalid":
        conflict_flags.append("CONFLICT_SELECTOR_RULE_BLOCK")
        conflict_adjustment = -15

    if not payload.get("edge_raw"):
        correlation_flags.append("GOV_EDGE_MISSING")
        completeness_adjustment -= 2

    if len(str(payload.get("rationale_summary","")).strip()) < 40:
        correlation_flags.append("GOV_RATIONALE_WEAK")
        rationale_adjustment -= 1

    desired = ("main_drivers","penalties","module_rank_internal","expiry_context")
    missing = sum(1 for k in desired if not payload.get(k))
    if missing >= 3:
        completeness_adjustment -= 3
    elif missing >= 1:
        completeness_adjustment -= 1

    same_fixture = [p for p in existing_raw if p.get("event_id") == payload.get("event_id")]
    if same_fixture:
        correlation_flags.append("DUP_SAME_FIXTURE")
        correlation_adjustment -= 2

    this_market = str(payload.get("market","")).lower()
    for other in same_fixture:
        other_market = str(other.get("market","")).lower()
        if ("under" in this_market and "over" in other_market) or ("over" in this_market and "under" in other_market):
            conflict_flags.append("CONFLICT_MARKET_DIRECTION")
            conflict_adjustment -= 7
            break
    if same_fixture and not conflict_flags:
        correlation_flags.append("CORR_SAME_MATCH_MODERATE")
        correlation_adjustment -= 5

    return {
        "conflict_flags": sorted(set(conflict_flags)),
        "correlation_flags": sorted(set(correlation_flags)),
        "adjustments": {
            "quality_adjustment": quality_adjustment,
            "conflict_adjustment": conflict_adjustment,
            "correlation_adjustment": correlation_adjustment,
            "rationale_adjustment": rationale_adjustment,
            "completeness_adjustment": completeness_adjustment,
        }
    }

def apply_theme_cluster(ranked_picks: list[dict]) -> list[dict]:
    keys = []
    for pick in ranked_picks:
        market = str(pick.get("market","")).lower()
        direction = "under" if "under" in market else "over" if "over" in market else market
        keys.append((pick["market_family"], direction))
    counts = Counter(keys)
    for pick in ranked_picks:
        market = str(pick.get("market","")).lower()
        direction = "under" if "under" in market else "over" if "over" in market else market
        if counts[(pick["market_family"], direction)] >= 3:
            if "CORR_THEME_CLUSTER" not in pick["correlation_flags"]:
                pick["correlation_flags"].append("CORR_THEME_CLUSTER")
            pick["correlation_adjustment"] -= 3
    return ranked_picks
