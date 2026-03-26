# Cards — Trunk Live Handoff Pack

## objetivo do pack
Provar que o módulo Cards já não depende de mirror local e que lê o provider oficial do `Data_API_Official_Trunk_v1` via serviços oficiais da Data/API Layer, com pipeline curto e output contratual estável.

## estado do pack
staging

## dependências
- Python 3.11+
- `pytest` para smoke tests
- tronco oficial disponível em `data_api/` no `PYTHONPATH`
- serviços oficiais:
  - `data_api.services.fixtures_service.get_fixtures_by_league_season`
  - `data_api.services.events_service.get_fixture_events`

## ponto de entrada
- `run_cards_trunk_live_demo.py`

## ponto de saída
- `out/*.json`

## referência ao contrato v1.1
- `market_pick.v1.1`
- Módulo de mercado -> Opportunity Pool

## leitura da Data/API Layer
Leitura oficial via:
- `data_api.services.fixtures_service.get_fixtures_by_league_season(league_id, season)`
- `data_api.services.events_service.get_fixture_events(fixture_id, league_id, season)`

O pack **não** usa espelho local de staging. Quando o tronco oficial não estiver fisicamente presente, o demo falha de forma explícita. Os testes curtos usam doubles dos serviços oficiais apenas para validar o handoff da interface.

## ficheiros principais
- `providers/official_live_provider.py`
- `providers/contracts.py`
- `providers/mappers.py`
- `src/cards_module/core/orchestrator.py`
- `src/cards_module/core/eligibility.py`
- `tests/test_short_pipeline.py`
- `docs/HANDOFF_CARDS.md`

## destino final pretendido
`modules/cards/`
