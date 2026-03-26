# Regras de output — contrato v1.1

A v12 deve emitir picks candidatas em `schema_version = market_pick.v1.1`.

## Obrigatório
- pick_id
- created_at
- module_id
- module_version
- event_id
- match_label
- competition
- market_family
- market
- selection
- line
- odds
- eligibility
- score_raw
- confidence_raw
- risk_raw
- edge_raw
- rationale_summary
- main_drivers
- penalties
- data_quality_flag

## Recomendado e já suportado neste pack
- kickoff_datetime
- module_rank_internal
- expiry_context
- module_specific_payload
