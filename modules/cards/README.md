# Cards Ready for Integration Pack

## objetivo do pack
Congelar a linha oficial do módulo Cards já pronta para integração, após confirmação de live real com o trunk físico, provider oficial único, pipeline curto validado e output contratual estabilizado.

## estado do pack
pronto_para_integracao

## target_state
pronto_para_integracao

## dependências
- Python 3.11+
- estrutura do projeto com `data_api/`
- `Data_API_Official_Trunk_v1` montado no ambiente
- contrato de integração SignalBet v1.1

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

## provider oficial
- `OfficialLiveProvider`

## objeto consumido
- `get_fixtures_by_league_season`
- `get_fixture_events`

## validação final confirmada
Resultado do live test real sobre o trunk físico:
- `TRUNK_IMPORT_OK`
- smoke básico: `OK`
- smoke live: `OK`
- `eligibility = true`
- `pick_id` gerado com sucesso

## decisão oficial
Este pack fica congelado como linha oficial do módulo Cards em estado `pronto_para_integracao`.
