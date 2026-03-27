# Ordem operacional — aumento de cobertura do trunk

## Objetivo
Aumentar a cobertura física do serviço oficial `get_fixtures_by_league_season()`.

## O que fazer
1. Ler `fixture_ids.json` do cenário alvo.
2. Comparar com:
   - `fixtures_catalog_status_*.json`
   - `events/fixture_*.json`
   - `statistics/fixture_*.json`
3. Identificar:
   - ids esperados mas ausentes no catálogo
   - ids presentes em `events/` e `statistics/`
   - ids totalmente ausentes do storage
4. Corrigir o trunk por esta ordem:
   - backfill dos fixtures metadata em falta
   - regeneração do catálogo oficial
   - rerun da calibração

## O que não fazer
- não mudar provider
- não mudar trunk
- não mudar consumidor
- não criar fallback paralelo permanente na calibração

## Critério de fecho
A frente fica desbloqueada quando o catálogo oficial do cenário alvo devolver mais do que 1 fixture.
