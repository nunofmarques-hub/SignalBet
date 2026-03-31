# game_card v12 — phase 1 contract

## Função
Entregar `game_cards` curtos, estáveis e comparáveis da v12 ao Orchestrator para a app phase 1.

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
- `module_name` deve ser sempre `v12`
- `market_code` deve estar limitado a:
  - `over15_team`
  - `over15_match`
  - `under35`
- `candidate_status` deve usar taxonomia curta e estável:
  - `candidate`
  - `watchlist`
  - `rejected`
- `risk_flags` deve ser lista curta e parseável
- `rationale_short` deve ser humano, breve e sem detalhe excessivo

## O que não entra
- BTTS
- Over 2.5
- Under 2.5
- linhas finas
- detalhe profundo de indicadores
- dumps internos do motor
