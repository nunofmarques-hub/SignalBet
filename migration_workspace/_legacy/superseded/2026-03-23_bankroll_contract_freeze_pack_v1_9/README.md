# Bankroll & Risk Manager — Contract Freeze Pack v1.9

## objetivo do pack
Congelar a camada financeira/operacional da Banca em linguagem estável, fechando sem ambiguidades o contrato GPS -> Banca e o payload final Banca -> Execution.

## estado do pack
staging

## dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- pack do Global Pick Selector: `migration_workspace/global_pick_selector/2026-03-23_gps_bankroll_execution_handoff_v1/`
- estado interno da política de banca (`policy_files/`)
- corredor de intake futuro da Execution / Tracking

## ponto de entrada
- `schemas/gps_shortlist_batch_contract_v1_9.json`
- `examples/gps_shortlist_batch_input_example_v1_9.json`

## ponto de saída
- `schemas/bankroll_response_batch_contract_v1_9.json`
- `schemas/execution_intake_final_contract_v1_9.json`
- `examples/bankroll_response_batch_example_v1_9.json`
- `examples/execution_intake_final_example_v1_9.json`

## referência ao contrato v1.1
Este pack assume o Contrato Transversal de Integração SignalBet v1.1 Operacional como base oficial de ownership, enums, linguagem de handoff e decisão auditável.

## indicação explícita de como lê da Data/API Layer ou do que falta para isso
Este pack não lê diretamente da Data/API Layer. A Banca consome shortlist já produzida pelo Global Pick Selector. Dependência indireta: o GPS deve consumir input oficial da Data/API via módulos analíticos. Falta apenas estabilização definitiva do payload real emitido pelo GPS em integração viva.

## ficheiros principais
- `policy_files/bank_policy_v1_9.yaml`
- `decision_rules/bank_decision_rules_v1_9.yaml`
- `schemas/gps_shortlist_batch_contract_v1_9.json`
- `schemas/bankroll_response_batch_contract_v1_9.json`
- `schemas/execution_intake_final_contract_v1_9.json`
- `examples/bankroll_response_batch_example_v1_9.json`
- `edge_cases/expected_result_map_v1_9.json`

## destino final pretendido
- `modules/bankroll_risk_manager/`
