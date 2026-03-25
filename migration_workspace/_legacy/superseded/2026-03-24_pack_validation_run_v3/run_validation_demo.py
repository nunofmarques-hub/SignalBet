from __future__ import annotations

import json
from pathlib import Path
import sys

PACK_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PACK_ROOT))

from app_core.launcher.run_validation_pipeline import run_validation_pipeline


def main() -> None:
    request_path = PACK_ROOT / 'app_core' / 'samples' / 'sample_run_request.json'
    run_request = json.loads(request_path.read_text(encoding='utf-8'))
    run_request['project_root'] = str(PACK_ROOT)
    result = run_validation_pipeline(run_request)

    out_dir = PACK_ROOT / 'runtime_outputs'
    out_dir.mkdir(exist_ok=True)
    (out_dir / 'last_health_report.json').write_text(json.dumps(result['health_report'], ensure_ascii=False, indent=2), encoding='utf-8')
    (out_dir / 'last_run_summary.json').write_text(json.dumps(result['run_summary'], ensure_ascii=False, indent=2), encoding='utf-8')
    (out_dir / 'last_ui_status.json').write_text(json.dumps(result['ui_status'], ensure_ascii=False, indent=2), encoding='utf-8')

    print('VALIDATION RUN OK')
    print(json.dumps(result['run_summary'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
