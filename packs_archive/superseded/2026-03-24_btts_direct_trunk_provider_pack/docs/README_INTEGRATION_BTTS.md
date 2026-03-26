# README de Integração BTTS

## provider oficial
`src/btts/providers/direct_official_trunk_provider.py`

## loader oficial
`src/btts/loaders/official_trunk_loader.py`

## fonte oficial
`Data_API_Official_Trunk_v1`

## input esperado vindo do tronco
- fixtures da liga/época
- events por fixture
- team statistics por equipa
- standings da liga/época

## output oficial do módulo
`sample_output/market_pick_v1_1_btts.json`

## execução mínima
```bash
python -m src.btts.run_minimal_flow
```
