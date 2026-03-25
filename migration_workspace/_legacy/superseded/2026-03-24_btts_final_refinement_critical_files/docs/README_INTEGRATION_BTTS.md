# README_INTEGRATION_BTTS

## provider principal
`src/btts/providers/direct_official_trunk_provider.py`

## loader oficial
`src/btts/loaders/official_trunk_loader.py`

## execução mínima
`python -m src.btts.run_minimal_flow`

## comportamento esperado
1. tenta primeiro a via oficial do tronco
2. só usa fallback se os serviços do tronco não estiverem acessíveis
3. gera output final em `market_pick.v1.1`
