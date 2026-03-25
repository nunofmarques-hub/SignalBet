from __future__ import annotations
from data_api.collectors.common import load_state, save_state, write_json, read_json
from data_api.paths import season_root, state_root
from data_api.providers.api_football_provider import ApiFootballProvider

def collect_team_statistics(league_id: int, season: int, max_items: int = 10) -> dict:
    provider = ApiFootballProvider()
    raw_root = season_root(league_id, season)
    cat = read_json(raw_root / "catalog" / "fixtures_catalog_status_FT_AET_PEN.json")
    team_ids = set()
    for r in cat.get("response", []) or []:
        for side in ("home", "away"):
            tid = r.get("teams", {}).get(side, {}).get("id")
            if tid:
                team_ids.add(tid)
    team_ids = sorted(team_ids)
    out_dir = raw_root / "team_statistics"
    state_file = state_root(league_id, season) / "resume_team_statistics.state.json"
    state = load_state(state_file, total=len(team_ids))
    done = set(state.get("done", []))
    pending = [tid for tid in team_ids if tid not in done and not (out_dir / f"team_{tid}.json").exists()][:max_items]
    for tid in pending:
        data = provider.get("/teams/statistics", {"league": league_id, "season": season, "team": tid})
        write_json(out_dir / f"team_{tid}.json", data)
        done.add(tid)
        state["done"] = sorted(done)
        state["last_success_item"] = tid
        save_state(state_file, state)
    return {"team_statistics_collected_now": len(pending), "done_total": len(done)}
