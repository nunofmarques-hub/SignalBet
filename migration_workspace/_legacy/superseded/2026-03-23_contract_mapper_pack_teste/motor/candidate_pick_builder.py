from __future__ import annotations

from typing import Any
from contract_mapper import map_corners_output_to_market_pick


def is_candidate_pick(corners_output: dict[str, Any]) -> bool:
    return ("market" in corners_output and "score" in corners_output and "eligible" in corners_output)


def infer_internal_rank(score: float) -> int:
    if score >= 86:
        return 1
    if score >= 72:
        return 2
    if score >= 60:
        return 3
    if score >= 50:
        return 4
    return 5


def build_candidate_pick(
    corners_output: dict[str, Any],
    *,
    module_version: str = "corners.v1_contract",
    kickoff_datetime: str | None = None,
    odds: float | None = None,
    edge_raw: float | str | None = None,
    expiry_context: str | None = None,
) -> dict[str, Any]:
    if not is_candidate_pick(corners_output):
        raise ValueError("corners_output incompleto para gerar candidate pick.")

    score = float(corners_output.get("score", 0.0))

    return map_corners_output_to_market_pick(
        corners_output,
        module_version=module_version,
        kickoff_datetime=kickoff_datetime,
        odds=odds,
        edge_raw=edge_raw,
        module_rank_internal=infer_internal_rank(score),
        expiry_context=expiry_context,
    )
