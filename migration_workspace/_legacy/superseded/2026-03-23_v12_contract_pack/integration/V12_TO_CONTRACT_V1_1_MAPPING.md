# Mapeamento v12 -> Contrato v1.1 Operacional

## Campos já suportados pelo motor
- `module_id`
- `module_version`
- `event_id`
- `match_label`
- `competition`
- `market_family`
- `market`
- `selection`
- `line`
- `odds`
- `eligibility`
- `score_raw`
- `confidence_raw`
- `risk_raw`
- `edge_raw`
- `rationale_summary`
- `main_drivers`
- `penalties`

## Campos a formalizar de forma obrigatória
- `schema_version`
- `pick_id`
- `created_at`
- `data_quality_flag`
- `module_rank_internal`
- `expiry_context`
- `module_specific_payload`

## Convenções oficiais da v12
- `market_family`: `goals`
- `market`: `team_goals_over` | `match_goals_over` | `match_goals_under`
- `motor_id`: `TEAM_OVER_ENGINE` | `MATCH_OVER_ENGINE` | `MATCH_UNDER_ENGINE`
- `goal_profile`: `offensive_directed` | `offensive_global` | `conservative_under`
- `market_variant`: `TEAM_OVER_15`, `MATCH_OVER_15`, `MATCH_UNDER_35`, etc.

## Núcleo ativo atual
- `TEAM_OVER_15`
- `MATCH_OVER_15`
- `MATCH_UNDER_35`

## Expansão futura suportada estruturalmente
- linhas de `0.5` a `5.5`
- família `team_goals_over`
- família `match_goals_over`
- família `match_goals_under`
