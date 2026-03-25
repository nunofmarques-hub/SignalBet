from __future__ import annotations
from pathlib import Path
import sys, json, os
PACK_ROOT = Path(__file__).resolve().parent
SRC = PACK_ROOT / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
from app_orch.launcher.run_val import run_validation_pipeline
from app_orch.util.io import read_json

def main() -> int:
    req = read_json(PACK_ROOT / 'examples' / 'req' / 'sample.json')
    if os.getenv('SIGNALBET_PROJECT_ROOT'):
        req['project_root'] = os.getenv('SIGNALBET_PROJECT_ROOT')
    result = run_validation_pipeline(req, PACK_ROOT)
    summary = result['run_summary']
    ui = result['ui_status']
    print(json.dumps({
        'run_id': summary['run_id'],
        'preflight_status': summary['preflight_status'],
        'official_trunk_status': summary['official_trunk_status'],
        'project_mode': summary['project_mode'],
        'modules_eligible': summary['modules_eligible'],
        'modules_run': summary['modules_run'],
        'modules_skipped': summary['modules_skipped'],
        'modules_failed': summary['modules_failed'],
        'module_feed_sources': summary['module_feed_sources'],
        'pipeline_steps': summary['pipeline_steps'],
        'button_context': ui['button_context'],
        'candidates_generated': summary['candidates_generated'],
        'execution_status': summary['execution_status'],
    }, indent=2, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
