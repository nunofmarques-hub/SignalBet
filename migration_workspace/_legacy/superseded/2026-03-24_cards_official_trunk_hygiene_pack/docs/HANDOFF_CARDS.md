# HANDOFF_CARDS

## Estado
- estado_pack: staging
- leitura_do_tronco: por interface oficial
- smoke_test: green

## Fonte oficial
`Data_API_Official_Trunk_v1`

## Ponto de consumo oficial
O Cards lê da Data/API Layer via:
- `get_fixtures_by_league_season()`
- `get_fixture_events()`

## Inputs mínimos esperados
- fixtures da liga/época
- events por fixture
- leitura simples de eventos de cartão

## Objetivo do consumo
Permitir ao módulo:
- identificar contexto mínimo de cartões
- validar elegibilidade base
- preparar lógica de sinal ou shortlist

## Regra operacional
O módulo Cards não deve depender de leitura direta da API externa para o fluxo mínimo, se os eventos já existirem no tronco.
