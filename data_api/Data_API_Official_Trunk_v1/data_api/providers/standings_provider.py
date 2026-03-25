from __future__ import annotations
from data_api.providers.api_football_provider import ApiFootballProvider

def fetch_standings(league_id: int, season: int) -> dict:
    provider = ApiFootballProvider()
    return provider.get("/standings", {"league": league_id, "season": season})
