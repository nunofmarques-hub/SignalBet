# Cards — Official Trunk Clean Pack

## objetivo do pack
Fechar o salto final do módulo Cards para consumo limpo do provider oficial do `Data_API_Official_Trunk_v1`, removendo artefactos de staging residuais, mantendo output estável e critérios de elegibilidade mais fechados.

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
Fonte única assumida:
- provider oficial: `data_api.services.fixtures_service.get_fixtures_by_league_season`
- provider oficial: `data_api.services.events_service.get_fixture_events`
- objeto consumido: `fixtures + fixture_events`

O pack já não usa mirror local nem inputs intermédios. Quando o tronco oficial não estiver fisicamente presente, o demo falha de forma explícita. Os smoke tests validam a interface oficial com doubles do provider.

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
