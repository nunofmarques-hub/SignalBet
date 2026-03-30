# App Phase 1 Protected Payload — contrato curto oficial

## bloco 1
`system_status`

### origem
Orchestrator / App Core + Data/API Layer

### campos mínimos
- `readiness_level`
- `cta_state`
- `source_mode`
- `observed_mode`
- `bridge_status`
- `snapshot_name`
- `final_status`
- `baseline_status`
- `complementary_status`
- `central_health`
- `summary_human`

---

## bloco 2
`shortlist`

### origem
GPS / Global Pick Selector

### campos mínimos por item
- `pick_id`
- `module_name`
- `fixture_id`
- `match_label`
- `market_code`
- `selection_label`
- `rank_position`
- `rationale_short`

---

## bloco 3
`game_cards`

### origem
v12 / Cards / BTTS / Corners

### campos mínimos por item
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

---

## bloco 4
`banking_decisions`

### origem
Bankroll / Banca

### campos mínimos por item
- `pick_id`
- `decision_status`
- `stake_approved`
- `stake_suggested`
- `stake_pct_bankroll`
- `execution_ready`
- `daily_exposure_after_if_accepted`
- `decision_note`

---

## bloco 5
`tracking_summary`

### origem
Execution / Tracking

### campos mínimos por item
- `pick_id`
- `execution_status`
- `ticket_status`
- `settlement_status`
- `result`
- `pnl`
- `timestamp`

---

## regra desta ronda
- envelope único
- naming estável
- sem campos concorrentes
- sem a UI precisar de adivinhar nada
- proveniência marcada dentro de cada bloco por `_block_source`
