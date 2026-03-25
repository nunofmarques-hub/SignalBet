
from __future__ import annotations
from pathlib import Path
from typing import Dict, List
from app_core_orchestrator.support.io import read_json

def run_module_checks(pack_root: str) -> List[Dict[str, object]]:
    root = Path(pack_root)
    registry = root / 'src' / 'app_core_orchestrator' / 'manifests' / 'modules_registry.json'
    statuses: List[Dict[str, object]] = []
    if not registry.exists():
        return [{'check_id':'module_manifest_present','status':'FAIL','message':'modules_registry.json em falta.','blocking':True}]
    data = read_json(registry)
    statuses.append({'check_id':'module_manifest_present','status':'PASS','message':'modules_registry.json presente.','blocking':True})
    enabled = [m for m in data.get('modules', []) if m.get('enabled')]
    entrypoint_ok = all((root / m['entrypoint']).exists() for m in enabled)
    statuses.append({'check_id':'module_entrypoint_present','status':'PASS' if entrypoint_ok else 'WARN','message':'Entrypoints dos módulos elegíveis localizados.' if entrypoint_ok else 'Há entrypoints de módulos elegíveis em falta.','blocking':False})
    version_ok = all(m.get('required_contract_version') == 'v1.1' for m in enabled)
    statuses.append({'check_id':'module_contract_version_ok','status':'PASS' if version_ok else 'WARN','message':'Versões contratuais consistentes.' if version_ok else 'Versões contratuais divergentes.','blocking':False})
    return statuses
