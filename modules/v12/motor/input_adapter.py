from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, Iterable, Optional, Tuple


class InputContractError(RuntimeError):
    """Raised when the protected input contract cannot be satisfied."""


@dataclass
class NormalizedFixture:
    fixture_id: int
    league_id: int
    season: int
    home_team_id: int
    away_team_id: int
    home_team_name: str
    away_team_name: str
    source_mode: str
    observed_mode: str
    readiness_level: str
    provider_name: str
    provider_source: str
    input_profile: str
    over_1_5_team_context: str = "OK"
    over_1_5_match_context: str = "OK"
    under_3_5_match_context: str = "OK"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def _deep_get(obj: Any, path: Iterable[str]) -> Any:
    cur = obj
    for key in path:
        if not isinstance(cur, dict) or key not in cur:
            return None
        cur = cur[key]
    return cur


def _first_present(bundle: Dict[str, Any], candidates: Iterable[Tuple[str, ...]]) -> Any:
    for path in candidates:
        value = _deep_get(bundle, path)
        if value is not None:
            return value
    return None


def _require(value: Any, field_name: str) -> Any:
    if value is None:
        raise InputContractError(
            f"hard_fail: missing required field '{field_name}' after protected input normalization"
        )
    return value


def normalize_protected_bundle(bundle: Dict[str, Any]) -> NormalizedFixture:
    fixture_id = _require(
        _first_present(bundle, [
            ("fixture_id",),
            ("fixture", "id"),
            ("bundle", "fixture_id"),
            ("bundle", "fixture", "id"),
        ]),
        "fixture_id",
    )

    league_id = _require(
        _first_present(bundle, [
            ("league_id",),
            ("fixture", "league_id"),
            ("fixture", "league", "id"),
            ("bundle", "league_id"),
            ("bundle", "fixture", "league_id"),
            ("bundle", "fixture", "league", "id"),
            ("context", "league_id"),
            ("match_context", "league_id"),
        ]),
        "league_id",
    )

    season = _require(
        _first_present(bundle, [
            ("season",),
            ("fixture", "season"),
            ("league", "season"),
            ("bundle", "season"),
            ("bundle", "fixture", "season"),
        ]),
        "season",
    )

    home_team_id = _require(
        _first_present(bundle, [
            ("home_team_id",),
            ("teams", "home", "id"),
            ("fixture", "teams", "home", "id"),
            ("bundle", "home_team_id"),
            ("bundle", "teams", "home", "id"),
        ]),
        "home_team_id",
    )

    away_team_id = _require(
        _first_present(bundle, [
            ("away_team_id",),
            ("teams", "away", "id"),
            ("fixture", "teams", "away", "id"),
            ("bundle", "away_team_id"),
            ("bundle", "teams", "away", "id"),
        ]),
        "away_team_id",
    )

    home_team_name = _first_present(bundle, [
        ("home_team_name",),
        ("teams", "home", "name"),
        ("fixture", "teams", "home", "name"),
    ]) or "HOME"

    away_team_name = _first_present(bundle, [
        ("away_team_name",),
        ("teams", "away", "name"),
        ("fixture", "teams", "away", "name"),
    ]) or "AWAY"

    source_mode = _require(_first_present(bundle, [("source_mode",)]), "source_mode")
    observed_mode = _require(_first_present(bundle, [("observed_mode",)]), "observed_mode")
    readiness_level = _require(_first_present(bundle, [("readiness_level",)]), "readiness_level")
    provider_name = _require(_first_present(bundle, [("provider_name",)]), "provider_name")
    provider_source = _require(_first_present(bundle, [("provider_source",)]), "provider_source")
    input_profile = _require(_first_present(bundle, [("input_profile",)]), "input_profile")

    over_team_ctx = _first_present(bundle, [
        ("over_1_5_team_context",),
        ("contexts", "over_1_5_team_context"),
    ]) or "OK"
    over_match_ctx = _first_present(bundle, [
        ("over_1_5_match_context",),
        ("contexts", "over_1_5_match_context"),
    ]) or "OK"
    under_ctx = _first_present(bundle, [
        ("under_3_5_match_context",),
        ("contexts", "under_3_5_match_context"),
    ]) or "OK"

    return NormalizedFixture(
        fixture_id=int(fixture_id),
        league_id=int(league_id),
        season=int(season),
        home_team_id=int(home_team_id),
        away_team_id=int(away_team_id),
        home_team_name=str(home_team_name),
        away_team_name=str(away_team_name),
        source_mode=str(source_mode),
        observed_mode=str(observed_mode),
        readiness_level=str(readiness_level),
        provider_name=str(provider_name),
        provider_source=str(provider_source),
        input_profile=str(input_profile),
        over_1_5_team_context=str(over_team_ctx),
        over_1_5_match_context=str(over_match_ctx),
        under_3_5_match_context=str(under_ctx),
    )
