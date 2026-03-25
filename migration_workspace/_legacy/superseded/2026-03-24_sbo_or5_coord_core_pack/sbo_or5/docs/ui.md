# Integração conceptual com UI

A UI mostra o botão principal e um painel de estado. A UI não decide readiness nem ordem do pipeline; apenas chama o Orchestrator e representa o retorno.

Campos mínimos para UI:
- `screen_status`
- `run_id`
- `system_health`
- `data_api_health`
- `module_overview`
- `last_run_summary`
- `candidates_generated`
- `cta_state`
