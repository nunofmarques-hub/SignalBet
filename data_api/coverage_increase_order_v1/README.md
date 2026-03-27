# coverage_increase_order_v1

Pack curto para aumentar cobertura física do trunk sem reabrir arquitetura.

## Diagnóstico já provado
- O serviço oficial `get_fixtures_by_league_season()` lê apenas o catálogo `fixtures_catalog_status_*.json`.
- No trunk atual existe apenas **1 catálogo de fixtures** para `league_140/season_2024/status=FT-AET-PEN`.
- Esse catálogo expõe **1 fixture**.
- No mesmo trunk existe `fixture_ids.json` com **4 fixture_ids** esperados para o mesmo cenário.
- Existem vários ficheiros de `events/` e `statistics/`, mas isso não aumenta a cobertura do serviço enquanto o catálogo oficial continuar curto.

## Objetivo
Aumentar a cobertura real do serviço **sem mudar provider, trunk ou consumidor**.

## Próxima ação correta
1. Auditar a discrepância entre `fixture_ids.json`, catálogo oficial e ficheiros físicos disponíveis.
2. Completar/recolher os fixtures em falta no trunk.
3. Regenerar `fixtures_catalog_status_FT_AET_PEN.json`.
4. Só depois voltar a correr a fase de calibração.

## Execução
Corre:
- `run_audit.cmd` no Windows
- ou `python src/audit_fixture_catalog_coverage.py --trunk-root <path>`
