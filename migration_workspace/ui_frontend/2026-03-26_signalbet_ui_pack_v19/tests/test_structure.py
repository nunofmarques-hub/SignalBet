import os
required = [
    'README.md',
    'manifest.json',
    'src/index.html',
    'src/js/services/runtimeBridgeService.js',
    'src/js/providers/realOrchestratorProtectedProvider.js',
    'docs/arquitetura_ui_v19.md',
    'docs/ui_reuse_decision_policy.md',
    'docs/ui_refresh_control_flow.md',
    'docs/ui_repeated_read_scenarios.md',
]
base = os.path.dirname(os.path.dirname(__file__))
missing = [p for p in required if not os.path.exists(os.path.join(base, p))]
if missing:
    raise SystemExit('MISSING: ' + ', '.join(missing))
print('TEST_STRUCTURE_OK_UI_V19')
