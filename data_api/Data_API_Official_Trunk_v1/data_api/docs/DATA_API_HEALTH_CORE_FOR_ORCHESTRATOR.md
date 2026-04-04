# DATA_API_HEALTH_CORE_FOR_ORCHESTRATOR

## objetivo
Entregar ao Orchestrator o núcleo mínimo de saúde dos dados para o bloco `system_status`.

## shape mínima
```json
{
  "baseline_status": "green",
  "complementary_status": "green",
  "central_health": "healthy_enriched",
  "source_mode": "project"
}
```

## regra
Este componente não deve empurrar detalhe de provider, collector, cache, storage, path ou diagnostics longos.

## leitura curta
- `baseline_status`: saúde da base principal
- `complementary_status`: disponibilidade do complemento não bloqueante
- `central_health`: leitura agregada curta do corredor de dados
- `source_mode`: modo oficial do corredor nesta fase
