# Execution / Tracking — Bankroll Crosswalk Pack v1

## objetivo do pack
Cruzar as últimas versões do Global Pick Selector e da Banca para fechar a fronteira real GPS -> Banca -> Execution, identificar o que já pode ser consumido pela Execution e congelar a recomendação de handoff operacional para intake real.

## estado do pack
staging

## dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- `migration_workspace/global_pick_selector/2026-03-23_gps_bankroll_execution_handoff_v1/`
- `migration_workspace/bankroll_risk_manager/2026-03-23_bankroll_gps_handoff_freeze_pack_v1_8/`
- Data/API Layer para settlement posterior

## ponto de entrada
- `handoff_crosswalk/gps_vs_bankroll_vs_execution_crosswalk.md`
- `intake/schema_final/execution_intake_real_candidate.v1.json`
- `intake/examples/execution_intake_real_example.json`

## ponto de saída
- `docs/execution_bankroll_alignment_note.md`
- `analytics/output_contracts/execution_analytics_output.v1.json`
- `settlement/hooks/execution_settlement_hook_required_payload_v1.json`

## referência ao contrato v1.1
Este pack usa o Contrato Transversal de Integração SignalBet v1.1 Operacional como base semântica para ownership, handoff, auditabilidade e continuidade GPS -> Banca -> Execution.

## indicação explícita de como lê da Data/API Layer ou do que falta para isso
Este pack ainda não lê diretamente da Data/API Layer. Fecha apenas o intake real vindo da Banca e congela o payload mínimo que a Execution precisará da Data/API para settlement. Falta integração viva ao provider oficial da Data/API.

## destino final pretendido
- `modules/execution_tracking/`
