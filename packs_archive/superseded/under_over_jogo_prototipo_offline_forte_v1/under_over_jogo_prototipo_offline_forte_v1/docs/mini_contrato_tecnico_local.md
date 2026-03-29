# Mini-Contrato Técnico Local — Under/Over Jogo

## Input mínimo obrigatório
- `lambda_league`
- `GPI_M`
- `DRI_M`
- `OPI_M`
- `NRI_M`
- `AttackAdj`
- `DefenseAdj`
- `PaceAdj`
- `RiskAdj`
- `a`
- `b`
- `c`
- `d`
- `market_odds` por linha

## Input auxiliar
- `risk_flags`
- `scenario_name`

## Output mínimo por cenário
- `module_name`
- `module_version`
- `scenario_name`
- `base_state`
  - `OU_Base_Score`
  - `lambda_match`
  - `profile`
- `results` por linha
  - `market_code`
  - `selection_label`
  - `lambda_match`
  - `probability`
  - `fair_odds`
  - `market_odds`
  - `edge`
  - `eligibility`
  - `candidate_status`
  - `risk_flags`

## Naming estável
Os campos acima devem manter naming estável nesta fase offline.
