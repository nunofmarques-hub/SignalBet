# GAME_CARD_HANDOFF_CARDS

## estado
- linha: ativa
- estado: integrado
- bloco_app: game_cards

## ficheiro oficial
- `integration_feeds/cards/latest.json`

## shape mínima do candidate
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

## regra
Leitura curta, comparável e estável. Sem microindicadores, sem breakdown disciplinar profundo e sem payload rico demais.
