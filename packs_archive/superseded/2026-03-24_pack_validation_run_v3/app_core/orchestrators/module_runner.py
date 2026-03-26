from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Dict, List


def _load_registry(project_root: str) -> Dict[str, Any]:
    registry = Path(project_root) / "app_core" / "manifests" / "modules_registry.json"
    return json.loads(registry.read_text(encoding="utf-8"))


def discover_modules(project_root: str, run_profile: str, forced_modules: List[str] | None = None) -> tuple[list[dict[str, Any]], list[str]]:
    data = _load_registry(project_root)
    modules = data.get("modules", [])
    profiles = json.loads((Path(project_root) / "app_core" / "manifests" / "run_profiles.json").read_text(encoding="utf-8"))
    profile_def = profiles.get("profiles", {}).get(run_profile, {})
    validation_subset = set(profile_def.get("validation_subset", []))
    subset_only = profile_def.get("subset_only", False)

    skipped: List[str] = []
    eligible: List[Dict[str, Any]] = []
    for module in modules:
        if forced_modules and module["module_id"] not in forced_modules:
            skipped.append(module["module_id"])
            continue
        if not module.get("enabled"):
            skipped.append(module["module_id"])
            continue
        if subset_only and validation_subset and module["module_id"] not in validation_subset:
            skipped.append(module["module_id"])
            continue
        eligible.append(module)

    eligible = sorted(eligible, key=lambda m: m.get("run_order", 999))
    return eligible, skipped


def run_modules(modules: List[Dict[str, Any]], run_context: Dict[str, Any]) -> List[Dict[str, Any]]:
    project_root = Path(run_context["project_root"])
    results = []
    for module in modules:
        start = time.perf_counter()
        sample_path = project_root / module["sample_output"]
        payload = json.loads(sample_path.read_text(encoding="utf-8")) if sample_path.exists() else {"candidates": []}
        elapsed = int((time.perf_counter() - start) * 1000)
        results.append({
            "module_id": module["module_id"],
            "status": payload.get("status", "PASS"),
            "warnings": payload.get("warnings", []),
            "errors": payload.get("errors", []),
            "candidates_count": len(payload.get("candidates", [])),
            "candidates_payload_ref": str(sample_path.relative_to(project_root)) if sample_path.exists() else None,
            "candidates": payload.get("candidates", []),
            "execution_time_ms": elapsed,
        })
    return results
