# Execution / Bankroll Alignment Note

## leitura prática
Depois de cruzar os packs mais recentes do GPS e da Banca, a Execution deixa de estar bloqueada por teoria e passa a estar bloqueada apenas por formato final de handoff.

## ponto forte
A Banca já tem material suficiente para abastecer a Execution.

## ponto fraco
A informação está partida em dois objetos:
1. `bankroll_response_batch.v1.8`
2. `execution_intake_candidate.v1.8`

## impacto na Execution
Se a Execution consumir só o `execution_intake_candidate.v1.8`, perde ligação direta a:
- `decision_id`
- `module_origin`
- `selector_run_id`
- `portfolio_group`
- `decision_timestamp`

## recomendação
Fechar a fronteira Banca -> Execution com um único payload enriquecido, sem inventar novos significados, apenas consolidando campos já existentes no output da Banca.

## consequência
Com esse payload unificado, a Execution passa a conseguir:
- intake real
- criação de `execution_id`
- reconciliação por `decision_id`
- rastreabilidade GPS run -> bank batch -> execution order
- ledger mais forte
- output analytics consistente
