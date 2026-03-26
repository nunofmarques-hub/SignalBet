# Intake Validation Notes

## Regras mínimas testadas
- `source_system` tem de ser `BANKROLL_RISK_MANAGER`
- `decision_status` tem de ser `APPROVED` ou `APPROVED_REDUCED` quando a stake aprovada continuar > 0
- `approved_odds_reference` é obrigatório para auditabilidade operacional forte
- `stake_approved` tem de ser maior que zero
- `execution_order` tem de ser inteiro >= 1
