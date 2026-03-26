"""Contratos mínimos do provider oficial de Cards."""
from __future__ import annotations

OFFICIAL_SOURCE = "Data_API_Official_Trunk_v1"
OFFICIAL_PROVIDER = "data_api.services"
FIXTURES_SERVICE = "data_api.services.fixtures_service.get_fixtures_by_league_season"
EVENTS_SERVICE = "data_api.services.events_service.get_fixture_events"
OFFICIAL_OBJECT = "fixtures + fixture_events"
EXPECTED_FIXTURE_KEYS = ["fixture", "teams"]
EXPECTED_EVENT_KEYS = ["type", "detail"]
