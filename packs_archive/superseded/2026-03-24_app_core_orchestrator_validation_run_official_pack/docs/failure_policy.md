
# Failure policy

- `FAIL` bloqueante no preflight aborta a corrida.
- `WARN` permite continuar em `validation_run`.
- `execution_status` fica `SKIPPED` em `validation_run` e `dry_run`.
- `btts` e `corners` podem ficar `SKIPPED` por maturidade/registry sem bloquear o fluxo.
