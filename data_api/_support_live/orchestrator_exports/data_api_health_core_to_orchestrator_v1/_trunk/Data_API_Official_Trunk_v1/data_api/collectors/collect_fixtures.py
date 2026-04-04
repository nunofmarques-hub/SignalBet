from __future__ import annotations
from data_api.collectors.common import write_json
from data_api.paths import season_root
from data_api.providers.fixtures_provider import fetch_fixtures

def collect_fixtures(league_id: int, season: int, status: str = "FT-AET-PEN") -> dict:
    data = fetch_fixtures(league_id, season, status)
    root = season_root(league_id, season)
    write_json(root / "catalog" / f"fixtures_catalog_status_{status.replace('-', '_')}.json", data)
    fixture_ids = [r.get("fixture", {}).get("id") for r in data.get("response", []) or [] if r.get("fixture", {}).get("id")]
    write_json(root / "catalog" / "fixture_ids.json", {"league": league_id, "season": season, "status": status, "fixture_ids": fixture_ids})
    return {"fixtures_collected": len(fixture_ids)}
