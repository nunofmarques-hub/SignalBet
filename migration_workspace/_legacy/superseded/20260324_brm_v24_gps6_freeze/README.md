# Bankroll & Risk Manager — GPS6 Freeze Pack v2.4

## objetivo do pack
Congelar a camada financeira/operacional da banca o mais perto possível do fecho, assumindo o **GPS v6** como upstream oficial e deixando o corredor **GPS -> Banca -> Execution** em linguagem estável, determinística e auditável.

## estado do pack
staging

## módulo / frente
bankroll_risk_manager

## dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- Global Pick Selector v6 como upstream oficial de shortlist batch
- Execution / Tracking como downstream oficial de intake operacional
- upstream indireto progressivamente ligado ao Data_API_Official_Trunk_v1

## ponto de entrada
- `contracts/gps_to_bank_v24.json`
- `examples/gps_batch_in_v24.json`
- `src/flow_demo.py`

## ponto de saída
- `contracts/bank_to_exec_v24.json`
- `examples/exec_payload_v24.json`
- `examples/e2e_corridor_result_v24.json`

## referência ao contrato v1.1
Este pack assume o Contrato Transversal de Integração SignalBet v1.1 Operacional como referência oficial de ownership, enums, estados e linguagem de handoff.

## ligação à Data/API Layer
A banca não lê diretamente da Data/API Layer. O seu upstream direto é o batch final do GPS v6. O upstream indireto passa progressivamente a assentar em módulos ligados ao Data_API_Official_Trunk_v1.

## como correr o smoke test
```bash
python run_smoke.py
```

## destino final pretendido
- `modules/bankroll_risk_manager/`

## notas finais
Este pack reduz a ambiguidade em quatro pontos de fecho:
1. contrato final batch `gps_to_bank`
2. resposta batch estável `bank_resp`
3. payload final sem ambiguidades `bank_to_exec`
4. edge cases completos com resultado esperado para os 4 estados finais
