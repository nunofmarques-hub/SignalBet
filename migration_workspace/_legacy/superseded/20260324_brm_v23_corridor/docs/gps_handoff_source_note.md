# GPS -> Banca Handoff v1

## missão
O Global Pick Selector entrega à Banca uma shortlist já:
- validada
- normalizada
- comparada
- ordenada
- sinalizada com flags de conflito e correlação

## o que a Banca recebe
A Banca recebe um lote de picks em linguagem comparável do sistema, já com:
- `global_score`
- `confidence_norm`
- `risk_norm`
- `edge_norm`
- `priority_tier`
- `conflict_flags`
- `correlation_flags`
- racional executivo
- nota do seletor

## o que a Banca faz
A Banca não recalcula o mercado.
A Banca decide:
- admissibilidade
- stake
- cortes
- bloqueios
- exposição
- prioridade operacional final

## regra prática
O GPS fecha a linguagem comparável.
A Banca fecha a linguagem financeira e operacional.
