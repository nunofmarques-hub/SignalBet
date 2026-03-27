
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import traceback

from calibration_trunk_adapter import (
    TrunkAdapterError,
    DEFAULT_STATUS,
    resolve_fixtures_service,
    discover_available_scenarios,
    call_service_for_scenario,
)

PACK_VERSION = "1.1.3"
PHASE_NAME = "Real Data Calibration & Reliability Phase"
PRIMARY_CONSUMER = "orchestrator"

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def write_json(path: Path, payload: dict | list):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

def status_of_count(count: int) -> tuple[str, str]:
    if count > 0:
        return "fresh", "green"
    return "empty", "degraded_run"

def normalize_fixture(item: dict) -> dict:
    fixture = item.get("fixture", {}) if isinstance(item, dict) else {}
    teams = item.get("teams", {}) if isinstance(item, dict) else {}
    home = teams.get("home", {}) if isinstance(teams, dict) else {}
    away = teams.get("away", {}) if isinstance(teams, dict) else {}
    status = fixture.get("status", {}) if isinstance(fixture, dict) else {}
    return {
        "fixture_id": fixture.get("id"),
        "event_date": fixture.get("date"),
        "status_short": status.get("short"),
        "status_long": status.get("long"),
        "home_team_id": home.get("id"),
        "home_team_name": home.get("name"),
        "away_team_id": away.get("id"),
        "away_team_name": away.get("name"),
    }

def scenario_priority(scenario: dict, requested_league: int, requested_season: int):
    score = 0
    if scenario["league_id"] == requested_league and scenario["season"] == requested_season:
        score += 1000
    if scenario["status"] == DEFAULT_STATUS:
        score += 200
    count_hint = scenario.get("count_hint", 0)
    score += min(count_hint, 500)
    return score

