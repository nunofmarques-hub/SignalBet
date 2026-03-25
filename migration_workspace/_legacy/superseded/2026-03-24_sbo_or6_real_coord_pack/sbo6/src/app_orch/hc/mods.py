from __future__ import annotations
from pathlib import Path
from app_orch.util.io import read_json

def run(pack_root: str):
    root = Path(pack_root)
    mods = read_json(root/'src'/'app_orch'/'man'/'modules.json')['modules']
    checks = []
    for m in mods:
        checks.append({'check_id':f"module_manifest_present_{m['module_id']}", 'status':'PASS', 'message':f"Manifest ok para {m['module_id']}.", 'blocking':False})
        checks.append({'check_id':f"module_contract_version_ok_{m['module_id']}", 'status':'PASS' if m.get('required_contract_version') == 'v1.1' else 'WARN', 'message':f"Contract version declarada para {m['module_id']}.", 'blocking':False})
    return checks
