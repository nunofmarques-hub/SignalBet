# Export Contract BTTS

## Destino semântico
O módulo BTTS deve exportar picks candidatas para a Opportunity Pool pelo schema:
- `market_pick.v1.1`

## Campos-base do envelope
- `schema_version`
- `pick_id`
- `created_at`
- `module_id = btts`
- `module_version`
- `event_id`
- `match_label`
- `competition`
- `market_family = btts`
- `market = match_btts`
- `selection`
- `odds`
- `eligibility`
- `score_raw`
- `confidence_raw`
- `risk_raw`
- `edge_raw`
- `rationale_summary`
- `main_drivers`
- `penalties`
- `data_quality_flag`
- `module_specific_payload`

## Payload específico BTTS
Dentro de `module_specific_payload` devem ficar:
- `btts_direction`
- `scoring_support`
- `concession_support`
- `bci_raw`
- `tsi_bilateral`
- `caps_applied`
- `warnings`
- `input_context`

## Regra de ownership
O BTTS exporta apenas:
- score/confiança/risco raw
- edge/raw strength
- racional
- drivers
- penalties
- contexto e qualidade do input

O BTTS **não** decide:
- stake
- prioridade financeira
- ranking global
