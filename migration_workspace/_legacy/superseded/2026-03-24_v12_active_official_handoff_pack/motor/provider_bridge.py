from data_api.services.fixtures_service import get_fixtures_by_league_season
from data_api.services.standings_service import get_standings_snapshot
from data_api.services.statistics_service import get_fixture_statistics, get_team_statistics

OFFICIAL_PROVIDER_NAME = "Data_API_Official_Trunk_v1.services"
REQUIRED_OBJECTS = [
    "fixtures_catalog",
    "standings_snapshot",
    "fixture_statistics",
    "team_statistics",
]

def load_official_bundle(league_id:int, season:int, fixture_index:int=0) -> dict:
    fixtures = get_fixtures_by_league_season(league_id, season)
    standings = get_standings_snapshot(league_id, season)
    fixture = fixtures[fixture_index]
    fixture_id = fixture["fixture"]["id"]
    home_team_id = fixture["teams"]["home"]["id"]
    away_team_id = fixture["teams"]["away"]["id"]
    fixture_stats = get_fixture_statistics(fixture_id, league_id, season)
    home_team_stats = get_team_statistics(home_team_id, league_id, season)
    away_team_stats = get_team_statistics(away_team_id, league_id, season)
    return {
        "provider": OFFICIAL_PROVIDER_NAME,
        "league_id": league_id,
        "season": season,
        "fixture": fixture,
        "fixtures_catalog": fixtures,
        "standings_snapshot": standings,
        "fixture_statistics": fixture_stats,
        "home_team_statistics": home_team_stats,
        "away_team_statistics": away_team_stats,
    }
