# Bankroll & Risk Manager — Edge Cases Pack v1.7

## Objetivo do pack
Fechar a fronteira de consumo GPS -> Banca -> Execution com foco em cases-limite, congelamento do consumo do seletor e validação do payload final para execution.

## Ficheiros principais
- `policy_files/bank_policy_v1_7.yaml`
- `decision_rules/bank_decision_rules_v1_7.yaml`
- `payload_selector_input/schema_b_selector_input_schema_v1_1.json`
- `payload_execution/schema_c_execution_output_schema_v1_1.json`
- `edge_cases/*.json`

## Dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- Payload estabilizado do Global Pick Selector
- Camada de Execution / Tracking preparada para consumir o Schema C da banca

## Destino final pretendido
- `modules/bankroll_risk_manager/`

## Estado
- `staging`

## Notas de integração
1. A banca consome apenas payloads do seletor com `pool_status = exported_to_bankroll`.
2. A banca não reabre análise analítica do mercado; decide admissibilidade, sizing, cortes, bloqueios e disciplina de exposição.
3. O output formal para execution deve sair sempre em Schema C com `decision_status`, stakes e `rules_triggered`.
4. Este pack traz exemplos normais e de fronteira para teste de contrato, gates prudenciais e fixture lock.
