# UI Contract Notes

## Ponte v12
A UI continua em staging e não faz consumo live do Orchestrator nem do trunk. Nesta ronda:
- snapshots mockados aproximam-se do formato real esperado
- adapters consolidam normalização do runtime
- view models recebem dados já tratados
- páginas mantêm desacoplamento da fonte

## Campos de runtime usados no painel “Pôr tudo a correr”
- cta_state
- readiness_level
- project_feed_coverage_ratio
- pipeline_state
- current_stage
- final_result
- summary
- module_overview
- pipeline_steps
- issues

## Modo de fonte
- `contract_mock`
- `orchestrator_mock`
- `placeholder_live`
