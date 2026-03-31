from pathlib import Path

def test_structure():
    root = Path(__file__).resolve().parents[1]
    assert (root / "src" / "index.html").exists()
    assert (root / "runtime_outputs" / "app_phase1_protected_payload.json").exists()
    assert (root / "manifest.json").exists()
