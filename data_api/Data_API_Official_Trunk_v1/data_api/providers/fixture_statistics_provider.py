from __future__ import annotations
from data_api.providers.api_football_provider import ApiFootballProvider

def fetch_fixture_statistics(fixture_id: int) -> dict:
    provider = ApiFootballProvider()
    return provider.get("/fixtures/statistics", {"fixture": fixture_id})
