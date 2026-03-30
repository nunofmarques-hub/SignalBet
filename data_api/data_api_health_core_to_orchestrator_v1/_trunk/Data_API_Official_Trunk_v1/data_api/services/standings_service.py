from __future__ import annotations
import json
from data_api.paths import season_root

def get_standings_snapshot(league_id: int, season: int) -> list[dict]:
    path = season_root(league_id, season) / "standings" / f"standings_league_{league_id}_season_{season}.json"
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("response", []) or []
