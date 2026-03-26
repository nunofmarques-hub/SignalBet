# Real provider wiring note

## Objetivo
Ligar a v12 a um provider real da Data/API Layer central sem depender de lógica sandbox/local.

## Ponto de entrada esperado
O provider deve devolver um payload com o shape descrito em `schemas/input_shape_provider_real.json`.

## Ligação mínima
- provider devolve payload por `fixture_id`
- `provider_bridge.py` recebe esse payload
- `input_adapter.py` valida e adapta
- `smoke_test.py` chama motores e emite payload v1.1

## Critério de passagem
Considera-se fluxo mínimo real provado quando:
- o provider responde
- o adapter não falha
- o smoke test gera 3 outputs em `market_pick.v1.1`
- os campos obrigatórios mantêm estabilidade
