from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from app_orch.launcher.run_val import run_validation_pipeline
from app_orch.util.io import read_json

def test_smoke_runs():
    req = read_json(ROOT / 'examples' / 'req' / 'sample.json')
    summary, ui = run_validation_pipeline(req, ROOT)
    assert 'run_id' in summary
    assert 'cta_state' in ui
