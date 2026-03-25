# HANDOFF_BTTS

## Estado
- estado_pack: staging
- provider_oficial: direto
- fallback_serializado: apenas apoio de teste
- output_estavel: sim

## Fonte oficial
`Data_API_Official_Trunk_v1`

## Provider oficial usado
`src/btts/providers/direct_official_trunk_provider.py`

## Loader oficial usado
`src/btts/loaders/official_trunk_loader.py`

## Ponto de consumo oficial
- `get_fixtures_by_league_season()`
- `get_fixture_events()`
- `get_team_statistics()`
- `get_standings_snapshot()`

## Regra operacional
O BTTS não deve chamar endpoints externos diretamente se o recurso já existir no tronco oficial.

## Fluxo alvo
Trunk oficial -> provider direto -> loader -> engine -> exporter -> `market_pick.v1.1`
