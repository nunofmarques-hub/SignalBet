# Cards — linha viva oficial

## objetivo do pack
Substituição integral limpa da linha viva do módulo Cards, pronta para ocupar a pasta oficial do módulo sem histórico misturado, sem subpastas redundantes e sem ruído técnico.

## estado do pack
integrado

## dependências
- Python 3.11+
- contrato de integração SignalBet v1.1
- quando aplicável, `data_api/` com o trunk oficial disponível para `--mode live`

## ponto de entrada
- runner oficial: `run_smoke.py`
- `run_demo.py` existe apenas como utilitário local, não como runner oficial do corredor

## ponto de saída
- `latest.json`
- stdout do smoke/live runner
- `pack_check_report.txt`

## referência ao contrato v1.1
O output do módulo segue `market_pick.v1.1` e o feed curto para app phase 1 está estabilizado em `latest.json`.

## como lê da Data/API Layer
Fonte única oficial:
- provider: `providers/official_live_provider.py`
- trunk: `Data_API_Official_Trunk_v1`
- serviços consumidos:
  - `data_api.services.fixtures_service.get_fixtures_by_league_season`
  - `data_api.services.events_service.get_fixture_events`

## estrutura viva incluída
- `providers/`
- `src/cards_module/`
- `contracts/`
- `docs/`
- `tests/`
- `run_smoke.py`
- `run_demo.py`
- `bootstrap_runtime.py`
- `latest.json`
- `manifest.json`
- `pack_check_report.txt`
