# Arquitetura UI v11

## Ponte UI v10 -> Orchestrator real
A v11 aproxima `systemSnapshotService`, `pipelineStatusService` e `uiDataService` dos campos já esperados do runtime:
- cta_state
- readiness_level
- project_feed_coverage_ratio
- pipeline_state
- current_stage
- final_result
- summary
- module_overview
- pipeline_steps
- button_context

## Mapeamento
Os view models passam a receber snapshots já adaptados e focam-se em leitura de produto.

## Objetivo
Preparar a troca futura do `orchestratorMockProvider` por um adapter real sem reescrita pesada da UI.

## Disciplina
- sem ligação real fingida
- sem acoplamento direto das páginas aos providers
- view models continuam como superfície de produto
