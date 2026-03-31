from __future__ import annotations
from typing import Iterable

ALLOWED_FIELDS = (
    "pick_id",
    "module_name",
    "match_label",
    "market_code",
    "selection_label",
    "rank_position",
    "rationale_short",
    "shortlist_level",
)

ALLOWED_LEVELS = {"primary", "secondary", "watchlist"}

def export_shortlist_product(shortlisted_picks: Iterable[dict]) -> list[dict]:
    output: list[dict] = []
    for pick in shortlisted_picks:
        item = {field: pick[field] for field in ALLOWED_FIELDS}
        if item["shortlist_level"] not in ALLOWED_LEVELS:
            raise ValueError(f"Invalid shortlist_level: {item['shortlist_level']}")
        output.append(item)
    output.sort(key=lambda x: x["rank_position"])
    return output
