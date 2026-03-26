# GPS Alignment Matrix v1.8

## batch recebido do GPS
- `batch_schema_version` -> deve ser `gps_shortlist_batch.v1`
- `selector_run_id` -> obrigatório
- `normalization_version` -> obrigatório
- `picks[]` -> lote de picks em linguagem comparável

## por pick, a banca consome
- `pick_id`
- `module_id`
- `event_id`
- `match_label`
- `market_family`
- `market`
- `selection`
- `line`
- `odds`
- `global_score`
- `confidence_norm`
- `risk_norm`
- `edge_norm`
- `priority_tier`
- `conflict_flags`
- `correlation_flags`
- `executive_rationale`
- `pool_status`

## regra de ownership
- GPS é dono da linguagem comparável
- Banca é dona da linguagem financeira e operacional
- Execution é dona do placement e settlement
