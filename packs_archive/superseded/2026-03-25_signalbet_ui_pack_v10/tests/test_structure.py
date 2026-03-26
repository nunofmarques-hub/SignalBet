from pathlib import Path
root = Path(__file__).resolve().parents[1]
required = [
    root/'README.md', root/'manifest.json', root/'run_smoke.sh', root/'run_smoke.bat', root/'pack_check_report.txt',
    root/'src/index.html', root/'src/styles/main.css', root/'src/assets/logo-signalbet-radar-focus.svg',
    root/'src/js/providers/providerRegistry.js', root/'src/js/services/systemSnapshotService.js', root/'src/js/services/pipelineStatusService.js',
    root/'src/js/viewmodels/homeViewModel.js', root/'src/js/pages/home.js'
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit('Missing files: ' + ', '.join(missing))
print('UI v10 structure OK')
