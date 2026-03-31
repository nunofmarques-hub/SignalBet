# game_card v12 — phase 1 contract

## Shape final
- `fixture_id`
- `match_label`
- `module_name`
- `market_code`
- `selection_label`
- `raw_module_score`
- `score_band`
- `eligibility`
- `candidate_status`
- `rationale_short`
- `risk_flags`

## Regras
- `module_name` deve ser `v12`
- `market_code` limitado a:
  - `over15_team`
  - `over15_match`
  - `under35`
- `candidate_status`:
  - `candidate`
  - `watchlist`
  - `rejected`
- `risk_flags` deve ser lista curta e parseável
- `rationale_short` deve ser breve e legível

## Não entra
- BTTS
- Over 2.5
- Under 2.5
- detalhe profundo do motor
- dumps internos
