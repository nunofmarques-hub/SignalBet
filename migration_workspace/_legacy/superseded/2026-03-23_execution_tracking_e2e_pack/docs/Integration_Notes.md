# Notas de Integração

## Banca -> Execution
A Banca deve entregar um payload `execution-intake.v1` já em estado `APPROVED`.

## Execution -> Settlement
A Execution deve ficar em `AWAITING_SETTLEMENT` após execução concluída.

## Data/API -> Execution
O settlement hook mínimo precisa de:
- `event_id`
- `fixture_status`
- `score`
- `market_result_context`
- `settlement_timestamp`

## Execution -> Analytics/Audit
A saída recomendada é `execution-audit-feed.v1`, usando o ledger final consolidado como fonte de verdade operacional.
