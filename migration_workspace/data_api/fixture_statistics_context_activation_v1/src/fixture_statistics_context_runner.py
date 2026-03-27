from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
PACK_ROOT = CURRENT_DIR.parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from statistics_context_trunk_adapter import StatisticsContextTrunkAdapter

DEFAULT_TRUNK_ROOT = PACK_ROOT / "_trunk" / "Data_API_Official_Trunk_v1"
SCENARIO = {"league_id": 140, "season": 2024, "status": "FT-AET-PEN"}


def _now():
    return datetime.now(timezone.utc).isoformat()


def _parse_fixture_base(item: dict) -> dict:
    fixture = item.get("fixture", {})
    teams = item.get("teams", {})
    status = fixture.get("status", {})
    return {
        "fixture_id": fixture.get("id"),
        "event_date": fixture.get("date"),
        "status_short": status.get("short"),
        "status_long": status.get("long"),
        "home_team_id": (teams.get("home") or {}).get("id"),
        "home_team_name": (teams.get("home") or {}).get("name"),
        "away_team_id": (teams.get("away") or {}).get("id"),
        "away_team_name": (teams.get("away") or {}).get("name"),
    }


def _summarize_stats(stat_rows: list[dict]) -> list[dict]:
    summary = []
    for row in stat_rows:
        team = row.get("team", {})
        mapped = {}
        for stat in row.get("statistics", []) or []:
            stype = stat.get("type")
            if stype in {"Ball Possession", "Total Shots", "Shots on Goal", "Corner Kicks", "Fouls", "Yellow Cards", "Red Cards", "Passes %"}:
                mapped[stype] = stat.get("value")
        summary.append({
            "team_id": team.get("id"),
            "metrics": mapped,
        })
    return summary


def main():
    trunk_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_TRUNK_ROOT.resolve()
    output_dir = PACK_ROOT / "logs"
    examples_dir = PACK_ROOT / "examples"
    output_dir.mkdir(parents=True, exist_ok=True)
    examples_dir.mkdir(parents=True, exist_ok=True)

    adapter = StatisticsContextTrunkAdapter(trunk_root)
    fixtures = adapter.load_fixtures(**SCENARIO)

    protected_items = []
    run_logs = []
    baseline_ok = bool(fixtures)

    for fixture in fixtures:
        base = _parse_fixture_base(fixture)
        stats = adapter.load_statistics(base["fixture_id"], SCENARIO["league_id"], SCENARIO["season"])
        available = len(stats) > 0
        protected = {
            **base,
            "statistics_status": "available" if available else "missing",
            "fallback_used": not available,
            "statistics_context": _summarize_stats(stats) if available else [],
        }
        protected_items.append(protected)
        run_logs.append({
            "timestamp": _now(),
            "fixture_id": base["fixture_id"],
            "provider_path": adapter.discovery_report["chosen_statistics_service_path"],
            "statistics_status": protected["statistics_status"],
            "fallback_used": protected["fallback_used"],
            "final_status": "green" if baseline_ok else "hard_fail",
        })

    summary = {
        "phase": "fixture_statistics_context_activation_v1",
        "timestamp": _now(),
        "trunk_root": str(trunk_root),
        "scenario": SCENARIO,
        "baseline_fixtures_count": len(fixtures),
        "statistics_available_count": sum(1 for x in protected_items if x["statistics_status"] == "available"),
        "statistics_missing_count": sum(1 for x in protected_items if x["statistics_status"] == "missing"),
        "orchestrator_consumer_status": "usable" if baseline_ok else "blocked",
        "non_blocking_preserved": baseline_ok,
        "result": "green" if baseline_ok else "hard_fail",
    }

    protected_output = {
        "output_name": "fixture_statistics_context_protected_output",
        "version": "1.0.0",
        "primary_consumer": "orchestrator",
        "baseline_source": "fixtures_service.py:get_fixtures_by_league_season",
        "statistics_source": "statistics_service.py:get_fixture_statistics",
        "scenario": SCENARIO,
        "items": protected_items,
        "discovery_report": adapter.discovery_report,
        "summary": summary,
    }

    (examples_dir / "protected_fixture_statistics_output_generated.json").write_text(
        json.dumps(protected_output, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (output_dir / "fixture_statistics_context_run_log_generated.json").write_text(
        json.dumps(run_logs, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (output_dir / "fixture_statistics_context_summary_generated.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(json.dumps(protected_output, ensure_ascii=False, indent=2))
    if summary["result"] != "green":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
