# Semântica de Degradação — Under/Over Jogo

## ready
Aplica-se quando:
- existe shape protegida mínima completa
- existem campos críticos do `protected_match_context`
- existem odds disponíveis

A frente pode emitir:
- score
- probabilidade
- fair_odds
- edge
- candidate_status

## degraded_run
Aplica-se quando:
- a shape protegida mínima existe
- os campos críticos existem
- faltam odds

A frente pode continuar a emitir:
- score
- probabilidade
- fair_odds
- candidate_status
mas deve deixar:
- `market_odds = null`
- `edge = null`

## hard_fail
Aplica-se quando:
- faltam campos críticos do input protegido
- falta bloco necessário para correr
- não existe base mínima para construir `lambda_match`

Neste caso:
- não deve tentar produzir output “como se estivesse íntegra”
- deve devolver `runtime_state = hard_fail`
- deve listar `missing_fields`
