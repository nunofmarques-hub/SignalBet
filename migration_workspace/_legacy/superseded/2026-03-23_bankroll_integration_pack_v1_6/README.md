# Bankroll & Risk Manager — Integration Pack v1.6

## Objetivo do pack
Fechar a ponte operacional **Global Pick Selector -> Banca -> Execution / Tracking** em formato de staging quase pronto para integração.

## Ficheiros principais
- `policy_files/bank_policy_v1_6.yaml`
- `decision_rules/bank_decision_rules_v1_6.yaml`
- `payload_selector_input/schema_b_selector_input_schema_v1_1.json`
- `payload_selector_input/schema_b_selector_input_example_v1_1.json`
- `payload_execution/schema_c_execution_output_schema_v1_1.json`
- `payload_execution/schema_c_execution_example_approved_v1_6.json`
- `payload_execution/schema_c_execution_example_approved_reduced_v1_6.json`
- `payload_execution/schema_c_execution_example_blocked_v1_6.json`
- `payload_execution/schema_c_execution_example_reserve_v1_6.json`
- `docs/Bankroll_Risk_Manager_Blueprint_Backend_v1_5.pdf`
- `docs/Bankroll_Risk_Manager_Blueprint_Backend_v1_5.docx`
- `docs/Contrato_Transversal_Integracao_SignalBet_v1_1_Operacional.pdf`

## Dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- payload real do Global Pick Selector no Schema B
- camada de estado da banca / exposure state
- execution layer capaz de consumir Schema C

## Destino final pretendido
- `modules/bankroll_risk_manager/`

## Estado
- `staging`

## Nota de integração
Este pack congela o consumo da banca sobre o **Schema B** e fecha o output da banca para **Schema C**. O ponto ainda dependente do sistema é o acoplamento ao payload real emitido pelo Global Pick Selector em ambiente de integração.
