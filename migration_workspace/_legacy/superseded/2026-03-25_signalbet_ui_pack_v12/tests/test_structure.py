from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md',
    'manifest.json',
    'pack_check_report.txt',
    'src/index.html',
    'src/js/providers/providerRegistry.js',
    'src/js/adapters/orchestratorAdapters.js',
    'src/js/services/systemSnapshotService.js',
    'src/js/services/pipelineStatusService.js',
    'src/js/services/runtimeBridgeService.js',
]

for rel in REQUIRED:
    path = ROOT / rel
    assert path.exists(), f'Missing {rel}'
