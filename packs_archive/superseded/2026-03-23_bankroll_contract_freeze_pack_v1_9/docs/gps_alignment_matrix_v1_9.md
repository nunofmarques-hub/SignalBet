# GPS -> Banca -> Execution Alignment Matrix v1.9

| camada | ownership | entrada | saída |
|---|---|---|---|
| GPS | linguagem comparável | picks dos módulos | shortlist batch para Banca |
| Banca | linguagem financeira/operacional | `gps_shortlist_batch.v1` | `bankroll_response_batch.v1.9` + `execution_intake_final.v1.9` |
| Execution | intake operacional | apenas picks `APPROVED` ou `APPROVED_REDUCED` | tracking, settlement, audit |

## regra-base
A Banca não recalcula profundamente o mercado. Usa `global_score`, `confidence_norm`, `risk_norm`, `edge_norm` e `priority_tier` como verdade comparável recebida do GPS.
