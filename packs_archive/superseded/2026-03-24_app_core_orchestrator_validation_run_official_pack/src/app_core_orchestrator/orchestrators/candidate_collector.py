
from __future__ import annotations
from typing import Any, Dict, List

def collect_candidates(run_id: str, module_outputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    candidates = []
    source_modules = []
    for output in module_outputs:
        source_modules.append(output['module_id'])
        candidates.extend(output.get('candidates', []))
    return {
        'run_id': run_id,
        'source_modules': source_modules,
        'candidate_count': len(candidates),
        'candidates': candidates,
    }
