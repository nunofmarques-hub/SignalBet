# HANDOFF_CARDS

## Estado
- estado_pack: staging
- target_state: pronto_para_integracao
- leitura_do_tronco: interface validada
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
- preparar shortlist/candidate

## Regra operacional
O módulo Cards não deve depender de leitura direta da API externa para o fluxo mínimo, se os eventos já existirem no trunk.
