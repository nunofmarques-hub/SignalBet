# Bankroll & Risk Manager — Corridor Pack v2.3

## objetivo do pack
Provar o corredor operacional real **GPS -> Banca -> Execution** em staging, sobre contrato já congelado, com batch de entrada do seletor, resposta batch da banca e payload final para intake da Execution.

## estado do pack
staging

## dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- pack do Global Pick Selector com batch shortlist e ponte para bankroll/execution
- upstream indireto progressivamente ligado ao Data_API_Official_Trunk_v1

## ponto de entrada
- `contracts/gps_to_bank_v23.json`
- `examples/gps_batch_in_v23.json`
- `src/flow_demo.py`

## ponto de saída
- `contracts/bank_to_exec_v23.json`
- `examples/exec_payload_v23.json`
- `examples/e2e_corridor_result_v23.json`

## referência ao contrato v1.1
Este pack assume o Contrato Transversal de Integração SignalBet v1.1 Operacional como referência oficial de ownership, enums, estados e linguagem de passagem entre camadas.

## indicação explícita de como lê da Data/API Layer ou do que falta para isso
A banca não lê diretamente da Data/API Layer. O seu upstream direto é o batch final do Global Pick Selector. O upstream indireto passa progressivamente a assentar em módulos ligados ao Data_API_Official_Trunk_v1.

## destino final pretendido
- `modules/bankroll_risk_manager/`

## ficheiros principais
- `contracts/gps_to_bank_v23.json`
- `contracts/bank_resp_v23.json`
- `contracts/bank_to_exec_v23.json`
- `contracts/bank_rules_v23.yaml`
- `contracts/bank_policy_v23.yaml`
- `src/flow_demo.py`
- `run_smoke.py`
- `examples/`
- `contracts/edge_cases/`
