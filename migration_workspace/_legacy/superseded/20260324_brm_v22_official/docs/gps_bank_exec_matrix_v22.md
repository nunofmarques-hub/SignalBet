# Matriz GPS -> Banca -> Execution v2.2

| camada | input | output | ownership |
|---|---|---|---|
| GPS | raw/normalized dos módulos | shortlist_batch_exported_to_bankroll | ranking, score normalizado, prioridade |
| Banca | `gps_to_bank_v22.json` | `bank_resp_v22.json` | admissibilidade, sizing, decision status |
| Execution | `bank_to_exec_v22.json` | intake operacional | execução e tracking |

Estados finais suportados pela banca:
- APPROVED
- APPROVED_REDUCED
- BLOCKED
- RESERVE
