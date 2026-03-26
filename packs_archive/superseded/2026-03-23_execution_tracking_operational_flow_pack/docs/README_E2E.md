# README E2E

## Caso principal
1. A Banca entrega `bankroll_handoff_real_case_v1.json`
2. O intake valida origem, schema e campos obrigatórios
3. A ordem percorre `RECEIVED -> VALIDATION_PENDING -> VALIDATED -> READY_TO_EXECUTE -> EXECUTION_PENDING -> EXECUTED -> AWAITING_SETTLEMENT -> SETTLED`
4. O settlement consome o payload de fixture-alvo
5. A Execution produz o ledger final e o output formal para analytics/audit

## Casos auxiliares
- `execution_intake_test_fail_missing_odds_reference_v1.json` prova rejeição no intake
- `execution_ledger_missed_market_closed_v1.json` prova falha operacional
- `execution_ledger_void_fixture_cancelled_v1.json` prova fecho em void
