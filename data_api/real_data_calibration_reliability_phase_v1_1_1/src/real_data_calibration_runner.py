from __future__ import annotations

import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from calibration_trunk_adapter import AdapterError, TrunkAdapter, dump_json

RUNS = 3


def classify_run(snapshot: Dict[str, Any]) -> str:
    if snapshot.get("fixtures_count", 0) > 0:
        return "green"
    return "degraded_run"


def shape_signature(snapshot: Dict[str, Any]) -> List[str]:
    fixtures = snapshot.get("fixtures", [])
    if not fixtures:
        return []
    keys = sorted(fixtures[0].keys())
    return keys


def orchestrator_consumer_status(snapshot: Dict[str, Any]) -> str:
    mandatory = {
        "fixture_id",
        "event_date",
        "status_short",
        "home_team_id",
        "away_team_id",
        "home_team_name",
        "away_team_name",
    }
    fixtures = snapshot.get("fixtures", [])
    for item in fixtures:
        if not mandatory.issubset(set(item.keys())):
            return "unstable"
    return "stable"


def result_status(summary: Dict[str, Any]) -> str:
    if summary["runs_hard_fail"] > 0:
        return "red_bootstrap"
    if not summary["snapshot_shape_consistent"]:
        return "red"
    if summary["orchestrator_consumer_status"] != "stable":
        return "red"
    if summary["fixtures_count_max"] <= 1:
        return "red_coverage"
    return "green"


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    examples_dir = root / "examples"
    logs_dir = root / "logs"
    examples_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)

    trunk_root = os.environ.get(
        "SIGNALBET_TRUNK_ROOT",
        r"U:\Users\genuser\Desktop\SignalBet\data_api\Data_API_Official_Trunk_v1",
    )

    run_logs: List[Dict[str, Any]] = []
    snapshots: List[Dict[str, Any]] = []
    latest_snapshot: Dict[str, Any] = {}

    try:
        adapter = TrunkAdapter(trunk_root)
    except Exception as exc:  # noqa: BLE001
        error_payload = {
            "phase": "Real Data Calibration & Reliability Phase",
            "pack_version": "1.1.1",
            "error": str(exc),
            "trunk_root": trunk_root,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "result": "red_bootstrap",
        }
        dump_json(logs_dir / "calibration_summary_generated.json", error_payload)
        print("[ERRO] Falha ao inicializar o trunk adapter.")
        print(json.dumps(error_payload, ensure_ascii=False, indent=2))
        return 1

    for idx in range(1, RUNS + 1):
        timestamp = datetime.now(timezone.utc).isoformat()
        try:
            snapshot = adapter.fetch_best_snapshot()
            final_status = classify_run(snapshot)
            latest_snapshot = snapshot
            snapshots.append(snapshot)
            run_logs.append(
                {
                    "run_index": idx,
                    "timestamp": timestamp,
                    "provider": snapshot.get("provider"),
                    "provider_path": snapshot.get("provider_path"),
                    "fixtures_count": snapshot.get("fixtures_count"),
                    "snapshot_status": snapshot.get("snapshot_status"),
                    "fallback_used": snapshot.get("coverage_scenario") != "primary_status_expanded",
                    "coverage_scenario": snapshot.get("coverage_scenario"),
                    "coverage_statuses": snapshot.get("coverage_statuses"),
                    "coverage_window": snapshot.get("coverage_window"),
                    "final_status": final_status,
                    "trunk_root": trunk_root,
                }
            )
        except AdapterError as exc:
            run_logs.append(
                {
                    "run_index": idx,
                    "timestamp": timestamp,
                    "provider": "fixtures_provider.py",
                    "fixtures_count": 0,
                    "snapshot_status": "error",
                    "fallback_used": False,
                    "final_status": "hard_fail",
                    "error": str(exc),
                    "trunk_root": trunk_root,
                }
            )
        except Exception as exc:  # noqa: BLE001
            run_logs.append(
                {
                    "run_index": idx,
                    "timestamp": timestamp,
                    "provider": "fixtures_provider.py",
                    "fixtures_count": 0,
                    "snapshot_status": "error",
                    "fallback_used": False,
                    "final_status": "hard_fail",
                    "error": f"unexpected: {exc}",
                    "trunk_root": trunk_root,
                }
            )

    counts = Counter(log["final_status"] for log in run_logs)
    shape_signatures = [tuple(shape_signature(snapshot)) for snapshot in snapshots if snapshot]
    snapshot_shape_consistent = len(set(shape_signatures)) <= 1 if shape_signatures else False
    fixtures_counts = [log.get("fixtures_count", 0) for log in run_logs]
    orchestrator_statuses = [orchestrator_consumer_status(snapshot) for snapshot in snapshots if snapshot]
    orchestrator_status = "stable" if orchestrator_statuses and all(s == "stable" for s in orchestrator_statuses) else "unstable"

    summary: Dict[str, Any] = {
        "phase": "Real Data Calibration & Reliability Phase",
        "pack_version": "1.1.1",
        "runs_attempted": RUNS,
        "runs_green": counts.get("green", 0),
        "runs_degraded": counts.get("degraded_run", 0),
        "runs_hard_fail": counts.get("hard_fail", 0),
        "fixtures_count_min": min(fixtures_counts) if fixtures_counts else 0,
        "fixtures_count_max": max(fixtures_counts) if fixtures_counts else 0,
        "snapshot_shape_consistent": snapshot_shape_consistent,
        "orchestrator_consumer_status": orchestrator_status,
        "coverage_goal_met": (max(fixtures_counts) if fixtures_counts else 0) > 1,
        "result": "pending",
    }
    summary["result"] = result_status(summary)

    payload = {
        "latest_snapshot": latest_snapshot,
        "run_logs": run_logs,
        "summary": summary,
    }

    dump_json(examples_dir / "calibration_snapshot_generated.json", payload)
    dump_json(logs_dir / "calibration_run_log_generated.json", {"run_logs": run_logs})
    dump_json(logs_dir / "calibration_summary_generated.json", summary)

    print(json.dumps(payload, ensure_ascii=False, indent=2))

    if summary["result"] != "green":
        print()
        print("[ERRO] Real Data Calibration and Reliability Phase terminou com erro.")
        return 1

    print()
    print("[OK] Real Data Calibration and Reliability Phase terminou com sucesso.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
