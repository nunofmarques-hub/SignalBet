# data_api_health_core_to_orchestrator_v1

Pack curto da Data/API Layer para entregar ao Orchestrator o núcleo mínimo de saúde dos dados.

## Objetivo
Produzir um componente limpo e curto para `system_status`, limitado a:
- `baseline_status`
- `complementary_status`
- `central_health`
- `source_mode`

## Regra desta fase
Não empurra:
- providers
- collectors
- cache
- dumps
- detalhe técnico de infra

## Como correr
### Windows
`run_extract_data_api_health.cmd`

### Linux/macOS
`sh run_extract_data_api_health.sh`

## Output esperado
- `examples/data_api_health_component_generated.json`
- `logs/data_api_health_summary_generated.json`

## Origem
Trunk oficial da Data/API Layer.

## Destino
Orchestrator / App Core.
