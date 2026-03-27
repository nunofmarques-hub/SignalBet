from pathlib import Path
import json
from typing import Optional

DEFAULT_BASELINE_PATH = "examples/demo_data_api/baselines/baseline_state_green.json"

def _read_json(path: Path) -> dict:
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

def _build_native_baseline(data_api_root: Path) -> dict:
    manifest_path = data_api_root / "storage" / "storage_snapshot_manifest.json"
    state_dir = data_api_root / "storage" / "state" / "league_140" / "season_2024"
    catalog_path = data_api_root / "storage" / "raw" / "league_140" / "season_2024" / "catalog" / "fixtures_catalog_status_FT_AET_PEN.json"

    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest_not_found:{manifest_path}")
    if not state_dir.exists():
        raise FileNotFoundError(f"state_dir_not_found:{state_dir}")
    if not catalog_path.exists():
        raise FileNotFoundError(f"catalog_not_found:{catalog_path}")

    manifest = _read_json(manifest_path)
    state_files = sorted(state_dir.glob("*.state.json"))
    if not state_files:
        raise FileNotFoundError(f"state_files_not_found:{state_dir}")

    states = [_read_json(p) for p in state_files]
    catalog = _read_json(catalog_path)

    total_done = sum(len(s.get("done", [])) for s in states)
    total_failed = sum(len(s.get("failed", [])) for s in states)

    if total_failed > 0:
        final_status = "degraded_run"
    else:
        final_status = "green"

    snapshot_status = "fresh" if total_done > 0 else "stale"

    warnings = []
    blockers = []

    if total_done == 0:
        final_status = "hard_fail"
        blockers.append("no_completed_items_in_state_files")

    return {
        "provider_observed": "fixtures_provider.py",
        "baseline_scenario": "league_140 / season_2024 / status FT-AET-PEN",
        "snapshot_name": "storage_snapshot_manifest",
        "snapshot_status": snapshot_status,
        "final_status": final_status,
        "warnings": warnings,
        "blockers": blockers,
        "coverage_state": "unlocked",
        "technical_stability": "confirmed",
        "consumer_primary": "orchestrator",
        "native_inputs": {
            "data_api_root": str(data_api_root),
            "manifest_path": str(manifest_path),
            "state_files": [str(p) for p in state_files],
            "catalog_path": str(catalog_path),
            "catalog_fixtures_count": len(catalog) if isinstance(catalog, list) else (len(catalog.get("fixtures", [])) if isinstance(catalog, dict) else 0),
            "minimum_expected_objects": manifest.get("minimum_expected_objects", []),
            "total_done": total_done,
            "total_failed": total_failed,
        },
    }

def load_baseline_state(project_root: Path | None = None, explicit_path: str | None = None) -> tuple[dict, str]:
    if explicit_path:
        p = Path(explicit_path)
        if p.exists():
            return _read_json(p), "explicit"

    if project_root:
        data_api_root = _find_data_api_root(project_root)
        if data_api_root:
            try:
                return _build_native_baseline(data_api_root), "project"
            except Exception:
                pass

    local = Path(__file__).resolve().parents[3] / DEFAULT_BASELINE_PATH
    return _read_json(local), "demo"
