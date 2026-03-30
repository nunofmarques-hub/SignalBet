# Semântica Fechada de Degradação

## ready
- input protegido completo
- odds presentes
- output final completo com edge

## degraded_run
- input protegido crítico completo
- sem odds
- output emitido sem edge, mas com score/probabilidade/fair_odds

## hard_fail
- falta campo crítico do input protegido
- não tenta emitir output normal
- devolve `missing_fields`
