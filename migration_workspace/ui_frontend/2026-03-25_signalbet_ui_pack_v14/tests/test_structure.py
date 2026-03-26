
from pathlib import Path
root = Path(__file__).resolve().parents[1]
required = ['README.md','manifest.json','src/index.html','src/js/services/runtimeBridgeService.js','src/js/providers/realOrchestratorProtectedProvider.js','docs/ui_runtime_read_bridge.md','examples/real_snapshot_minimal.json']
missing = [p for p in required if not (root / p).exists()]
if missing: raise SystemExit(f'Missing required files: {missing}')
print('TEST_STRUCTURE_OK_UI_V14')
