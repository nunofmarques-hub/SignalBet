# Payload para UI

O Orchestrator continua a ser a camada técnica. A UI mostra o botão, chama a corrida e apresenta o retorno.

## Campos mais úteis
- `screen_status`
- `cta_state`
- `system_health`
- `data_api_health`
- `project_mode`
- `button_context`
- `module_overview`
- `pipeline_steps`
- `counts`
- `last_run_summary`

## Leitura esperada
A UI deve conseguir mostrar módulos elegíveis, corridos, skipped, failed, origem dos feeds, estado do pipeline e se o botão está pronto, degradado ou bloqueado.
