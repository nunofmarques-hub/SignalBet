from __future__ import annotations

"""Input adapter between the future Data/API Layer central payload and the v12 motor.

This adapter does NOT own data collection. It only maps the central payload into the
internal shape expected by the v12 market engines.
"""

from dataclasses import dataclass
from typing import Any


REQUIRED_ROOT_KEYS = {
    "fixture",
    "teams",
    "standings_context",
    "team_stats_season",
    "team_stats_recent",
    "league_market_profile",
    "odds_snapshot",
    "timing_profile",
    "scoreline_profile",
    "risk_flags",
}


@dataclass
class CentralInputValidation:
    ok: bool
    missing_keys: list[str]
    quality_flag: str
    notes: list[str]



def validate_central_payload(payload: dict[str, Any]) -> CentralInputValidation:
    missing = sorted(REQUIRED_ROOT_KEYS.difference(payload.keys()))
    notes: list[str] = []
    if missing:
        return CentralInputValidation(False, missing, "invalid", ["missing_root_keys"])

    quality_flag = "clean"
    odds_source = payload.get("odds_snapshot", {}).get("source", "unknown")
    if odds_source in {"estimated", "manual_override"}:
        quality_flag = "partial"
        notes.append(f"odds_source={odds_source}")

    if not payload.get("team_stats_recent"):
        quality_flag = "fragile"
        notes.append("recent_form_missing")

    return CentralInputValidation(True, [], quality_flag, notes)



def adapt_fixture_block(payload: dict[str, Any]) -> dict[str, Any]:
    fixture = payload["fixture"]
    teams = payload["teams"]
    return {
        "fixture_id": fixture["fixture_id"],
        "match_label": fixture["match_label"],
        "competition": fixture["competition"],
        "kickoff_datetime": fixture["kickoff_datetime"],
        "league_id": fixture.get("league_id"),
        "league_name": fixture.get("league_name", fixture["competition"]),
        "season": fixture.get("season"),
        "country": fixture.get("country"),
        "home_team_id": teams["home"]["team_id"],
        "home_team_name": teams["home"]["name"],
        "away_team_id": teams["away"]["team_id"],
        "away_team_name": teams["away"]["name"],
    }



def adapt_team_context(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "standings_context": payload["standings_context"],
        "team_stats_season": payload["team_stats_season"],
        "team_stats_recent": payload["team_stats_recent"],
        "league_market_profile": payload["league_market_profile"],
        "odds_snapshot": payload["odds_snapshot"],
        "timing_profile": payload["timing_profile"],
        "scoreline_profile": payload["scoreline_profile"],
        "risk_flags": payload["risk_flags"],
    }



def build_v12_input(payload: dict[str, Any]) -> dict[str, Any]:
    validation = validate_central_payload(payload)
    if not validation.ok:
        raise ValueError(f"Central payload invalid: missing={validation.missing_keys}")

    adapted = adapt_fixture_block(payload)
    adapted.update(adapt_team_context(payload))
    adapted["adapter_meta"] = {
        "adapter_version": "v12.input_adapter.0.1",
        "data_quality_flag": validation.quality_flag,
        "adapter_notes": validation.notes,
    }
    return adapted
