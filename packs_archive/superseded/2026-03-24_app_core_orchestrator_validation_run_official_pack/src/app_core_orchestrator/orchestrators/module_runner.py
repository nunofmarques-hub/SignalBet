
from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List, Tuple
from app_core_orchestrator.support.io import read_json

def discover_modules(pack_root: str, forced_modules: List[str] | None = None) -> Tuple[List[Dict[str, Any]], List[str]]:
    root = Path(pack_root)
    registry = read_json(root / 'src' / 'app_core_orchestrator' / 'manifests' / 'modules_registry.json')
    modules = sorted(registry['modules'], key=lambda x: x['run_order'])
    selected = []
    skipped = []
    for module in modules:
        if not module.get('enabled'):
            skipped.append(module['module_id'])
            continue
        if forced_modules and module['module_id'] not in forced_modules:
            skipped.append(module['module_id'])
            continue
        selected.append(module)
    return selected, skipped

def run_modules(pack_root: str, modules: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    root = Path(pack_root)
    outputs = []
    for module in modules:
        payload = read_json(root / module['entrypoint'])
        outputs.append(payload)
    return outputs
