# HANDOFF_BTTS

## Estado
- estado_pack: staging
- leitura_do_tronco: validada
- smoke_test: green

## Fonte oficial
`Data_API_Official_Trunk_v1`

## Ponto de consumo oficial
O BTTS deve ler da Data/API Layer via:

- `get_fixtures_by_league_season()`
- `get_fixture_events()`
- `get_team_statistics()`
- `get_standings_snapshot()`

## Inputs mínimos esperados
- fixtures da liga/época
- events por fixture
- team statistics por equipa
- standings da liga/época

## Objetivo do consumo
Permitir ao BTTS alimentar:
- BOS
- BVS
- SBI
- AMI bilateral
- FGT BTTS
- TSI bilateral
- contexto competitivo base

## Regra operacional
O BTTS não deve chamar endpoints externos diretamente se o recurso já existir no tronco oficial.

## Estado já provado
Smoke test BTTS: GREEN

### O que já foi validado
- fixtures lidos do tronco
- standings lidos do tronco
- events lidos do tronco
- team_statistics lidos do tronco
