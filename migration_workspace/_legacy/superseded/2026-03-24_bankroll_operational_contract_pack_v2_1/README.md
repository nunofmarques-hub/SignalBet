# Bankroll & Risk Manager — Operational Contract Pack v2.1

## Objetivo do pack
Congelar a camada financeira/operacional da banca com linguagem estável para handoff entre o Global Pick Selector e a Execution / Tracking.

## Estado do pack
staging

## Dependências
- Contrato_Transversal_Integracao_SignalBet_v1_1_Operacional.pdf
- Upstream direto: Global Pick Selector
- Upstream indireto: módulos progressivamente ligados ao Data_API_Official_Trunk_v1
- Material técnico de suporte da banca (blueprint backend v1.5)

## Ponto de entrada
- `schemas/gps_to_bankroll_contract_batch_v2_1.json`
- `examples/gps_to_bankroll_batch_input_example_v2_1.json`

## Ponto de saída
- `schemas/bank_to_execution_final_payload_v2_1.json`
- `examples/final_execution_payload_example_v2_1.json`

## Referência ao contrato v1.1
Este pack segue o Contrato Transversal de Integração SignalBet v1.1 Operacional.

## Como lê da Data/API Layer ou o que falta
A banca não consome a API externa diretamente. Lê do Global Pick Selector, que por sua vez deve estabilizar progressivamente sobre módulos ligados ao Data_API_Official_Trunk_v1.

## Ficheiros principais
- `policy_files/bank_policy_v2_1.yaml`
- `decision_rules/bank_decision_rules_v2_1.yaml`
- `schemas/gps_to_bankroll_contract_batch_v2_1.json`
- `schemas/bankroll_response_batch_contract_v2_1.json`
- `schemas/bank_to_execution_final_payload_v2_1.json`
- `edge_cases/expected_result_map_v2_1.json`

## Destino final pretendido
`modules/bankroll_risk_manager/`
