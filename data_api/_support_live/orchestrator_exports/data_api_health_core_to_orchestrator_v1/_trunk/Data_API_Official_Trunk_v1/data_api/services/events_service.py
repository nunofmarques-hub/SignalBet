from __future__ import annotations
import json
from data_api.paths import season_root

def get_fixture_events(fixture_id: int, league_id: int, season: int) -> list[dict]:
    path = season_root(league_id, season) / "events" / f"fixture_{fixture_id}.json"
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("response", []) or []
