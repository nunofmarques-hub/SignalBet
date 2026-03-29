# Cards Final Polish Pack

## objetivo do pack
Polimento final curto do módulo Cards sem reabrir lógica analítica, fixando `run_smoke.py` como runner oficial desta fase, endurecendo o layout de runtime/package e clarificando smoke vs demo vs corredor.

## estado do pack
staging

## target_state
pronto_para_integracao

## dependências
- Python 3.11+
- estrutura do projeto com `data_api/`
- `Data_API_Official_Trunk_v1` montado no ambiente para `--mode live`
- contrato de integração SignalBet v1.1

## ponto de entrada
- oficial desta fase: `run_smoke.py`
- demo/local: `run_demo.py`

## ponto de saída
- stdout do runner oficial
- `out/*.json` quando usado `run_demo.py`
- `pack_check_report.txt`

## referência ao contrato v1.1
O output do módulo segue `market_pick.v1.1`.

## como lê da Data/API Layer
Fonte única oficial:
- provider: `providers/official_live_provider.py`
- trunk: `Data_API_Official_Trunk_v1`
- serviços consumidos:
  - `data_api.services.fixtures_service.get_fixtures_by_league_season`
  - `data_api.services.events_service.get_fixture_events`

## provider oficial
- `OfficialLiveProvider`

## objeto consumido
- `get_fixtures_by_league_season`
- `get_fixture_events`

## nota de runtime
Nesta ronda, `run_smoke.py` é o runner oficial do módulo para confirmação técnica local/contratual. `run_demo.py` permanece apenas como demo/local e não deve ser usado como entrypoint oficial do corredor.
