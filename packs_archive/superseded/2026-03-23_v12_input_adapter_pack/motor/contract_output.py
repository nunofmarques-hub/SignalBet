from __future__ import annotations

"""Contract v1.1 output builder for v12 candidate picks."""

from datetime import datetime, timezone
from typing import Any


MARKET_MAP = {
    "O15_TEAM": {"market": "team_goals_over", "goal_profile": "offensive_directed", "motor_family": "team_over"},
    "O15_GAME": {"market": "match_goals_over", "goal_profile": "offensive_global", "motor_family": "match_over"},
    "U35": {"market": "match_goals_under", "goal_profile": "conservative_under", "motor_family": "match_under"},
}


VARIANT_MAP = {
    ("O15_TEAM", 1.5): "TEAM_OVER_15",
    ("O15_GAME", 1.5): "MATCH_OVER_15",
    ("U35", 3.5): "MATCH_UNDER_35",
}



def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")



def _market_line_and_selection(engine: str, match_label: str, favorite_team: str | None) -> tuple[float, str]:
    if engine == "O15_TEAM":
        return 1.5, f"{favorite_team} Over 1.5"
    if engine == "O15_GAME":
        return 1.5, "Over 1.5"
    if engine == "U35":
        return 3.5, "Under 3.5"
    raise ValueError(f"Unsupported engine: {engine}")



def build_market_pick_v11(
    *,
    module_version: str,
    fixture_id: int | str,
    match_label: str,
    competition: str,
    kickoff_datetime: str,
    engine: str,
    score_raw: float,
    confidence_raw: int,
    risk_raw: int,
    edge_raw: str,
    odds: float,
    eligibility: bool,
    rationale_summary: str,
    main_drivers: list[str],
    penalties: list[str],
    data_quality_flag: str,
    module_rank_internal: int,
    favorite_team: str | None,
    indicator_snapshot: dict[str, Any],
    driver_scores: dict[str, Any],
    penalty_scores: dict[str, Any],
    source_notes: list[str] | None = None,
) -> dict[str, Any]:
    line, selection = _market_line_and_selection(engine, match_label, favorite_team)
    market_info = MARKET_MAP[engine]
    market_variant = VARIANT_MAP[(engine, line)]
    safe_comp = competition.lower().replace(" ", "_")
    pick_id = f"v12_{fixture_id}_{market_variant.lower()}_{safe_comp}"

    return {
        "schema_version": "market_pick.v1.1",
        "pick_id": pick_id,
        "created_at": _iso_now(),
        "module_id": "v12",
        "module_version": module_version,
        "event_id": fixture_id,
        "match_label": match_label,
        "competition": competition,
        "kickoff_datetime": kickoff_datetime,
        "market_family": "goals",
        "market": market_info["market"],
        "selection": selection,
        "line": line,
        "odds": odds,
        "eligibility": eligibility,
        "score_raw": round(score_raw, 2),
        "confidence_raw": confidence_raw,
        "risk_raw": risk_raw,
        "edge_raw": edge_raw,
        "rationale_summary": rationale_summary,
        "main_drivers": main_drivers,
        "penalties": penalties,
        "data_quality_flag": data_quality_flag,
        "module_rank_internal": module_rank_internal,
        "expiry_context": "refresh_if_odds_move_5pct",
        "module_specific_payload": {
            "motor_id": {
                "O15_TEAM": "TEAM_OVER_ENGINE",
                "O15_GAME": "MATCH_OVER_ENGINE",
                "U35": "MATCH_UNDER_ENGINE",
            }[engine],
            "motor_family": market_info["motor_family"],
            "market_variant": market_variant,
            "goal_profile": market_info["goal_profile"],
            "model_window": "season_plus_last5",
            "line_family_supported": [0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
            "current_core_status": "active_core",
            "indicator_snapshot": indicator_snapshot,
            "driver_scores": driver_scores,
            "penalty_scores": penalty_scores,
            "source_notes": source_notes or [],
        },
    }
