# README.md

## objetivo do pack
Consolidar o BTTS como módulo real a consumir oficialmente a Data/API Layer via `Data_API_Official_Trunk_v1`, usando provider direto do tronco como caminho principal e fallback apenas para smoke test controlado.

## estado do pack
staging

## dependências
- Python 3.11+
- `Data_API_Official_Trunk_v1`
- Contrato transversal `market_pick.v1.1`
- Serviços oficiais esperados:
  - `get_fixtures_by_league_season()`
  - `get_fixture_events()`
  - `get_team_statistics()`
  - `get_standings_snapshot()`

## ponto de entrada
`src/btts/run_minimal_flow.py`

## ponto de saída
`sample_output/market_pick_v1_1_btts.json`

## referência ao contrato v1.1
O output sai em `market_pick.v1.1` para a Opportunity Pool.

## como lê da Data/API Layer
O provider principal tenta ler diretamente do `Data_API_Official_Trunk_v1`.
O fallback serializado existe apenas para teste quando o tronco não estiver montado no ambiente.

## destino final pretendido
`modules/btts/`
