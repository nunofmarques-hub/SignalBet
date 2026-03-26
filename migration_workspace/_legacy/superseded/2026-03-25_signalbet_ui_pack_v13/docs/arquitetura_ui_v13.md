# Arquitetura UI v13

## Objetivo
Consolidar a ponte controlada entre a UI e o runtime esperado do Orchestrator, mantendo staging honesto.

## Pontos-chave
- `orchestratorAdapters.js` continua central na normalização
- `runtimeBridgeService.js` endurece source selection e fallback
- `placeholder_live` representa ponto de entrada protegido para futura leitura real parcial
- páginas consomem bundles vindos de services/view models e não dados crus
