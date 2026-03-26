# Daily Reporting Summary

## Estado geral da run
- run_id: RUN-20260326-151430
- readiness_level: real_ready
- preflight_status: PASS
- official_trunk_status: PASS
- project_feed_coverage_ratio: 1.0
- cta_state: ready_live

## Módulos ativos
- v12
- cards
- btts
- corners

## Contagens principais
- candidatos gerados pelo Orchestrator: 8
- candidatos vistos no export GPS: 4
- decisões da Banca: 4
- enviadas para Execution: 2
- approved: 1
- approved_reduced: 1
- blocked: 1
- reserve: 1

## Bloqueios / exceções relevantes
- execution_status do Orchestrator: SKIPPED
- modules_failed: 0
- warnings do Orchestrator: 0
- errors do Orchestrator: 0
- caso de trace bloqueado incluído nesta iteração: btts_003 (btts)

## Nota curta de auditabilidade
- trace factual com Execution preservado em `audit/audit_trace_sample.json`
- trace bloqueado pré-execution preservado em `audit/audit_trace_case_2.json`
- ownership por output explicitado nos artefactos técnicos desta frente

## Ownership deste output
- bruto produzido por: Orchestrator, Execution, Banca, GPS
- consolidado por: Analytics / Audit / Reporting
- lido por: PM, operação, futura UI quando fizer sentido

## Limitação remanescente
- o contexto do Orchestrator já entra por artefactos runtime do pack `sbo9/out`, mas ainda não existe uma interface dedicada desta frente para consumo desse contexto
