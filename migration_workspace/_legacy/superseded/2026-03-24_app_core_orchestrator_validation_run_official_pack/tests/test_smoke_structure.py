
from pathlib import Path

def test_required_files_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / 'README.md').exists()
    assert (root / 'manifest.json').exists()
    assert (root / 'run_smoke.py').exists()
