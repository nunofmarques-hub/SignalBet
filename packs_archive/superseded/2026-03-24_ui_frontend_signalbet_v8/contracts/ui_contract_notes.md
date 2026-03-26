# UI Contract Notes — v8

## Núcleo comum refletido pela UI
- global_score
- confidence_norm
- edge_norm
- risk_norm
- priority_tier
- eligibility
- decision_status
- execution_status
- data_quality_flag

## Estados do orchestrator refletidos no painel visual
- idle
- running
- partial
- success
- error

## Notas de integração
A v8 já separa os estados de corrida do restante contrato visual da app.
Isto permite substituir `orchestratorMockProvider` por uma fonte real com menor impacto nas páginas.

## Regra
Qualquer novo campo que ainda não pertença ao contrato ou a um output estabilizado do Orchestrator deve ser marcado como mock/placeholder antes de ser promovido a estrutural.
