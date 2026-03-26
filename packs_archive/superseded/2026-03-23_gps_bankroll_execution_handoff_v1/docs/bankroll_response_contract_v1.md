# Bankroll Response Contract v1

## decisão por pick
A Banca deve responder por pick com:
- `decision_status`
- `stake_base`
- `stake_suggested`
- `stake_approved`
- `stake_pct_bankroll`
- `bank_state_mode`
- `portfolio_group`
- `exposure_bucket`
- `execution_order`
- `rules_triggered`
- `block_reason_code`
- `block_reason_text`
- `bankroll_note`

## enums mínimos
### decision_status
- `APPROVED`
- `APPROVED_REDUCED`
- `BLOCKED`
- `RESERVE`

### bank_state_mode
- `Normal`
- `Alerta`
- `Defesa`
- `Protecao_Maxima`

### portfolio_group
- `core`
- `satellite`
- `optional`

## regra
A Banca não altera:
- `global_score`
- `confidence_norm`
- `risk_norm`
- `edge_norm`
- `priority_tier`
- `normalization_version`
