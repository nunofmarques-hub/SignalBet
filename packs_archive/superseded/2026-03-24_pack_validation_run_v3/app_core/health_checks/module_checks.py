from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List


def run_module_checks(project_root: str) -> List[Dict[str, object]]:
    registry = Path(project_root) / "app_core" / "manifests" / "modules_registry.json"
    checks: List[Dict[str, object]] = []
    checks.append({"check_id": "module_manifest_present", "status": "PASS" if registry.exists() else "FAIL", "message": "modules_registry.json encontrado." if registry.exists() else "modules_registry.json em falta.", "blocking": True})

    entrypoints_ok = False
    contracts_ok = False
    if registry.exists():
        data = json.loads(registry.read_text(encoding="utf-8"))
        modules = data.get("modules", [])
        entrypoints_ok = all(":" in module.get("entrypoint", "") for module in modules)
        contracts_ok = all(module.get("required_contract_version") == "1.1" for module in modules)

    checks.append({"check_id": "module_entrypoint_present", "status": "PASS" if entrypoints_ok else "WARN", "message": "Entrypoints de módulos válidos." if entrypoints_ok else "Entrypoints de módulos incompletos ou em falta.", "blocking": False})
    checks.append({"check_id": "module_contract_version_ok", "status": "PASS" if contracts_ok else "WARN", "message": "Versões contratuais de módulos alinhadas." if contracts_ok else "Versões contratuais desalinhadas ou em falta.", "blocking": False})
    return checks
