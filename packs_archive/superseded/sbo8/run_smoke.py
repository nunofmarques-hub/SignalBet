from __future__ import annotations
from pathlib import Path
import sys, json

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'src'))

from app_orch.launcher.run_val import run_validation_pipeline
from app_orch.util.io import read_json

if __name__ == '__main__':
    req = read_json(ROOT / 'examples' / 'req' / 'sample.json')
    summary, ui = run_validation_pipeline(req, ROOT)
    print(json.dumps({
        'run_id': summary['run_id'],
        'project_mode': summary['project_mode'],
        'run_mode': summary['run_mode'],
        'modules_run': summary['modules_run'],
        'modules_failed': summary['modules_failed'],
        'module_feed_stats': summary['module_feed_stats'],
        'project_feed_coverage_ratio': summary['project_feed_coverage_ratio'],
        'final_summary': summary['final_summary'],
        'cta_state': ui['cta_state']
    }, indent=2, ensure_ascii=False))
