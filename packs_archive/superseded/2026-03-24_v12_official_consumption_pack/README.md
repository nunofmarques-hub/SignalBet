# v12 official consumption pack

- objetivo do pack: provar consumo oficial ativo do `Data_API_Official_Trunk_v1`, sem fallback preferencial para staging/local, com smoke test curto e output `market_pick.v1.1` estável.
- estado do pack: staging
- dependências: `data_api.services.fixtures_service`, `data_api.services.standings_service`, `data_api.services.statistics_service`
- ponto de entrada: `motor/smoke_test.py`
- ponto de saída: `examples/smoke_output_pool.ndjson` e payloads JSON v1.1 em `examples/`
- referência ao contrato v1.1: `Contrato_Transversal_Integracao_SignalBet_v1_1_Operacional.pdf`
- leitura da Data/API Layer: consumo oficial ativo do `Data_API_Official_Trunk_v1` via:
  - `get_fixtures_by_league_season()`
  - `get_standings_snapshot()`
  - `get_team_statistics()`
  - `get_fixture_statistics()`

## ficheiros principais
- `motor/provider_bridge.py`
- `motor/input_adapter.py`
- `motor/market_engines.py`
- `motor/contract_output.py`
- `motor/smoke_test.py`
- `integration/PROVIDER_USAGE.md`
- `integration/FINAL_INTEGRATION_NOTE.md`

## destino final pretendido
- integração forte em staging via Opportunity Pool / Global Pick Selector
- promoção posterior para `modules/` só após integração consolidada
