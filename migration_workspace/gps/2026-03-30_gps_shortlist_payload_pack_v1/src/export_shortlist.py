
from __future__ import annotations
from typing import Iterable

ALLOWED_FIELDS = (
    "pick_id",
    "module_name",
    "fixture_id",
    "match_label",
    "market_code",
    "selection_label",
    "rank_position",
    "rationale_short",
)

def export_shortlist(shortlisted_picks: Iterable[dict]) -> list[dict]:
    output: list[dict] = []
    for pick in shortlisted_picks:
        item = {field: pick[field] for field in ALLOWED_FIELDS}
        output.append(item)
    output.sort(key=lambda x: x["rank_position"])
    return output
