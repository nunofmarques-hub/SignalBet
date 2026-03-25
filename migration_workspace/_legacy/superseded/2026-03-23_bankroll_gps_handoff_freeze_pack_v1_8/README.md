# Bankroll & Risk Manager — GPS Handoff Freeze Pack v1.8

## objetivo do pack
Congelar o consumo real do payload do Global Pick Selector pela Banca e fechar, sem ambiguidades, a passagem Banca -> Execution / Tracking com exemplos operacionais e casos-limite.

## estado do pack
staging

## dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- pack do Global Pick Selector: `migration_workspace/global_pick_selector/2026-03-23_gps_bankroll_execution_handoff_v1/`
- política interna da Banca
- intake da Execution / Tracking

## ponto de entrada
- `schemas/gps_shortlist_batch_consumption_v1_8.json`
- `examples/gps_shortlist_batch_input_example_v1_8.json`

## ponto de saída
- `schemas/bankroll_response_batch_v1_8.json`
- `schemas/execution_intake_candidate_v1_8.json`
- `examples/bankroll_response_batch_example_v1_8.json`
- `examples/execution_intake_approved_example_v1_8.json`
- `examples/execution_intake_approved_reduced_example_v1_8.json`

## referência ao contrato v1.1
Este pack assume o Contrato Transversal de Integração SignalBet v1.1 Operacional como base oficial de ownership, enums, normalização, handoff entre GPS -> Banca -> Execution e decisão auditável.

## indicação explícita de como lê da Data/API Layer ou do que falta para isso
Este pack não lê diretamente da Data/API Layer. A Banca consome shortlist já produzida pelo Global Pick Selector. Dependência indireta: o GPS deve receber input oficial da Data/API via módulos de mercado. Falta apenas estabilização final do payload real emitido pelo GPS em integração viva.

## ficheiros principais
- `policy_files/bank_policy_v1_8.yaml`
- `decision_rules/bank_decision_rules_v1_8.yaml`
- `schemas/gps_shortlist_batch_consumption_v1_8.json`
- `schemas/bankroll_response_batch_v1_8.json`
- `schemas/execution_intake_candidate_v1_8.json`
- `examples/bankroll_response_batch_example_v1_8.json`
- `edge_cases/expected_result_map_v1_8.json`

## destino final pretendido
- `modules/bankroll_risk_manager/`
