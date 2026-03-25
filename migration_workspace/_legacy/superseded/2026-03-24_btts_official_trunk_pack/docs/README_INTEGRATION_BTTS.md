# README de Integração BTTS

## provider oficial usado
`src/btts/providers/official_trunk_provider.py`

## loader oficial usado
`src/btts/loaders/official_trunk_loader.py`

## fonte oficial
`Data_API_Official_Trunk_v1`

## input esperado vindo do tronco
- fixtures da liga/época
- standings snapshot
- events por fixture
- team statistics por equipa

## fluxo
Provider -> Loader -> Engine -> Exporter -> `market_pick.v1.1`

## output oficial do módulo
`sample_output/market_pick_v1_1_btts.json`
