
from __future__ import annotations
from pathlib import Path
from typing import Dict, List

def run_pipeline_checks(pack_root: str) -> List[Dict[str, object]]:
    root = Path(pack_root)
    required = [
        root / 'src' / 'app_core_orchestrator' / 'orchestrators' / 'shortlist_flow.py',
        root / 'src' / 'app_core_orchestrator' / 'orchestrators' / 'execution_bridge.py',
        root / 'src' / 'app_core_orchestrator' / 'orchestrators' / 'ui_response_builder.py',
    ]
    all_present = all(p.exists() for p in required)
    return [
        {'check_id':'gps_available','status':'PASS' if all_present else 'WARN','message':'Bridge para GPS disponível em draft.' if all_present else 'Bridge para GPS incompleta.','blocking':False},
        {'check_id':'bankroll_available','status':'PASS' if all_present else 'WARN','message':'Bridge para Banca disponível em draft.' if all_present else 'Bridge para Banca incompleta.','blocking':False},
        {'check_id':'execution_available','status':'PASS' if all_present else 'WARN','message':'Bridge para Execution disponível em draft.' if all_present else 'Bridge para Execution incompleta.','blocking':False},
    ]
