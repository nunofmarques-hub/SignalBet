# Data/API Layer — Integration Seed v1

## Objetivo
Consolidar Week1 e permitir integração parcial dos módulos.

## O que este pack já traz
- config central
- provider inicial (`api_football_provider.py`)
- collectors prioritários
- storage base (`raw`, `normalized`, `derived`, `state`)
- services mínimos para consumo dos módulos

## Ponto único de credenciais
- `api.env.txt` na raiz

## Collectors prioritários
- `collect_fixtures.py`
- `collect_events.py`
- `collect_fixture_statistics.py`
- `collect_team_statistics.py`
- `collect_standings.py`

## Pontos de entrada para módulos
- `get_fixtures_by_league_season()`
- `get_fixture_events()`
- `get_fixture_statistics()`
- `get_team_statistics()`
- `get_standings_snapshot()`

## Política de storage
- `storage/raw/` = payload original
- `storage/normalized/` = reservado para contratos internos estáveis
- `storage/derived/` = reservado para agregados e features
- `storage/state/` = retoma e progresso dos jobs

## Estado atual
- Integração: parcial
- Arquitetura: forte
- Execução: inicial mas já consumível
