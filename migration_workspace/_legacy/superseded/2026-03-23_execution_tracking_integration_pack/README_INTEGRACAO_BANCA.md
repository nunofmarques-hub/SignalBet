# README — Integração com a Banca

## Papel da Banca nesta fronteira
A Banca é a única origem autorizada de ordens para a Execution / Tracking Layer.

## Regra de entrada
A Execution só aceita payloads que respeitem:
- `source_system = BANKROLL_RISK_MANAGER`
- `decision_status = APPROVED`
- schema_version compatível com `execution-intake.v1`

## O que a Banca envia
Payload formal com:
- identidade da decisão
- identidade da pick
- mercado e seleção
- stake aprovada
- referência de odds aprovada
- janela de odds aprovada
- metadados de prioridade / portfolio
- timestamp da decisão
- regras acionadas

## O que a Execution devolve
### na entrada aceite
- `execution_id`
- `decision_id`
- `execution_status`
- `settlement_status`
- `status_changed_at`
- `execution_reason_code`
- `execution_reason_text`

### em rejeição operacional
- `execution_id`
- `decision_id`
- `execution_status = REJECTED_AT_EXECUTION`
- `execution_reason_code`
- `execution_reason_text`

## Erros de integração esperados
- `INVALID_SCHEMA`
- `MISSING_REQUIRED_FIELD`
- `INVALID_SOURCE`
- `INVALID_DECISION_STATUS`
- `DUPLICATE_ORDER`
- `DATA_MISMATCH`

## Nota operacional
A Execution não altera stake, não recalcula score e não reinterpreta a decisão. Em caso de problema, regista o problema.
