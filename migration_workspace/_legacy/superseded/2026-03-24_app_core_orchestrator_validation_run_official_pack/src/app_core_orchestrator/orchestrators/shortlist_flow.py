
from __future__ import annotations
from typing import Any, Dict

def run_global_pick_selector(opportunity_pool: Dict[str, Any]) -> Dict[str, Any]:
    ordered = sorted(opportunity_pool['candidates'], key=lambda x: x.get('confidence', 0), reverse=True)
    shortlist = ordered[:2]
    return {'status':'PASS','shortlist':shortlist,'selected_count':len(shortlist)}

def run_bankroll_manager(gps_output: Dict[str, Any]) -> Dict[str, Any]:
    approved = gps_output['shortlist'][:1]
    reduced = gps_output['shortlist'][1:]
    return {'status':'PASS','approved':approved,'reduced':reduced,'blocked':[],'reserve':[]}
