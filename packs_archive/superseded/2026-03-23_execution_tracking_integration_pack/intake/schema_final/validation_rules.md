# Intake — Regras finais v1

## Validações obrigatórias
1. `source_system` tem de ser `BANKROLL_RISK_MANAGER`
2. `decision_status` tem de ser `APPROVED`
3. `stake_approved > 0`
4. `stake_pct_bankroll > 0`
5. `approved_odds_reference > 1.00`
6. `execution_order >= 1`
7. `rules_triggered` deve existir, mesmo que venha vazio
8. `decision_timestamp` deve ser datetime ISO válido

## Deduplicação recomendada
Tratar como duplicado se existir ordem aberta com a mesma combinação:
- `decision_id`
- `pick_id`
- `event_id`
- `market`
- `selection`

## Reason codes principais na fronteira de intake
- `INVALID_SCHEMA`
- `MISSING_REQUIRED_FIELD`
- `INVALID_SOURCE`
- `INVALID_DECISION_STATUS`
- `DUPLICATE_ORDER`
- `DATA_MISMATCH`
