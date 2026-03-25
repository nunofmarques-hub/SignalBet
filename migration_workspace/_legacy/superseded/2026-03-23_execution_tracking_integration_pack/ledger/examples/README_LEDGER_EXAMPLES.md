# Ledger examples — leitura operacional

## Caso 1 — Settled WIN
Fluxo esperado:
APPROVED (na Banca) -> RECEIVED -> VALIDATED -> READY_TO_EXECUTE -> EXECUTED -> AWAITING_SETTLEMENT -> SETTLED

## Caso 2 — MISSED
Fluxo esperado:
APPROVED -> RECEIVED -> VALIDATED -> READY_TO_EXECUTE -> EXECUTION_PENDING -> MISSED

## Caso 3 — VOID
Fluxo esperado:
APPROVED -> RECEIVED -> VALIDATED -> READY_TO_EXECUTE -> EXECUTED -> AWAITING_SETTLEMENT -> VOID

## Objetivo destes exemplos
Servirem como payloads de reconciliação entre:
- Banca
- Execution
- Analytics / Audit
