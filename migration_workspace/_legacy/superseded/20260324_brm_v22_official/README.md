# 20260324_brm_v22_official

## objetivo do pack
Congelar a camada financeira/operacional da Banca / Bankroll & Risk Manager em linguagem estável para downstream real, com contrato final GPS -> banca, payload final banca -> execution, rules mais fechadas e edge cases completos.

## estado do pack
staging

## módulo / frente
bankroll_risk_manager

## dependências
- Contrato_Transversal_Integracao_SignalBet_v1_1_Operacional
- Global Pick Selector como upstream direto
- Data_API_Official_Trunk_v1 como upstream indireto, via módulos analíticos e GPS
- Python 3.11+ para smoke test

## ponto de entrada
- `run_smoke.py`
- apoio técnico em `src/bank_service_pseudocode.py`

## ponto de saída
- `contracts/bank_to_exec_v22.json`
- `examples/exec_payload_v22.json`
- `examples/approved_v22.json`
- `examples/approved_reduced_v22.json`
- `examples/blocked_v22.json`
- `examples/reserve_v22.json`

## referência ao contrato v1.1
Este pack assume como referência oficial o `Contrato_Transversal_Integracao_SignalBet_v1_1_Operacional.pdf` e mantém os enums, ownership semântico e corredor GPS -> Banca -> Execution coerentes com o contrato.

## ligação à Data/API Layer
A banca não consome a API externa diretamente. O upstream direto é o Global Pick Selector. O upstream indireto passa progressivamente a assentar em módulos ligados ao `Data_API_Official_Trunk_v1`. Este pack deixa esse ponto explícito no `manifest.json` e nos docs de integração.

## como correr o smoke test
```bash
python run_smoke.py
```
O smoke test valida a estrutura mínima, abre os contratos principais, verifica os exemplos finais e gera/atualiza `pack_check_report.txt`.

## notas finais
- pack já em formato oficial de ronda
- inclui `README.md`, `manifest.json`, `run_smoke.py`, `pack_check_report.txt`, `src/`, `docs/`, `tests/`, `examples/` e `contracts/`
- nomes mantidos curtos para reduzir risco de erro de caminho longo no Windows
