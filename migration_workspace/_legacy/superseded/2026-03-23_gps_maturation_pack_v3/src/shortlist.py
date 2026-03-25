from __future__ import annotations

def build_shortlist(ranked_picks: list[dict]) -> list[dict]:
    shortlisted, used_event_ids = [], set()
    for pick in sorted(ranked_picks, key=lambda x: x["global_score"], reverse=True):
        if pick["priority_tier"] not in {"Best","Top","Actionable"}:
            pick["selection_status"] = "watch"
            pick["shortlist_bucket"] = "watch"
            continue
        if "CONFLICT_SELECTOR_RULE_BLOCK" in pick["conflict_flags"] or "CONFLICT_DIRECT_OPPOSITE" in pick["conflict_flags"]:
            pick["selection_status"] = "blocked"
            pick["shortlist_bucket"] = "watch"
            continue
        if pick["event_id"] in used_event_ids:
            pick["selection_status"] = "excluded_duplicate_fixture"
            pick["shortlist_bucket"] = "watch"
            if "DUP_SAME_FIXTURE" not in pick["correlation_flags"]:
                pick["correlation_flags"].append("DUP_SAME_FIXTURE")
            continue
        pick["rank_position"] = len(shortlisted) + 1
        pick["selection_status"] = "selected"
        pick["shortlist_bucket"] = "core" if pick["priority_tier"] in {"Best","Top"} else "support"
        pick["pool_status"] = "shortlisted"
        shortlisted.append(pick)
        used_event_ids.add(pick["event_id"])
    return shortlisted
