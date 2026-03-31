# Bankroll / Banca

## Objetivo do pack
Linha oficial ativa da Banca / Bankroll & Risk Manager nesta fase, já limpa, estabilizada e pronta para substituir a linha anterior no módulo.

## Estado do pack
oficial_ativa_limpa

## Linha oficial ativa
v24, estabilizada pelo cleanup/freeze v25.

## Upstream oficial
GPS v6 clean pack.

## Downstream oficial
Execution / Tracking.

## Payload final oficial
`contracts/bank_to_exec_v24.json`

## Runner oficial desta fase
`run_smoke.py`

## O que fica congelado nesta linha
- `contracts/gps_to_bank_v24.json`
- `contracts/bank_resp_v24.json`
- `contracts/bank_to_exec_v24.json`
- `contracts/bank_rules_v24.yaml`
- `contracts/bank_policy_v24.yaml`
- edge cases associados à linha v24
- docs/contracts associados a esta linha

## Regra operacional congelada
### Seguem para Execution
- `APPROVED`
- `APPROVED_REDUCED`

### Ficam apenas auditados na Banca
- `BLOCKED`
- `RESERVE`

## App phase 1
O bloco curto da app phase 1 vive em:
- `contracts/app_phase1/banking_decisions_phase1_contract.json`
- `contracts/app_phase1/banking_decisions_phase1_example.json`
- `contracts/app_phase1/shortlist_enriched_with_banking_decisions_example.json`

## Ficheiros principais
- `run_smoke.py`
- `manifest.json`
- `contracts/`
- `examples/`
- `docs/`
- `tests/`
- `src/`

## Dependências
- GPS v6 clean pack como upstream oficial
- Execution / Tracking para consumo do `bank_to_exec_v24`
- Orchestrator / App Core para consumo do bloco curto da app phase 1

## Notas de limpeza
- removidos `__pycache__`
- removidos `.pyc`
- removidos ficheiros locais obsoletos ou redundantes desta linha
- mantido apenas o necessário para a linha oficial ativa
