from data_api.services.fixtures_service import get_fixtures_by_league_season
from data_api.services.standings_service import get_standings_snapshot
from data_api.services.statistics_service import get_fixture_statistics, get_team_statistics

OFFICIAL_PROVIDER_NAME = "Data_API_Official_Trunk_v1.services"
OFFICIAL_SERVICES_USED = [
    "get_fixtures_by_league_season",
    "get_standings_snapshot",
    "get_team_statistics",
    "get_fixture_statistics",
]
REQUIRED_OBJECTS = [
    "fixtures_catalog",
    "standings_snapshot",
    "fixture_statistics",
    "team_statistics",
]
REQUIRED_FIELDS = {
    "fixture": [
        "fixture.id",
        "fixture.date",
        "league.id",
        "league.name",
        "teams.home.id",
        "teams.home.name",
        "teams.away.id",
        "teams.away.name",
    ],
    "team_statistics": [
        "goals_for_per_game",
        "goals_against_per_game",
        "shots_on_target_per_game",
    ],
}


def _assert_required_fixture_fields(fixture: dict) -> None:
    fixture_id = fixture["fixture"]["id"]
    fixture_date = fixture["fixture"]["date"]
    league_id = fixture["league"]["id"]
    league_name = fixture["league"]["name"]
    home_id = fixture["teams"]["home"]["id"]
    home_name = fixture["teams"]["home"]["name"]
    away_id = fixture["teams"]["away"]["id"]
    away_name = fixture["teams"]["away"]["name"]
    _ = (fixture_id, fixture_date, league_id, league_name, home_id, home_name, away_id, away_name)


def _assert_required_team_stat_fields(stats: dict) -> None:
    _ = stats["goals_for_per_game"]
    _ = stats["goals_against_per_game"]
    _ = stats["shots_on_target_per_game"]


def load_official_bundle(league_id: int, season: int, fixture_index: int = 0) -> dict:
    fixtures = get_fixtures_by_league_season(league_id, season)
    standings = get_standings_snapshot(league_id, season)
    fixture = fixtures[fixture_index]
    _assert_required_fixture_fields(fixture)
    fixture_id = fixture["fixture"]["id"]
    home_team_id = fixture["teams"]["home"]["id"]
    away_team_id = fixture["teams"]["away"]["id"]
    fixture_stats = get_fixture_statistics(fixture_id, league_id, season)
    home_team_stats = get_team_statistics(home_team_id, league_id, season)
    away_team_stats = get_team_statistics(away_team_id, league_id, season)
    _assert_required_team_stat_fields(home_team_stats)
    _assert_required_team_stat_fields(away_team_stats)
    return {
        "provider": OFFICIAL_PROVIDER_NAME,
        "official_services_used": OFFICIAL_SERVICES_USED,
        "league_id": league_id,
        "season": season,
        "fixture": fixture,
        "fixtures_catalog": fixtures,
        "standings_snapshot": standings,
        "fixture_statistics": fixture_stats,
        "home_team_statistics": home_team_stats,
        "away_team_statistics": away_team_stats,
        "required_objects_used": REQUIRED_OBJECTS,
        "required_fields": REQUIRED_FIELDS,
    }
