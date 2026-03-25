# README.md

## objetivo do pack
Consolidar o BTTS como módulo real a consumir oficialmente a Data/API Layer através do `Data_API_Official_Trunk_v1`, substituindo a ponte de sample serializado por um provider direto do tronco e mantendo o fluxo mínimo executável com output estável em `market_pick.v1.1`.

## estado do pack
staging

## dependências
- Python 3.11+
- `Data_API_Official_Trunk_v1`
- Contrato transversal de integração SignalBet v1.1 operacional
- Serviços oficiais disponíveis no tronco:
  - `get_fixtures_by_league_season()`
  - `get_fixture_events()`
  - `get_team_statistics()`
  - `get_standings_snapshot()`

## ponto de entrada
`src/btts/run_minimal_flow.py`

## ponto de saída
`sample_output/market_pick_v1_1_btts.json`

## referência ao contrato v1.1
O output deste pack segue o envelope `market_pick.v1.1` para a Opportunity Pool.

## como lê da Data/API Layer
Lê diretamente do `Data_API_Official_Trunk_v1` através de um provider oficial do módulo BTTS.
O provider monta um `sample_input` oficial a partir de:
- fixtures da liga/época
- standings da liga/época
- events por fixture
- team statistics por equipa

## destino final pretendido
`modules/btts/`
