# v12 — Linha Final Oficial

## objetivo do pack
Congelar a linha final oficial da v12 para promoção de `fechada em staging forte` para `pronto_para_integracao`, sem reabrir o módulo.

## estado do pack
pronto_para_integracao

## dependências
- Python 3.11+
- `data_api.services.fixtures_service.get_fixtures_by_league_season`
- `data_api.services.standings_service.get_standings_snapshot`
- `data_api.services.statistics_service.get_team_statistics`
- `data_api.services.statistics_service.get_fixture_statistics`

## ponto de entrada
- `motor/smoke_test.py`

## ponto de saída
- `examples/smoke_output_team_over_15.json`
- `examples/smoke_output_match_over_15.json`
- `examples/smoke_output_match_under_35.json`
- `examples/smoke_output_pool.ndjson`
- `examples/smoke_summary.json`

## referência ao contrato v1.1
O output formal do módulo é `market_pick.v1.1`.

## cenário live usado
- trunk físico montado
- imports reais do trunk: OK
- smoke básico: GREEN
- smoke live: GREEN

## provider oficial usado
- `PROVIDER_NAME = Data_API_Official_Trunk_v1`
- `PROVIDER_SOURCE = official_default`

## outputs gerados com sucesso
- `OUTPUTS_GENERATED = 3`

## leitura da Data/API Layer
A v12 lê preferencialmente do `Data_API_Official_Trunk_v1` via serviços oficiais.
O fallback local existe apenas como `diagnostic_only`, nunca como caminho preferencial.

## nota de fecho
A v12 fica promovida para `pronto_para_integracao`, mantendo a linha final oficial como única linha ativa do módulo.
