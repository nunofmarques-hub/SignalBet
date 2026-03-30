# Data/API health core contract

Componente mínimo entregue ao Orchestrator:

```json
{
  "baseline_status": "green",
  "complementary_status": "green",
  "central_health": "healthy_enriched",
  "source_mode": "project"
}
```

Uso esperado: integrar este bloco em `system_status` sem expor detalhe técnico interno.
