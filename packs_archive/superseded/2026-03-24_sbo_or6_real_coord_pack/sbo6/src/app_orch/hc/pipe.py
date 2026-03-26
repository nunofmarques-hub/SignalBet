from __future__ import annotations
from pathlib import Path

def run(pack_root: str, project_root: str):
    root = Path(pack_root)
    proj = Path(project_root)
    flow = root/'src'/'app_orch'/'orch'/'flow.py'
    ui = root/'src'/'app_orch'/'orch'/'ui.py'
    gps_hint = any((proj/p).exists() for p in ['gps', 'global_pick_selector', 'modules/gps'])
    bank_hint = any((proj/p).exists() for p in ['bankroll', 'banca', 'modules/bankroll'])
    exec_hint = any((proj/p).exists() for p in ['execution', 'tracking', 'modules/execution'])
    code_ok = flow.exists() and ui.exists()
    return [
        {'check_id':'gps_available','status':'PASS' if code_ok else 'WARN','message':'Flow GPS disponível em draft.' if code_ok else 'Flow GPS em falta.','blocking':False},
        {'check_id':'gps_project_hint','status':'PASS' if gps_hint else 'WARN','message':'Hint de GPS encontrado no projeto.' if gps_hint else 'Sem hint físico de GPS no projeto.','blocking':False},
        {'check_id':'bankroll_available','status':'PASS' if code_ok else 'WARN','message':'Flow Banca disponível em draft.' if code_ok else 'Flow Banca em falta.','blocking':False},
        {'check_id':'bank_project_hint','status':'PASS' if bank_hint else 'WARN','message':'Hint de Banca encontrado no projeto.' if bank_hint else 'Sem hint físico de Banca no projeto.','blocking':False},
        {'check_id':'execution_available','status':'PASS' if code_ok else 'WARN','message':'Bridge Execution disponível em draft.' if code_ok else 'Bridge Execution em falta.','blocking':False},
        {'check_id':'execution_project_hint','status':'PASS' if exec_hint else 'WARN','message':'Hint de Execution encontrado no projeto.' if exec_hint else 'Sem hint físico de Execution no projeto.','blocking':False},
    ]
