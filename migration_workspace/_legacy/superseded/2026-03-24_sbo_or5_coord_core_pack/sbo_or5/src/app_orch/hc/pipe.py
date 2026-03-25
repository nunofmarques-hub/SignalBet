from __future__ import annotations
from pathlib import Path

def run(pack_root: str):
    root = Path(pack_root)
    req = [root/'src'/'app_orch'/'orch'/'flow.py', root/'src'/'app_orch'/'orch'/'ui.py']
    ok = all(p.exists() for p in req)
    return [
        {'check_id':'gps_available','status':'PASS' if ok else 'WARN','message':'Flow GPS disponível em draft.' if ok else 'Flow GPS em falta.','blocking':False},
        {'check_id':'bankroll_available','status':'PASS' if ok else 'WARN','message':'Flow Banca disponível em draft.' if ok else 'Flow Banca em falta.','blocking':False},
        {'check_id':'execution_available','status':'PASS' if ok else 'WARN','message':'Bridge Execution disponível em draft.' if ok else 'Bridge Execution em falta.','blocking':False},
    ]
