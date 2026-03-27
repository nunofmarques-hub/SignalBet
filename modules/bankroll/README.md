# Bankroll & Risk Manager — v25 Cleanup Freeze Pack

## Objetivo do pack
Limpar resíduos de ambiente, confirmar formalmente a linha v24 como linha oficial ativa da Banca e entregar o corredor GPS -> Banca -> Execution em formato de staging forte, pronto para downstream real.

## Estado do pack
staging

## Dependências
- Global Pick Selector v6 como upstream oficial
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- Execution / Tracking a consumir `bank_to_exec_v24`
- Upstream indireto progressivamente alinhado com `Data_API_Official_Trunk_v1`

## Ponto de entrada
- `contracts/gps_to_bank_v24.json`
- `examples/gps_batch_in_v24.json`
- `run_smoke.py`

## Ponto de saída
- `contracts/bank_resp_v24.json`
- `contracts/bank_to_exec_v24.json`
- `examples/bank_resp_batch_v24.json`
- `examples/exec_payload_v24.json`

## Referência ao contrato v1.1
Este pack assume o Contrato Transversal de Integração SignalBet v1.1 Operacional como referência oficial da fronteira GPS -> Banca -> Execution.

## Como lê da Data/API Layer ou o que falta
A Banca não consome a API externa diretamente. O seu upstream oficial é o GPS v6, que por sua vez consolida picks vindas de módulos progressivamente ligados ao `Data_API_Official_Trunk_v1`.

## Ficheiros principais
- `contracts/gps_to_bank_v24.json`
- `contracts/bank_resp_v24.json`
- `contracts/bank_to_exec_v24.json`
- `contracts/bank_rules_v24.yaml`
- `contracts/bank_policy_v24.yaml`
- `contracts/edge_cases/expected_v24.json`
- `examples/approved_v24.json`
- `examples/approved_reduced_v24.json`
- `examples/blocked_v24.json`
- `examples/reserve_v24.json`
- `docs/closure_note_v25.md`

## Destino final pretendido
`modules/bankroll_risk_manager/`

## Nota de linha oficial ativa
A linha oficial ativa da Banca fica confirmada nesta ronda como a linha v24, com `bank_to_exec_v24` mantido como payload final oficial para consumo da Execution.
