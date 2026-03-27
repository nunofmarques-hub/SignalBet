# HANDOFF_CARDS

## Estado
- estado_pack: staging
- target_state: pronto_para_integracao
- leitura_do_tronco: interface validada
- smoke_test: green

## Fonte oficial
`Data_API_Official_Trunk_v1`

## Provider oficial
`providers/official_live_provider.py`

## Ponto de consumo oficial
O Cards lê da Data/API Layer via:
- `data_api.services.fixtures_service.get_fixtures_by_league_season`
- `data_api.services.events_service.get_fixture_events`

## Objeto consumido
- fixtures por liga/época
- events por fixture
- leitura simples de card events

## Regra operacional
O módulo Cards não deve depender de leitura direta da API externa para o fluxo mínimo, se os eventos já existirem no trunk.

## Passo final
Executar `python run_smoke.py --mode live --league 140 --season 2024` com o trunk físico montado.
