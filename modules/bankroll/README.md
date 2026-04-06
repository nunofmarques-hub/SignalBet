# Bankroll & Risk Manager — Active Line Clean Replacement v28

## Objetivo do pack
Entregar substituição integral limpa da pasta viva `modules/bankroll/`, preservando a linha oficial congelada da Banca e removendo resíduos, duplicações e artefactos já sem utilidade operacional.

## Estado do pack
pronto_para_integracao

## Dependências
- GPS v6 clean pack como upstream oficial
- Execution / Tracking como downstream oficial
- Contrato Transversal de Integração SignalBet v1.1 como referência de fronteira
- upstream indireto progressivamente alinhado com `Data_API_Official_Trunk_v1`

## Ponto de entrada
- `contracts/gps_to_bank_v24.json`
- `examples/gps_batch_in_v24.json`
- `run_smoke.py`

## Ponto de saída
- `contracts/bank_resp_v24.json`
- `contracts/bank_to_exec_v24.json`
- `examples/bank_resp_batch_v24.json`
- `examples/exec_payload_v24.json`

## Linha oficial ativa
- base ativa: v24
- estabilização/cleanup: v25
- substituição física limpa desta linha: v28

## App Phase 1
Ficheiros curtos do bloco `banking_decisions`:
- `contracts/app_phase1/banking_decisions_phase1_contract.json`
- `contracts/app_phase1/banking_decisions_phase1_example.json`
- `contracts/app_phase1/shortlist_enriched_with_banking_decisions_example.json`

## Regra operacional congelada
Seguem para Execution:
- `APPROVED`
- `APPROVED_REDUCED`

Ficam apenas auditados na Banca:
- `BLOCKED`
- `RESERVE`

## Destino final pretendido
`modules/bankroll/`
