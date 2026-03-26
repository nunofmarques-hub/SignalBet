# Analytics / Audit / Reporting — First Real Pack

## objetivo do pack

Materializar a frente **Analytics / Audit / Reporting** num primeiro pack físico mínimo, disciplinado e executável, já ancorado em fontes reais do repositório oficial `nunofmarques-hub/SignalBet` na branch `main`.

O pack prova três blocos distintos:
- **analytics operacional**
- **audit trail**
- **reporting resumido**

## estado do pack

staging

## módulo / frente

analytics_audit_reporting

## dependências

- Python 3.11+
- standard library apenas
- repositório oficial SignalBet em `main`
- corredor central já existente:
  - GPS v6
  - Banca v24/v25 cleanup freeze
  - Execution / Tracking
  - App Core / Orchestrator (sbo9)

## fontes reais de leitura aplicadas neste pack

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
- `migration_workspace/app_core_orchestrator/sbo9/README.md`
- `migration_workspace/app_core_orchestrator/sbo9/STATUS.md`

## estrutura mínima obrigatória

- `README.md`
- `manifest.json`
- `analytics/`
- `audit/`
- `reporting/`
- `examples/`
- `run_smoke.py`

## artefactos mínimos obrigatórios

- `analytics/system_analytics_snapshot.json`
- `analytics/run_summary.json`
- `audit/audit_trace_sample.json`
- `reporting/daily_reporting_summary.md`

## o que cada bloco prova

### analytics
- consolidação mínima de volume de candidatos
- estados principais
- leitura por módulo/origem

### audit
- rastreabilidade mínima ponta a ponta de 1 caso
- ligação GPS -> Banca -> Execution
- contexto de run quando aplicável

### reporting
- síntese curta e legível do estado operacional
- módulos ativos
- aprovadas / reduzidas / bloqueadas / executadas
- alertas curtos

## ownership

### quem produz
- GPS produz shortlist e export upstream
- Banca produz decisões de risco e payload para Execution
- Execution produz ledger, analytics e audit locais
- Orchestrator produz contexto de run e discovery operacional

### quem consolida
- Analytics / Audit / Reporting

### quem lê
- operação interna
- governance
- revisão de qualidade
- PM
- futura UI, quando fizer sentido

## como correr o smoke test

```bash
python run_smoke.py
```

## nota operacional

O executivo nasce do técnico.
Este pack não cria dashboard, não cria camada visual e não duplica ownership das frentes de origem.
