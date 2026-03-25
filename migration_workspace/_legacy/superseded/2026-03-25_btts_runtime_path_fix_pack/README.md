# README.md

## objetivo do pack
Aplicar o ajuste final de runtime path do módulo BTTS, mantendo o `direct_official_trunk_provider` como via principal e corrigindo a resolução do `fallback_path` relativamente à raiz real do pack.

## estado do pack
staging

## dependências
- Python 3.11+
- `Data_API_Official_Trunk_v1`
- Contrato transversal `market_pick.v1.1`

## ponto de entrada
`src/btts/run_minimal_flow.py`

## ponto de saída
`sample_output/market_pick_v1_1_btts.json`

## referência ao contrato v1.1
O output do módulo sai em `market_pick.v1.1` para a Opportunity Pool.

## mudança principal deste pack
- `run_minimal_flow.py` passa a resolver `pack_root` corretamente
- `direct_official_trunk_provider.py` endurece a resolução do fallback relativamente à raiz real do pack

## destino final pretendido
`modules/btts/`
