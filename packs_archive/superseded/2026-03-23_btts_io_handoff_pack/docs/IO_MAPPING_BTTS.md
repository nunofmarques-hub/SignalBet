# IO mapping BTTS

## Input central -> motor
- `league_snapshot` -> LigaScore BTTS
- `home_snapshot` / `away_snapshot` -> BOS / BVS / AMI / FGT / TSI
- `market_context` -> dominance / risco / output final

## Output do motor -> Opportunity Pool
O BTTS exporta `market_pick.v1.1` com:
- envelope comum do contrato transversal
- detalhes técnicos dentro de `module_specific_payload`

## Campos BTTS específicos no output
- `btts_direction`
- `scoring_support`
- `concession_support`
- `bci_raw`
- `caps_applied`
- `warnings`
