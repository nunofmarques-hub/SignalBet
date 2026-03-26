# Pseudofluxo Operacional

```text
receive bankroll handoff
  -> validate schema and source
  -> create execution order
  -> freeze snapshots
  -> move to READY_TO_EXECUTE
  -> register execution attempt
  -> if success: EXECUTED -> AWAITING_SETTLEMENT
  -> consume settlement payload from Data/API
  -> resolve market outcome
  -> compute return_amount and result_profit_loss
  -> close as SETTLED or VOID
  -> emit analytics/audit output
```
