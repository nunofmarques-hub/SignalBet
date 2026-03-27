from pathlib import Path
import json
from typing import Optional

def _read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def _find_data_api_root(project_root: Path) -> Optional[Path]:
    candidates = [
        project_root / "data_api" / "Data_API_Official_Trunk_v1" / "data_api",
        project_root / "Data_API_Official_Trunk_v1" / "data_api",
        project_root / "data_api",
    ]
    for c in candidates:
        if c.exists() and c.is_dir():
            return c
    return None

def _load_fixtures_baseline(data_api_root: Path) -> dict:
    manifest_path = data_api_root / "storage" / "storage_snapshot_manifest.json"
    state_dir = data_api_root / "storage" / "state" / "league_140" / "season_2024"
    catalog_path = data_api_root / "storage" / "raw" / "league_140" / "season_2024" / "catalog" / "fixtures_catalog_status_FT_AET_PEN.json"

    manifest = _read_json(manifest_path)
    state_files = sorted(state_dir.glob("*.state.json"))
    states = [_read_json(p) for p in state_files]
    catalog = _read_json(catalog_path)

    total_done = sum(len(s.get("done", [])) for s in states)
    total_failed = sum(len(s.get("failed", [])) for s in states)

    final_status = "green" if total_failed == 0 and total_done > 0 else ("degraded_run" if total_done > 0 else "hard_fail")
    snapshot_status = "fresh" if total_done > 0 else "stale"

    return {
        "flow_id": "fixtures",
        "flow_role": "primary_baseline",
        "provider_observed": "fixtures_provider.py",
        "scenario": "league_140 / season_2024 / status FT-AET-PEN",
        "snapshot_name": "storage_snapshot_manifest",
        "snapshot_status": snapshot_status,
        "final_status": final_status,
        "done_count": total_done,
        "failed_count": total_failed,
        "catalog_count": len(catalog) if isinstance(catalog, list) else (len(catalog.get("fixtures", [])) if isinstance(catalog, dict) else 0),
        "warnings": [],
        "blockers": [] if total_done > 0 else ["fixtures_baseline_unavailable"],
        "native_inputs": {
            "manifest_path": str(manifest_path),
            "state_files_count": len(state_files),
            "catalog_path": str(catalog_path),
            "minimum_expected_objects": manifest.get("minimum_expected_objects", []),
        },
    }

def _load_statistics_context(data_api_root: Path) -> dict:
    candidates = [
        data_api_root / "storage" / "state" / "league_140" / "season_2024" / "fixture_statistics_context_activation_v1.state.json",
        data_api_root / "storage" / "state" / "league_140" / "season_2024" / "statistics_context.state.json",
        data_api_root / "storage" / "state" / "league_140" / "season_2024" / "statistics_context_activation.state.json",
    ]
    found = None
    for c in candidates:
        if c.exists():
            found = c
            break

    if not found:
        return {
            "flow_id": "statistics_context",
            "flow_role": "complementary_non_blocking",
            "available": False,
            "final_status": "missing",
            "warnings": ["statistics_context_not_found"],
            "blockers": [],
            "non_blocking": True,
            "observed_path": None,
            "statistics_available_count": 0,
            "statistics_missing_count": 0,
        }

    payload = _read_json(found)
    result = payload.get("result") or payload.get("final_status") or payload.get("status") or "green"
    stats_av = payload.get("statistics_available_count", payload.get("available_count", 0))
    stats_miss = payload.get("statistics_missing_count", payload.get("missing_count", 0))
    return {
        "flow_id": "statistics_context",
        "flow_role": "complementary_non_blocking",
        "available": True,
        "final_status": "green" if result == "green" else ("degraded_run" if result in ("degraded_run", "warn", "usable") else "hard_fail"),
        "warnings": [] if result == "green" else [f"statistics_context_{result}"],
        "blockers": [],
        "non_blocking": True,
        "observed_path": str(found),
        "statistics_available_count": stats_av,
        "statistics_missing_count": stats_miss,
        "raw_status": result,
    }

def load_central_corridor(project_root: Path | None = None):
    if project_root:
        root = _find_data_api_root(project_root)
        if root:
            fixtures = _load_fixtures_baseline(root)
            stats = _load_statistics_context(root)
            return {"fixtures": fixtures, "statistics_context": stats}, "project"

    fixtures = {
        "flow_id": "fixtures",
        "flow_role": "primary_baseline",
        "provider_observed": "fixtures_provider.py",
        "scenario": "league_140 / season_2024 / status FT-AET-PEN",
        "snapshot_name": "storage_snapshot_manifest",
        "snapshot_status": "fresh",
        "final_status": "green",
        "done_count": 10,
        "failed_count": 0,
        "catalog_count": 10,
        "warnings": [],
        "blockers": [],
        "native_inputs": {},
    }
    stats = {
        "flow_id": "statistics_context",
        "flow_role": "complementary_non_blocking",
        "available": True,
        "final_status": "green",
        "warnings": [],
        "blockers": [],
        "non_blocking": True,
        "observed_path": "demo",
        "statistics_available_count": 10,
        "statistics_missing_count": 0,
        "raw_status": "green",
    }
    return {"fixtures": fixtures, "statistics_context": stats}, "demo"
