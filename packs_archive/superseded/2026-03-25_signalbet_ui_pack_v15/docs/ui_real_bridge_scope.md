# UI Real Bridge Scope

## O que entra por ponte real neste v15
- snapshot JSON externo/protegido em modo `real_read_protected`
- campos mínimos aceites:
  - `cta_state`
  - `readiness_level`
  - `project_feed_coverage_ratio`
  - `pipeline_state`
  - `current_stage`
  - `summary`
  - `module_overview`
  - `pipeline_steps`

## Onde é usado
- painel “Pôr tudo a correr”
- Home / Dashboard
- blocos de pipeline / readiness
