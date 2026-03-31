# Execution / Tracking — Linha oficial ativa (cleanup pack)

## objetivo do pack
Alinhar a pasta `modules/execution/` com a linha oficial ativa e congelada da frente Execution / Tracking, sem alterar lógica interna.

## estado do pack
linha_oficial_ativa_congelada

## módulo / frente
execution_tracking

## dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- input oficial: `bank_to_exec_v24`
- contexto oficial: payload final de fixture do `Data_API_Official_Trunk_v1`

## ponto de entrada
- `run_smoke.py`
- `examples/intake/bank_to_exec_v24_example.json`
- `contracts/upstream/bank_to_exec_v24.schema.json`

## ponto de saída
- `tests/smoke_outputs/ledger.json`
- `tests/smoke_outputs/analytics.json`
- `tests/smoke_outputs/audit.json`
- `tests/smoke_outputs/tracking_summary.json`

## ligação à Data/API Layer
- caminho oficial ativo: `Data_API_Official_Trunk_v1`
- contexto oficial de settlement: `execution_fixture_payload`

## como correr o smoke test
```bash
python run_smoke.py
```

## nota
Este pack é apenas de limpeza e alinhamento documental da linha oficial ativa. Não reabre arquitetura nem altera contratos núcleo.
