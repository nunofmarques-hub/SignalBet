from pathlib import Path

base = Path(__file__).resolve().parents[1]
required = [
    'README.md','manifest.json','run_smoke.sh','run_smoke.bat','pack_check_report.txt',
    'src/index.html','src/styles/main.css','src/assets/logo-signalbet-radar-focus.svg',
    'src/js/app.js','src/js/core/store.js',
    'src/js/providers/contractMockProvider.js','src/js/providers/orchestratorMockProvider.js','src/js/providers/providerRegistry.js',
    'src/js/adapters/contractAdapters.js','src/js/adapters/orchestratorAdapters.js',
    'src/js/services/uiDataService.js',
    'docs/arquitetura_ui_v8.md','contracts/ui_contract_notes.md','examples/sample_input.json','examples/sample_output.json'
]
missing = [p for p in required if not (base / p).exists()]
assert not missing, f'Missing required files: {missing}'
print('structure_ok')
