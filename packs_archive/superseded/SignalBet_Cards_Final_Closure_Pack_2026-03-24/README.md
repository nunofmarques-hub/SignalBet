# Cards Final Closure Pack

## objetivo do pack
Fechar o módulo Cards como pack final de staging forte orientado a pronto_para_integracao, com consumo oficial do Data_API_Official_Trunk_v1 via provider único, pipeline curto, output contratual estável e runners preparados para live real.

## estado do pack
staging

## target_state
pronto_para_integracao

## dependências
- Python 3.11+
- Estrutura do projeto com `data_api/`
- Data_API_Official_Trunk_v1 fisicamente montado no ambiente
- Contrato de integração SignalBet v1.1

## ponto de entrada
- `run_demo.py`
- `run_smoke.py`

## ponto de saída
- `out/*.json`
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

## objeto consumido
- `fixtures_by_league_season`
- `fixture_events`

## o que falta para fecho final
Correr `python run_smoke.py --mode live --league 140 --season 2024` com o trunk físico montado no mesmo ambiente.

## estado operacional honesto
O pack está pronto para esse passo final, mas neste ambiente não foi possível provar o live real porque o `data_api/` físico não está presente.
