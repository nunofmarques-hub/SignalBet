from __future__ import annotations

OFFICIAL_SOURCE = 'Data_API_Official_Trunk_v1'
OFFICIAL_OBJECT = 'fixtures + fixture_events'
FIXTURES_SERVICE = 'data_api.services.fixtures_service.get_fixtures_by_league_season'
EVENTS_SERVICE = 'data_api.services.events_service.get_fixture_events'
MIN_FIXTURE_KEYS = ['fixture', 'teams']
MIN_EVENT_CARD_RULE = "type == 'Card' OR 'card' in detail.lower()"