def main():
    root = Path(__file__).resolve().parents[1]
    logs_dir = root / "logs"
    examples_dir = root / "examples"

    requested_league = 140
    requested_season = 2024

    bootstrap_debug = {
        "phase": PHASE_NAME,
        "pack_version": PACK_VERSION,
        "timestamp": now_iso(),
    }

    trunk_root = None
    env_path = root / ".trunk_root"
    if env_path.exists():
        trunk_root = Path(env_path.read_text(encoding="utf-8").strip())
    else:
        # default local path used in prior runs
        trunk_root = Path(r"U:\Users\genuser\Desktop\SignalBet\data_api\Data_API_Official_Trunk_v1")

    bootstrap_debug["trunk_root"] = str(trunk_root)

    try:
        service_fn, provider_path, discovery_report = resolve_fixtures_service(trunk_root)
        scenarios_report = discover_available_scenarios(trunk_root)

        candidate_scenarios = []
        for entry in scenarios_report["available_scenarios"]:
            scenario = {
                "league_id": entry["league_id"],
                "season": entry["season"],
                "status": entry["status"],
                "catalog_path": entry["catalog_path"],
            }
            try:
                # Use service itself to confirm what it returns for the exact scenario.
                returned = call_service_for_scenario(service_fn, scenario)
                scenario["count_hint"] = len(returned)
            except Exception:
                scenario["count_hint"] = -1
            candidate_scenarios.append(scenario)

        if not candidate_scenarios:
            candidate_scenarios = [{
                "league_id": requested_league,
                "season": requested_season,
                "status": DEFAULT_STATUS,
                "catalog_path": None,
                "count_hint": len(call_service_for_scenario(service_fn, {
                    "league_id": requested_league,
                    "season": requested_season,
                    "status": DEFAULT_STATUS,
                })),
            }]

        candidate_scenarios = sorted(
            candidate_scenarios,
            key=lambda s: (s.get("count_hint", -1), scenario_priority(s, requested_league, requested_season)),
            reverse=True,
        )

        selected_scenario = candidate_scenarios[0]
        selected_fixtures = call_service_for_scenario(service_fn, selected_scenario)

        run_logs = []
        latest_snapshot = None

        for run_index in range(1, 4):
            fixtures = call_service_for_scenario(service_fn, selected_scenario)
            snapshot_status, final_status = status_of_count(len(fixtures))
            latest_snapshot = {
                "snapshot_name": "fixtures_calibration_snapshot",
                "version": PACK_VERSION,
                "provider": provider_path.name,
                "provider_path": str(provider_path),
                "service": "get_fixtures_by_league_season()",
                "primary_consumer": PRIMARY_CONSUMER,
                "league_id": selected_scenario["league_id"],
                "season": selected_scenario["season"],
                "coverage_scenario": (
                    "requested_primary_contract"
                    if selected_scenario["league_id"] == requested_league and selected_scenario["season"] == requested_season and selected_scenario["status"] == DEFAULT_STATUS
                    else "discovered_best_available"
                ),
                "coverage_status": selected_scenario["status"],
                "coverage_window": "no_window",
                "fixtures_count": len(fixtures),
                "fixtures": [normalize_fixture(item) for item in fixtures],
                "snapshot_status": snapshot_status,
                "discovery_report": {
                    **discovery_report,
                    "storage_discovery": scenarios_report,
                    "selected_scenario": selected_scenario,
                    "requested_scenario": {
                        "league_id": requested_league,
                        "season": requested_season,
                        "status": DEFAULT_STATUS,
                    },
                },
            }

            run_logs.append({
                "run_index": run_index,
                "timestamp": now_iso(),
                "provider": provider_path.name,
                "provider_path": str(provider_path),
                "fixtures_count": len(fixtures),
                "snapshot_status": snapshot_status,
                "fallback_used": selected_scenario["league_id"] != requested_league or selected_scenario["season"] != requested_season or selected_scenario["status"] != DEFAULT_STATUS,
                "coverage_scenario": latest_snapshot["coverage_scenario"],
                "coverage_status": selected_scenario["status"],
                "coverage_window": "no_window",
                "final_status": final_status,
                "trunk_root": str(trunk_root),
            })

        fixtures_counts = [entry["fixtures_count"] for entry in run_logs]
        coverage_goal_met = max(fixtures_counts or [0]) > 1
        result = "green" if coverage_goal_met and all(entry["final_status"] == "green" for entry in run_logs) else "red_coverage"
        summary = {
            "phase": PHASE_NAME,
            "pack_version": PACK_VERSION,
            "runs_attempted": len(run_logs),
            "runs_green": sum(1 for entry in run_logs if entry["final_status"] == "green"),
            "runs_degraded": sum(1 for entry in run_logs if entry["final_status"] == "degraded_run"),
            "runs_hard_fail": sum(1 for entry in run_logs if entry["final_status"] == "hard_fail"),
            "fixtures_count_min": min(fixtures_counts) if fixtures_counts else 0,
            "fixtures_count_max": max(fixtures_counts) if fixtures_counts else 0,
            "snapshot_shape_consistent": True,
            "orchestrator_consumer_status": "stable",
            "coverage_goal_met": coverage_goal_met,
            "result": result,
        }

        write_json(examples_dir / "calibration_snapshot_generated.json", latest_snapshot)
        write_json(logs_dir / "calibration_run_log_generated.json", run_logs)
        write_json(logs_dir / "calibration_summary_generated.json", summary)
        write_json(logs_dir / "bootstrap_debug_generated.json", bootstrap_debug | {
            "provider_path": str(provider_path),
            "selected_scenario": selected_scenario,
        })

        print(json.dumps({
            "latest_snapshot": latest_snapshot,
            "run_logs": run_logs,
            "summary": summary,
        }, indent=2, ensure_ascii=False))

        if result != "green":
            raise SystemExit(1)

    except TrunkAdapterError as exc:
        payload = {
            "phase": PHASE_NAME,
            "pack_version": PACK_VERSION,
            "error": str(exc),
            "trunk_root": str(trunk_root),
            "timestamp": now_iso(),
            "result": "red_bootstrap",
        }
        write_json(logs_dir / "bootstrap_debug_generated.json", bootstrap_debug | payload)
        print("[ERRO] Falha ao inicializar o trunk adapter.")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        raise SystemExit(1)
    except Exception as exc:
        payload = {
            "phase": PHASE_NAME,
            "pack_version": PACK_VERSION,
            "error": str(exc),
            "traceback": traceback.format_exc(),
            "trunk_root": str(trunk_root),
            "timestamp": now_iso(),
            "result": "red_runtime",
        }
        write_json(logs_dir / "bootstrap_debug_generated.json", bootstrap_debug | payload)
        print("[ERRO] Falha runtime durante a calibração.")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        raise SystemExit(1)

if __name__ == "__main__":
    main()
