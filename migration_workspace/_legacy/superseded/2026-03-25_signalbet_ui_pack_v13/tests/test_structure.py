from pathlib import Path
root = Path(__file__).resolve().parents[1]
required = [
    'README.md','manifest.json','run_smoke.sh','run_smoke.bat','pack_check_report.txt',
    'src/index.html','src/styles/main.css','src/assets/logo-signalbet-radar-focus.svg',
    'src/js/providers/providerRegistry.js','src/js/adapters/orchestratorAdapters.js',
    'src/js/services/runtimeBridgeService.js','docs/ui_runtime_read_bridge.md'
]
missing = [p for p in required if not (root / p).exists()]
if missing:
    raise SystemExit('Missing: ' + ', '.join(missing))
print('STRUCTURE_OK')
