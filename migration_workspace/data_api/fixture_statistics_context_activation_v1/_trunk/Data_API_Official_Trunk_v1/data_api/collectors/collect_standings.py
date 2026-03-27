from __future__ import annotations
from data_api.collectors.common import write_json
from data_api.paths import season_root
from data_api.providers.standings_provider import fetch_standings

def collect_standings(league_id: int, season: int) -> dict:
    data = fetch_standings(league_id, season)
    root = season_root(league_id, season)
    write_json(root / "standings" / f"standings_league_{league_id}_season_{season}.json", data)
    return {"standings_collected": True}
