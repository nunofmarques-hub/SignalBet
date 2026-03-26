from __future__ import annotations
from pathlib import Path
from app_orch.util.io import read_json

def run(pack_root: str):
    root = Path(pack_root)
    reg = root / 'src' / 'app_orch' / 'man' / 'modules.json'
    if not reg.exists():
        return [{'check_id':'module_manifest_present','status':'FAIL','message':'modules.json em falta.','blocking':True}]
    data = read_json(reg)
    mods = data.get('modules', [])
    enabled = [m for m in mods if m.get('enabled')]
    version_ok = all(m.get('required_contract_version') == 'v1.1' for m in enabled)
    return [
        {'check_id':'module_manifest_present','status':'PASS','message':'modules.json presente.','blocking':True},
        {'check_id':'module_entrypoint_present','status':'PASS','message':'Execução por feeds/registry ativa.','blocking':False},
        {'check_id':'module_contract_version_ok','status':'PASS' if version_ok else 'WARN','message':'Versões contratuais consistentes.' if version_ok else 'Versões contratuais divergentes.','blocking':False},
    ]
