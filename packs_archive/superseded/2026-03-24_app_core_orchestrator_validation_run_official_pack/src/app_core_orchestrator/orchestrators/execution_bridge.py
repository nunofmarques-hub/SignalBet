
from __future__ import annotations
from typing import Any, Dict

def register_execution(bankroll_output: Dict[str, Any], dry_run: bool) -> Dict[str, Any]:
    if dry_run:
        return {'status':'SKIPPED','message':'Validation/Dry run sem execution real.'}
    return {'status':'PASS','message':'Execution registada em draft.'}
