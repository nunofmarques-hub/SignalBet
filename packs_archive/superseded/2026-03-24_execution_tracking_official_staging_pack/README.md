# 2026-03-24 Execution Tracking Official Staging Pack

## Objetivo do pack
Provar um fluxo operacional real da Execution / Tracking com intake real vindo da Banca, settlement com payload oficial-orientado de fixture e output formal para analytics/audit.

## Estado do pack
staging

## Módulo / frente
execution_tracking

## Dependências
- handoff real da Banca (bankroll_response_batch.v1.8 + execution_intake_candidate.v1.8)
- Data_API_Official_Trunk_v1 como referência oficial da Data/API Layer
- contrato transversal v1.1 operacional

## Ponto de entrada
`run_smoke.py`

## Ponto de saída
- `tests/smoke_outputs/ledger.json`
- `tests/smoke_outputs/analytics.json`

## Referência ao contrato v1.1
Este pack segue o contrato transversal de integração SignalBet v1.1 e o contrato operacional interno da Execution / Tracking.

## Ligação à Data/API Layer
Provider declarado: `Data_API_Official_Trunk_v1`
Objeto de consumo: `fixtures/fixture_settlement_payload`
Estado atual: settlement oficial-orientado; a ligação final depende do shape definitivo do provider oficial de fixture.

## Como correr o smoke test
```bash
python run_smoke.py
```

## Notas finais
- Intake real já construído a partir do handoff da Banca.
- Settlement preparado para payload oficial do tronco.
- Output analytics/audit estabilizado para esta ronda.
