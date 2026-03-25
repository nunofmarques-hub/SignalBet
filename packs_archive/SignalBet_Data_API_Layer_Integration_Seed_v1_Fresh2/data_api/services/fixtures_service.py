from __future__ import annotations
import json
from data_api.paths import season_root

def get_fixtures_by_league_season(league_id: int, season: int, status: str = "FT-AET-PEN") -> list[dict]:
    path = season_root(league_id, season) / "catalog" / f"fixtures_catalog_status_{status.replace('-', '_')}.json"
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("response", []) or []
