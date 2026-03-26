from pathlib import Path
root = Path(__file__).resolve().parents[1]
required = [
    'README.md','manifest.json','src/index.html','src/js/services/runtimeBridgeService.js',
    'src/js/providers/realOrchestratorProtectedProvider.js','docs/ui_real_bridge_scope.md',
    'docs/ui_mock_scope.md','docs/ui_bridge_limits.md','docs/ui_real_read_expansion_plan.md'
]
missing = [p for p in required if not (root / p).exists()]
if missing:
    raise SystemExit('MISSING:' + ','.join(missing))
print('TEST_STRUCTURE_OK_UI_V15')
