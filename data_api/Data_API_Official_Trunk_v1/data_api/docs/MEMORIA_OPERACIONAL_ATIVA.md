# Memória Operacional Ativa — Data/API Layer

## Frente
Correção de cobertura física do trunk para desbloqueio da calibração real.

## Bloqueio identificado
O catálogo oficial `fixtures_catalog_status_FT_AET_PEN.json` expunha apenas 1 fixture, apesar de existirem múltiplos ficheiros físicos em `events/` e `statistics/` para o mesmo cenário.

## Fixtures em falta / estado observado
- `1208501`: existia em storage e estava ausente do catálogo.
- `1208600`: ausente do storage fornecido.
- `1208702`: ausente do storage fornecido.

## Ação tomada
- Regenerado o catálogo oficial com base nos fixtures fisicamente presentes em `events/` + `statistics/`.
- Atualizado `fixture_ids.json` para refletir os fixtures realmente suportados pelo catálogo regenerado.
- Emitido `coverage_fix_report.json` com o antes/depois da cobertura.

## Estado do catálogo
- Antes: 1 fixture no catálogo oficial.
- Depois: 10 fixtures no catálogo oficial.

## Próximo rerun previsto
Executar novamente `real_data_calibration_reliability_phase_v1_1_3` sobre este trunk corrigido.

## Nota
`1208600` e `1208702` continuam pendentes de backfill físico, porque não existem no storage incluído neste trunk. O bloqueio de calibração, no entanto, fica operacionalmente desbloqueado pela regeneração do catálogo já suportado por storage real.
