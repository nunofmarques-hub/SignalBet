from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def discover_modules(project_root: str, forced_modules: List[str] | None = None) -> List[Dict[str, Any]]:
    registry = Path(project_root) / "app_core" / "manifests" / "modules_registry.json"
    data = json.loads(registry.read_text(encoding="utf-8"))
    modules = data.get("modules", [])
    if forced_modules:
        modules = [m for m in modules if m["module_id"] in forced_modules]
    return sorted([m for m in modules if m.get("enabled")], key=lambda m: m.get("run_order", 999))


def run_modules(modules: List[Dict[str, Any]], run_context: Dict[str, Any]) -> List[Dict[str, Any]]:
    # Draft intencional: nesta fase simula resultados normalizados por módulo.
    results = []
    for module in modules:
        results.append({
            "module_id": module["module_id"],
            "status": "PASS",
            "warnings": [],
            "errors": [],
            "candidates_count": 0,
            "candidates_payload_ref": None,
            "execution_time_ms": 0,
        })
    return results
