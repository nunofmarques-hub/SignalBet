TRUNK_NAME = "Data_API_Official_Trunk_v1"
PROVIDER_NAME = "official_live_provider"
CONSUMED_SERVICES = [
    "data_api.services.fixtures_service.get_fixtures_by_league_season",
    "data_api.services.events_service.get_fixture_events",
]
CONSUMED_OBJECTS = ["fixtures_by_league_season", "fixture_events"]
OUTPUT_SCHEMA = "market_pick.v1.1"
