# GPS -> Bankroll -> Execution Matrix v2.3

| Step | Input | Owner | Output |
|---|---|---|---|
| 1 | `gps_shortlist_batch.v1` | Global Pick Selector | batch shortlist exportado para banca |
| 2 | shortlist batch | Bankroll & Risk Manager | `bankroll_response_batch.v1` |
| 3 | decisions batch | Bankroll & Risk Manager | `execution_intake_batch.v1` com picks execution_ready |
| 4 | execution batch | Execution / Tracking | intake operacional / placement / settlement |
