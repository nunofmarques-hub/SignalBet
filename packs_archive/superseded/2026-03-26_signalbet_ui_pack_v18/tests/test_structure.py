import os
required = [
    'README.md',
    'manifest.json',
    'src/index.html',
    'src/js/services/runtimeBridgeService.js',
    'src/js/providers/realOrchestratorProtectedProvider.js',
    'docs/arquitetura_ui_v18.md',
    'docs/ui_snapshot_freshness_policy.md',
    'docs/ui_snapshot_invalidation_rules.md',
    'docs/ui_real_vs_reused_read_boundary.md',
]
base = os.path.dirname(os.path.dirname(__file__))
missing = [p for p in required if not os.path.exists(os.path.join(base, p))]
if missing:
    raise SystemExit('MISSING: ' + ', '.join(missing))
print('TEST_STRUCTURE_OK_UI_V18')
