from __future__ import annotations
from data_api.providers.api_football_provider import ApiFootballProvider

def fetch_fixture_events(fixture_id: int) -> dict:
    provider = ApiFootballProvider()
    return provider.get("/fixtures/events", {"fixture": fixture_id})
