# MEMORIA_OPERACIONAL_ATIVA_V12
## SignalBet / modules / v12

**estado atual:** fecho residual curto de runtime sobre `league_id` fechado nesta linha limpa de troca integral

## leitura curta
- erro bruto `KeyError: 'league'` eliminado
- adapter endurecido
- derivação de `league_id` fechada por múltiplas origens semânticas
- `hard_fail` mantido apenas para ausência real do campo após normalização
- módulo pronto para rerun isolado via `motor/smoke_test.py`

## próximo passo
1. trocar a pasta atual por esta linha limpa
2. correr `python motor/smoke_test.py`
3. se passar, voltar ao shadow run ponta a ponta
