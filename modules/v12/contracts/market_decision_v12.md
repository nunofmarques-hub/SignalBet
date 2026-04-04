# market_decision_v12 — contract

## Campos mínimos do output desta frente
- `fixture_id`
- `match_label`
- `module_name`
- `markets`

### markets
Lista curta com os 3 mercados maduros, cada um contendo:
- `market_code`
- `tsi`
- `dci`
- `market_probability`
- `fair_odds`
- `edge_pct`
- `eligibility`
- `rationale_short`

## Campo final de escolha
- `best_market_code`
- `best_selection_label`
- `best_market_probability`
- `best_fair_odds`
- `best_edge_pct`
- `decision_summary`

## Regras
- só entram `over15_team`, `over15_match`, `under35`
- `tsi` e `dci` devem ser auditáveis e legíveis
- `market_probability` deve estar em escala 0-1
- `fair_odds` = 1 / probability
- `edge_pct` = (odd_real / fair_odds) - 1, quando odd real existir
