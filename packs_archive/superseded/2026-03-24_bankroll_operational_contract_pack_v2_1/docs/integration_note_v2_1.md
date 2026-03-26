# Integration note v2.1

- Upstream formal da banca: Global Pick Selector
- A banca consome apenas batches em `pool_status = exported_to_bankroll`
- O output final para Execution inclui apenas candidatos com `decision_status` em `APPROVED` ou `APPROVED_REDUCED` e `execution_ready = true`
- `BLOCKED` e `RESERVE` permanecem auditáveis mas não seguem para execution
- Fixture lock mantém a regra de uma fixture comprometida por entrada aprovada
