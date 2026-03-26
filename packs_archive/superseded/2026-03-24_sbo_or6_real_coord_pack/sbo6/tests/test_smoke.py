from pathlib import Path
import sys
PACK_ROOT = Path(__file__).resolve().parents[1]
SRC = PACK_ROOT / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
from app_orch.launcher.run_val import run_validation_pipeline

def test_smoke_validation_run():
    result = run_validation_pipeline({'run_profile':'validation_run'}, PACK_ROOT)
    summary = result['run_summary']
    assert summary['official_trunk_status'] in {'PASS','WARN'}
    assert 'v12' in summary['modules_eligible']
