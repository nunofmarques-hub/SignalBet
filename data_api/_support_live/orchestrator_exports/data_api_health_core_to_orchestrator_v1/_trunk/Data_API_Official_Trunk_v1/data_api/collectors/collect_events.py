from __future__ import annotations
from data_api.collectors.common import load_state, save_state, write_json, read_json
from data_api.paths import season_root, state_root
from data_api.providers.events_provider import fetch_fixture_events

def collect_events(league_id: int, season: int, max_items: int = 10) -> dict:
    raw_root = season_root(league_id, season)
    fixture_ids = read_json(raw_root / "catalog" / "fixture_ids.json").get("fixture_ids", [])
    out_dir = raw_root / "events"
    state_file = state_root(league_id, season) / "resume_events.state.json"
    state = load_state(state_file, total=len(fixture_ids))
    done = set(state.get("done", []))
    pending = [fx for fx in fixture_ids if fx not in done and not (out_dir / f"fixture_{fx}.json").exists()][:max_items]
    for fx in pending:
        data = fetch_fixture_events(fx)
        write_json(out_dir / f"fixture_{fx}.json", data)
        done.add(fx)
        state["done"] = sorted(done)
        state["last_success_item"] = fx
        save_state(state_file, state)
    return {"events_collected_now": len(pending), "done_total": len(done)}
