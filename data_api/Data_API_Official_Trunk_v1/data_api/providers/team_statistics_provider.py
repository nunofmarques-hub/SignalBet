from __future__ import annotations
from data_api.providers.api_football_provider import ApiFootballProvider

def fetch_team_statistics(team_id: int, league_id: int, season: int) -> dict:
    provider = ApiFootballProvider()
    return provider.get("/teams/statistics", {"league": league_id, "season": season, "team": team_id})
