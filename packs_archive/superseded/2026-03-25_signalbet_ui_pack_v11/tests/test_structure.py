from pathlib import Path
base = Path(__file__).resolve().parents[1]
required = [
    'README.md','manifest.json','run_smoke.sh','run_smoke.bat','pack_check_report.txt',
    'src/index.html','src/styles/main.css','src/assets/logo-signalbet-radar-focus.svg',
    'src/js/services/systemSnapshotService.js','src/js/services/pipelineStatusService.js',
    'src/js/services/uiDataService.js','src/js/viewmodels/homeViewModel.js','docs/arquitetura_ui_v11.md'
]
missing = [p for p in required if not (base / p).exists()]
if missing:
    raise SystemExit('Missing: ' + ', '.join(missing))
print('TEST_STRUCTURE_OK')
