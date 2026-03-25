# Bankroll & Risk Manager — Migration Pack v1.5

## Objetivo do pack
Entregar um pack modular de teste/staging do módulo **Bankroll & Risk Manager**, alinhado com o Contrato Transversal de Integração SignalBet v1.1 Operacional, já preparado para migração controlada a partir de `migration_workspace/`.

## Ficheiros principais
- `policy_files/bank_policy_v1_5.yaml`
- `decision_rules/bank_decision_rules_v1_5.yaml`
- `payload_execution/schema_c_execution_example_v1_5.json`
- `payload_execution/schema_b_selector_input_example_v1_1.json`
- `docs/Bankroll_Risk_Manager_Blueprint_Backend_v1_5.pdf`
- `docs/Bankroll_Risk_Manager_Blueprint_Backend_v1_5.docx`
- `docs/Contrato_Transversal_Integracao_SignalBet_v1_1_Operacional.pdf`

## Dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- Global Pick Selector a emitir Schema B válido
- Execution / Tracking a consumir Schema C
- Camada central de persistência para audit trail, fixture lock e exposição diária

## Destino final pretendido
`modules/bankroll_risk_manager/`

## Estado
staging
