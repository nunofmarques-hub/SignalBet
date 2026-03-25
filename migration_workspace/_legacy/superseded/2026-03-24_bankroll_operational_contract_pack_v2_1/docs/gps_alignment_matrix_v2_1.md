# GPS alignment matrix v2.1

| Campo GPS | Uso na banca | Observação |
|---|---|---|
| global_score | sizing | não reavaliado pela banca |
| confidence_norm | sizing | ajuste positivo/negativo |
| risk_norm | reductions | pode gerar `REDUCE_HIGH_RISK` |
| edge_norm | sizing | bucket de edge oficial |
| priority_tier | stake_base | classe operacional |
| pool_status | gate de entrada | deve ser `exported_to_bankroll` |
| conflict_flags | prudência | apoio a bloqueio futuro |
| correlation_flags | prudência | pode gerar `REDUCE_PARTIAL_CORRELATION` |
