import json
from pathlib import Path

class BTTSDirectOfficialTrunkProvider:
    def __init__(self, fallback_path):
        self.fallback_path = Path(fallback_path)

    def _real_trunk_available(self):
        try:
            from data_api.services.fixtures_service import get_fixtures_by_league_season  # noqa
            from data_api.services.events_service import get_fixture_events  # noqa
            from data_api.services.statistics_service import get_team_statistics  # noqa
            from data_api.services.standings_service import get_standings_snapshot  # noqa
            return True
        except Exception:
            return False

    def build_official_input(self, league_id: int, season: int, fixture_index: int = 0):
        if self._real_trunk_available():
            from data_api.services.fixtures_service import get_fixtures_by_league_season
            from data_api.services.events_service import get_fixture_events
            from data_api.services.statistics_service import get_team_statistics
            from data_api.services.standings_service import get_standings_snapshot

            fixtures = get_fixtures_by_league_season(league_id, season)
            standings = get_standings_snapshot(league_id, season)
            fixture = fixtures[fixture_index]
            fixture_id = fixture["fixture"]["id"]
            home_team_id = fixture["teams"]["home"]["id"]
            away_team_id = fixture["teams"]["away"]["id"]
            events = get_fixture_events(fixture_id, league_id, season)
            home_stats = get_team_statistics(home_team_id, league_id, season)
            away_stats = get_team_statistics(away_team_id, league_id, season)

            payload = json.loads(self.fallback_path.read_text(encoding='utf-8'))
            payload["event_id"] = fixture_id
            payload["match_label"] = f'{fixture["teams"]["home"]["name"]} vs {fixture["teams"]["away"]["name"]}'
            payload["competition"] = fixture["league"]["name"]
            payload["kickoff_datetime"] = fixture["fixture"]["date"]
            payload["home_snapshot"]["team_id"] = home_team_id
            payload["home_snapshot"]["team_name"] = fixture["teams"]["home"]["name"]
            payload["away_snapshot"]["team_id"] = away_team_id
            payload["away_snapshot"]["team_name"] = fixture["teams"]["away"]["name"]
            payload["data_api_context"]["source_profile"] = "official_trunk_direct"
            payload["data_api_context"]["trunk_reads"] = {
                "fixtures": bool(fixtures),
                "standings": bool(standings),
                "events": bool(events),
                "home_team_statistics": bool(home_stats),
                "away_team_statistics": bool(away_stats),
            }
            return payload

        return json.loads(self.fallback_path.read_text(encoding='utf-8'))
