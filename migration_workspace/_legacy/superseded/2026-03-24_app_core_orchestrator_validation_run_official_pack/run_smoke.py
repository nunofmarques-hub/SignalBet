
from __future__ import annotations
from pathlib import Path
import sys
import json

PACK_ROOT = Path(__file__).resolve().parent
SRC_ROOT = PACK_ROOT / 'src'
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from app_core_orchestrator.launcher.run_validation_pipeline import run_validation_pipeline
from app_core_orchestrator.support.io import read_json


def main() -> int:
    request = read_json(PACK_ROOT / 'examples' / 'requests' / 'sample_input.json')
    result = run_validation_pipeline(request, PACK_ROOT)
    print(json.dumps({
        'run_id': result['run_summary']['run_id'],
        'preflight_status': result['run_summary']['preflight_status'],
        'official_trunk_status': result['run_summary']['official_trunk_status'],
        'modules_run': result['run_summary']['modules_run'],
        'candidates_generated': result['run_summary']['candidates_generated'],
        'execution_status': result['run_summary']['execution_status'],
    }, indent=2, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
