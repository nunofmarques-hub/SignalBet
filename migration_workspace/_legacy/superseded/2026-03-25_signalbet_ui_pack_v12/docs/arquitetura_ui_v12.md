# Arquitetura UI v12

## Objetivo
Consolidar a bridge controlada entre a UI e o snapshot real esperado do Orchestrator.

## Camadas
- providers: origem dos snapshots
- adapters: normalização e defesa contra faltas
- services: snapshots e pipeline status consumíveis pela UI
- view models: shape final para cada ecrã
- components/pages: renderização desacoplada

## Novidades desta ronda
- `runtimeBridgeService.js` centraliza seleção de fonte e fallback
- `orchestratorAdapters.js` reforçado para normalizar:
  - summary
  - module_overview
  - pipeline_steps
  - cta_context
- mock snapshots mais próximos do formato esperado
- painel do Orchestrator mais fiel ao runtime provado

## Regra desta ronda
Sem ligação live fingida. Estrutura pronta para troca futura via provider controlado.
