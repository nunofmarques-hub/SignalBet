# GPS vs Banca vs Execution — Crosswalk Operacional

## conclusão rápida
O handoff GPS -> Banca está coerente.
O bloqueio real está agora na passagem Banca -> Execution.

## o que já está bem fechado
- o GPS entrega `selector_run_id`, `normalization_version` e picks comparáveis
- a Banca consome esse batch e devolve `bankroll_response_batch.v1.8`
- a Banca também produz `execution_intake_candidate.v1.8` para picks `APPROVED` e `APPROVED_REDUCED`

## o que falta para a Execution
O payload `execution_intake_candidate.v1.8` da Banca ainda não traz, por si só, todos os campos que a Execution precisa para:
- auditabilidade forte
- reconciliação completa com a decisão financeira
- rastreabilidade batch -> decision -> execution

## campos já presentes no execution_intake_candidate.v1.8
- `execution_intake_schema_version`
- `source_batch_id`
- `intake_timestamp`
- `pick_id`
- `event_id`
- `match_label`
- `market_family`
- `market`
- `selection`
- `line`
- `odds_snapshot`
- `global_score`
- `priority_tier`
- `decision_status`
- `stake_approved`
- `stake_pct_bankroll`
- `execution_order`
- `approved_odds_window`
- `rules_triggered`
- `execution_note`

## campos que continuam a faltar para a Execution como ledger forte
- `decision_id`
- `module_origin`
- `selector_run_id`
- `decision_timestamp`
- `portfolio_group`
- `bankroll_note`
- `source_system`

## observação importante
Esses campos não desapareceram: eles existem no `bankroll_response_batch.v1.8`.
O problema é que a Banca os separou do payload de intake.

## recomendação operacional
Congelar para a Execution um payload de intake real enriquecido, derivado da Banca, que una:
- identidade operacional do `execution_intake_candidate.v1.8`
- identidade decisional do `bankroll_response_batch.v1.8`

## decisão recomendada
A Execution deve trabalhar em cima de um handoff real único vindo da Banca, aqui proposto como:
- `execution_intake_real.v1`

Este handoff não recalcula nada.
Apenas junta os campos mínimos já decididos pela Banca num único payload estável para intake da Execution.
