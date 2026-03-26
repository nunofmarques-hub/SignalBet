# HANDOFF_CARDS

## Estado
- estado_pack: staging
- leitura_do_tronco: interface_validada
- smoke_test: green

## Fonte oficial
`Data_API_Official_Trunk_v1`

## Ponto de consumo oficial
O Cards lê da Data/API Layer via:

- `data_api.services.fixtures_service.get_fixtures_by_league_season()`
- `data_api.services.events_service.get_fixture_events()`

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

## Estado já provado
Smoke test Cards: GREEN

### O que já foi validado
- interface oficial de fixtures lida via serviço oficial
- interface oficial de events lida via serviço oficial
- card events simples identificados
- output contratual validado

## Nota honesta
Neste ambiente o tronco físico `data_api/` não está montado, por isso o smoke test valida a interface oficial com doubles dos serviços do trunk. A leitura contra o tronco físico real fica pronta assim que esse pack estiver presente no mesmo ambiente.
