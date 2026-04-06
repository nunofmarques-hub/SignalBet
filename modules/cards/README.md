# Cards — Clean Replacement Active Line

## objetivo do pack
Substituição integral limpa da linha viva do módulo Cards, já alinhada com as últimas decisões do projeto: linha integrada, runner oficial fixado, `game_card` final fechado para app phase 1 e feed oficial pronto para o Orchestrator.

## estado do pack
integrado

## o que este pack substitui
- linhas intermédias de staging/polimento/live-ready já absorvidas
- ruído estrutural, caches e artefactos transitórios
- versões da linha viva anteriores a esta consolidação limpa

## o que passa a ser a linha ativa
- esta pasta `cards/`
- runner oficial: `run_smoke.py`
- feed ativo: `latest.json`
- provider oficial: `providers/official_live_provider.py`

## o que sai da pasta viva
- histórico misturado
- caches, `.pyc` e artefactos transitórios
- notas redundantes já absorvidas
- outputs locais sem papel na linha ativa

## dependências
- Python 3.11+
- estrutura do projeto com `data_api/`
- `Data_API_Official_Trunk_v1` montado no ambiente para `--mode live`
- contrato de integração SignalBet v1.1

## ponto de entrada
- runner oficial: `run_smoke.py`
- demo/local: `run_demo.py`

## ponto de saída
- stdout do runner oficial
- `latest.json`
- `pack_check_report.txt`

## referência ao contrato v1.1
O output do módulo segue `market_pick.v1.1` e o feed curto segue `module_feed.v1` para `integration_feeds/cards/latest.json`.

## como lê da Data/API Layer
Fonte única oficial:
- trunk: `Data_API_Official_Trunk_v1`
- provider: `providers/official_live_provider.py`
- serviços consumidos:
  - `data_api.services.fixtures_service.get_fixtures_by_league_season`
  - `data_api.services.events_service.get_fixture_events`

## papel atual na app phase 1
Fornecedor de `game_cards` curtos, comparáveis e estáveis para o Orchestrator.
