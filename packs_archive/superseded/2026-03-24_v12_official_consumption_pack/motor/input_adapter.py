from __future__ import annotations

from typing import Any, Dict


def adapt_bundle(bundle) -> Dict[str, Any]:
    fixture = bundle.fixtures_catalog[0]

    return {
        "fixture_id": fixture["fixture"]["id"],
        "kickoff_datetime": fixture["fixture"]["date"],
        "competition": fixture["league"]["name"],
        "home_team_id": fixture["teams"]["home"]["id"],
        "home_team_name": fixture["teams"]["home"]["name"],
        "away_team_id": fixture["teams"]["away"]["id"],
        "away_team_name": fixture["teams"]["away"]["name"],
        "standings_snapshot": bundle.standings_snapshot,
        "fixture_statistics": bundle.fixture_statistics,
        "home_team_statistics": bundle.home_team_statistics,
        "away_team_statistics": bundle.away_team_statistics,
        "provider_name": bundle.provider_name,
        "provider_source": bundle.source,
    }