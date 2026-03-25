# README_E2E

## Caso ponta a ponta incluído
Fluxo principal coberto neste pack:
`APPROVED -> RECEIVED -> VALIDATION_PENDING -> VALIDATED -> READY_TO_EXECUTE -> EXECUTION_PENDING -> EXECUTED -> AWAITING_SETTLEMENT -> SETTLED`

## Ficheiros-chave
- `handoff/bankroll_case/bankroll_handoff_case_approved.json`
- `state_machine/e2e_flow/e2e_state_flow_settled_win.json`
- `settlement/e2e_case/fixture_settlement_case_win.json`
- `ledger/final_outputs/execution_ledger_settled_win.json`
- `analytics/final_outputs/execution_audit_feed_settled_win.json`

## Como usar
1. usar o payload da Banca como input da Execution
2. validar campos obrigatórios e criar `execution_id`
3. aplicar o fluxo de estados documentado
4. consumir o payload de settlement vindo da Data/API
5. comparar o output final com o ledger e audit feed fornecidos neste pack

## Casos adicionais incluídos
- `execution_ledger_missed_market_closed.json`
- `execution_ledger_void_fixture_cancelled.json`

## Critério de fecho deste pack
O pack fica bem sucedido se a implementação real reproduzir o ledger final e o output analytics a partir do payload de handoff e do payload de settlement.
