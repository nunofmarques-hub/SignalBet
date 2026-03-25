from __future__ import annotations
from data_api.providers.api_football_provider import ApiFootballProvider

def fetch_fixtures(league_id: int, season: int, status: str = "FT-AET-PEN") -> dict:
    provider = ApiFootballProvider()
    return provider.get("/fixtures", {"league": league_id, "season": season, "status": status})
