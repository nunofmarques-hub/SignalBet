from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


DEFAULT_LEAGUE_ID = 140
DEFAULT_SEASON = 2024


@dataclass
class ProviderBundle:
    provider_name: str
    source: str
    fixtures_catalog: List[Dict[str, Any]]
    standings_snapshot: Dict[str, Any]
    fixture_statistics: Dict[str, Any]
    home_team_statistics: Dict[str, Any]
    away_team_statistics: Dict[str, Any]


def _get_nested(data: Any, path: str, default: Any = None) -> Any:
    current = data
    for part in path.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return default
    return current


def _to_float(value: Any, default: float = 0.0) -> float:
    try:
        if value in (None, "", "null", "None"):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def _to_int(value: Any, default: int = 0) -> int:
    try:
        if value in (None, "", "null", "None"):
            return default
        return int(float(value))
    except (TypeError, ValueError):
        return default


def _normalize_team_statistics(raw_stats: Dict[str, Any]) -> Dict[str, Any]:
    goals_for_per_game = _to_float(
        _get_nested(raw_stats, "goals.for.average.total"), 0.0
    )
    goals_against_per_game = _to_float(
        _get_nested(raw_stats, "goals.against.average.total"), 0.0
    )
    matches_played = _to_int(
        _get_nested(raw_stats, "fixtures.played.total"), 0
    )

    shots_on_target_per_game = _to_float(
        _get_nested(raw_stats, "shots.on.goal.average.total"),
        _to_float(
            _get_nested(raw_stats, "shots.on_target.average.total"),
            _to_float(
                _get_nested(raw_stats, "statistics.shots_on_target_per_game"),
                0.0,
            ),
        ),
    )

    shots_per_game = _to_float(
        _get_nested(raw_stats, "shots.total.average.total"),
        _to_float(
            _get_nested(raw_stats, "shots.average.total"),
            _to_float(
                _get_nested(raw_stats, "statistics.shots_per_game"),
                0.0,
            ),
        ),
    )

    return {
        "goals_for_per_game": goals_for_per_game,
        "goals_against_per_game": goals_against_per_game,
        "matches_played": matches_played,
        "shots_per_game": shots_per_game,
        "shots_on_target_per_game": shots_on_target_per_game,
        "raw_provider_payload": raw_stats,
    }


def _extract_ids(fixtures: List[Dict[str, Any]]) -> Dict[str, int]:
    if not fixtures:
        raise ValueError("Provider devolveu lista de fixtures vazia.")

    first = fixtures[0]
    fixture_id = _to_int(_get_nested(first, "fixture.id"))
    home_team_id = _to_int(_get_nested(first, "teams.home.id"))
    away_team_id = _to_int(_get_nested(first, "teams.away.id"))

    if not fixture_id or not home_team_id or not away_team_id:
        raise ValueError(
            "Não foi possível extrair fixture_id/home_team_id/away_team_id."
        )

    return {
        "fixture_id": fixture_id,
        "home_team_id": home_team_id,
        "away_team_id": away_team_id,
    }


def _diagnostic_fallback() -> ProviderBundle:
    fixture = {
        "fixture": {
            "id": 878317,
            "date": "2026-03-25T19:45:00Z",
        },
        "league": {
            "id": 140,
            "name": "La Liga",
            "season": 2024,
        },
        "teams": {
            "home": {"id": 529, "name": "Mallorca"},
            "away": {"id": 530, "name": "Las Palmas"},
        },
    }

    standings = {
        "league_id": 140,
        "season": 2024,
        "rows": [
            {"team_id": 529, "rank": 12, "points": 38},
            {"team_id": 530, "rank": 16, "points": 30},
        ],
    }

    fixture_stats = {
        "fixture_id": 878317,
        "home": {"shots_on_target": 4},
        "away": {"shots_on_target": 3},
    }

    home_stats = {
        "goals_for_per_game": 1.45,
        "goals_against_per_game": 1.12,
        "matches_played": 28,
        "shots_per_game": 11.2,
        "shots_on_target_per_game": 4.1,
    }

    away_stats = {
        "goals_for_per_game": 1.08,
        "goals_against_per_game": 1.51,
        "matches_played": 28,
        "shots_per_game": 9.4,
        "shots_on_target_per_game": 3.2,
    }

    return ProviderBundle(
        provider_name="diagnostic_local_fallback",
        source="diagnostic_only",
        fixtures_catalog=[fixture],
        standings_snapshot=standings,
        fixture_statistics=fixture_stats,
        home_team_statistics=home_stats,
        away_team_statistics=away_stats,
    )


def load_official_bundle(
    league_id: int = DEFAULT_LEAGUE_ID,
    season: int = DEFAULT_SEASON,
) -> ProviderBundle:
    try:
        from data_api.services.fixtures_service import get_fixtures_by_league_season
        from data_api.services.standings_service import get_standings_snapshot
        from data_api.services.statistics_service import (
            get_fixture_statistics,
            get_team_statistics,
        )

        fixtures = get_fixtures_by_league_season(league_id, season)
        standings = get_standings_snapshot(league_id, season)
        ids = _extract_ids(fixtures)

        raw_fixture_stats = get_fixture_statistics(ids["fixture_id"], league_id, season)
        raw_home_stats = get_team_statistics(ids["home_team_id"], league_id, season)
        raw_away_stats = get_team_statistics(ids["away_team_id"], league_id, season)

        home_stats = _normalize_team_statistics(raw_home_stats)
        away_stats = _normalize_team_statistics(raw_away_stats)

        return ProviderBundle(
            provider_name="Data_API_Official_Trunk_v1",
            source="official_default",
            fixtures_catalog=fixtures,
            standings_snapshot=standings,
            fixture_statistics=raw_fixture_stats,
            home_team_statistics=home_stats,
            away_team_statistics=away_stats,
        )

    except Exception:
        return _diagnostic_fallback()