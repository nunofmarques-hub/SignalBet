# Cards Active Line — Game Card Phase 1 Pack

## objetivo do pack
Consolidar a linha ativa integrada do módulo Cards já limpa, sem ruído intermédio, com o feed oficial `integration_feeds/cards/latest.json` fechado para o bloco `game_cards` da app phase 1.

## estado do pack
integrado

## dependências
- Python 3.11+
- estrutura do projeto com `data_api/`
- `Data_API_Official_Trunk_v1` como upstream oficial
- contrato de integração SignalBet v1.1

## ponto de entrada
- runner oficial técnico: `run_smoke.py`
- demo/local: `run_demo.py`

## ponto de saída
- feed oficial: `latest.json`
- stdout do runner oficial
- `pack_check_report.txt`

## referência ao contrato v1.1
O output do módulo segue `market_pick.v1.1` e o envelope de feed segue `module_feed.v1`.

## como lê da Data/API Layer
Fonte única oficial:
- provider: `providers/official_live_provider.py`
- trunk: `Data_API_Official_Trunk_v1`
- serviços consumidos:
  - `data_api.services.fixtures_service.get_fixtures_by_league_season`
  - `data_api.services.events_service.get_fixture_events`

## handoff para o Orchestrator
Ficheiro oficial a consumir:
- `integration_feeds/cards/latest.json`

## nota curta
Esta linha substitui a ativa anterior e fica limpa para handoff do bloco `game_cards`, sem docs redundantes, sem caches e sem variantes intermédias já absorvidas.
