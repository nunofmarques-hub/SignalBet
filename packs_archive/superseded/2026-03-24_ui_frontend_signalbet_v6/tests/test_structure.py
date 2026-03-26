from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    'README.md',
    'manifest.json',
    'src/index.html',
    'src/assets/logo-signalbet-radar-focus.svg',
    'src/styles/main.css',
    'src/js/app.js',
    'src/data/mock-data.js',
    'docs/arquitetura_ui_v6.md',
    'contracts/ui_contract_notes.md',
    'examples/sample_input.json',
    'examples/sample_output.json',
]


def test_required_files_present():
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    assert not missing, f"Missing: {missing}"
