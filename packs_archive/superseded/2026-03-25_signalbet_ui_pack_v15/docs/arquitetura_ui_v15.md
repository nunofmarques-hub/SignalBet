# Arquitetura UI v15

O v15 transforma a bridge real provada no v14 em objeto formal do pack.

## Foco
- clarificar o que entra por ponte real
- clarificar o que continua mock
- explicitar limites da bridge atual
- preparar próximos passos para ampliar leitura real sem perder controlo

## Peças centrais
- `runtimeBridgeService.js`
- `orchestratorAdapters.js`
- `realOrchestratorProtectedProvider.js`
- `uiDataService.js`

## Source modes
- `contract_mock`
- `orchestrator_mock`
- `real_read_protected`
- `placeholder_live`
