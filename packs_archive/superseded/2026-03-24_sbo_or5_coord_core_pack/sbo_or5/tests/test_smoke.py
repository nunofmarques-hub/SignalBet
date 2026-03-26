from pathlib import Path

def test_pack_files():
    root = Path(__file__).resolve().parents[1]
    assert (root / 'README.md').exists()
    assert (root / 'manifest.json').exists()
    assert (root / 'run_smoke.py').exists()
