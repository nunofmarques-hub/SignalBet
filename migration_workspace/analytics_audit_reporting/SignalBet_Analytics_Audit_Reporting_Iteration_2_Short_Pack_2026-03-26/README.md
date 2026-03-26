# Analytics / Audit / Reporting — Iteração 2 Curta

## objetivo do pack

Reforçar a materialização mínima da frente sobre fontes reais já identificadas, com melhoria curta de:
- contexto runtime
- rastreabilidade
- reporting
- ownership por output

## estado do pack

staging_forte_inicial

## módulo / frente

analytics_audit_reporting

## foco desta iteração

Sem redesenho estrutural.
Sem dashboard.
Sem duplicação de ownership das frentes de origem.

Esta iteração reforça:
- a entrada do Orchestrator com contexto mais runtime (`out/last_sum.json`, `out/last_health.json`, `out/last_ui.json`)
- um segundo caso de audit trace
- um `daily_reporting_summary.md` mais rico
- ownership explícito por output gerado

## fontes reais aplicadas

### GPS
- `migration_workspace/global_pick_selector/2026-03-24_global_pick_selector_integration_critical_pack_v6_final/examples/bankroll_export_outputs/bankroll_export_case_main.json`

### Banca
- `migration_workspace/bankroll_risk_manager/20260324_brm_v25_cleanup_freeze/examples/bank_resp_batch_v24.json`
- `migration_workspace/bankroll_risk_manager/20260324_brm_v25_cleanup_freeze/examples/exec_payload_v24.json`

### Execution
- `migration_workspace/execution_tracking/2026-03-24_execution_tracking_corridor_minimum_ready_pack/tests/smoke_outputs/analytics.json`
- `migration_workspace/execution_tracking/2026-03-24_execution_tracking_corridor_minimum_ready_pack/tests/smoke_outputs/audit.json`
- `migration_workspace/execution_tracking/2026-03-24_execution_tracking_corridor_minimum_ready_pack/tests/smoke_outputs/ledger.json`

### Orchestrator
- `migration_workspace/app_core_orchestrator/sbo9/out/last_sum.json`
- `migration_workspace/app_core_orchestrator/sbo9/out/last_health.json`
- `migration_workspace/app_core_orchestrator/sbo9/out/last_ui.json`
- `migration_workspace/app_core_orchestrator/sbo9/out/proof_stdout.json`

## outputs obrigatórios desta iteração

- `analytics/system_analytics_snapshot.json`
- `analytics/run_summary.json`
- `audit/audit_trace_sample.json`
- `reporting/daily_reporting_summary.md`

## output extra desta iteração

- `audit/audit_trace_case_2.json`

## ownership por output

### `analytics/system_analytics_snapshot.json`
- bruto produzido por: Execution, Banca, GPS, Orchestrator
- consolidado por: Analytics / Audit / Reporting
- lido por: operação interna, QA, governance

### `analytics/run_summary.json`
- bruto produzido por: Orchestrator + Execution
- consolidado por: Analytics / Audit / Reporting
- lido por: operação interna, PM

### `audit/audit_trace_sample.json`
- bruto produzido por: GPS, Banca, Execution, Orchestrator
- consolidado por: Analytics / Audit / Reporting
- lido por: governance, revisão operacional

### `reporting/daily_reporting_summary.md`
- bruto produzido por: Orchestrator, Execution, Banca, GPS
- consolidado por: Analytics / Audit / Reporting
- lido por: PM, operação, futura UI quando fizer sentido

## como correr

```bash
python run_smoke.py
```

## limitação remanescente

O contexto do Orchestrator já entra de forma mais runtime nesta iteração, mas ainda é baseado em artefactos de saída do pack `sbo9` e não numa interface dedicada desta frente.

Isso não bloqueia a iteração 2, mas continua a ser a melhoria natural seguinte.
