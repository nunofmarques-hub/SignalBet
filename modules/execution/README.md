# Execution / Tracking

## Objetivo do pack
Pack limpo de substituição integral da linha oficial ativa da Execution / Tracking, pronto para ocupar `modules/execution/` como base viva desta fase.

## Estado do pack
`linha oficial ativa, madura e congelada nesta fase`

## Módulo / frente
Execution / Tracking

## Dependências
- upstream oficial: Bankroll / Banca (`bank_to_exec_v24`)
- contexto oficial de settlement: payload físico final de fixture do `Data_API_Official_Trunk_v1`
- Python 3.11+

## Ponto de entrada
- `run_smoke.py`

## Ponto de saída
- `tests/smoke_outputs/ledger.json`
- `tests/smoke_outputs/analytics.json`
- `tests/smoke_outputs/audit.json`
- `tests/smoke_outputs/tracking_summary.json`

## Referência contratual
Contrato Transversal de Integração SignalBet v1.1 Operacional.

## Ligação à Data/API Layer
Esta linha consome settlement/contexto oficial a partir do payload físico final de fixture do `Data_API_Official_Trunk_v1`.

## Como correr o smoke test
```bash
python run_smoke.py
```

## O que este pack substitui
Substitui integralmente a linha viva anterior de `modules/execution/` por uma linha limpa, sem ruído intermédio, crosswalks transitórios ou artefactos superseded a competir com a base oficial.

## O que sai da pasta viva
- variantes intermédias de intake
- notas de provisório já ultrapassadas
- handoffs antigos de alinhamento
- staging redundante
- artefactos transitórios já absorvidos

## O que fica congelado nesta linha
- input oficial: `bank_to_exec_v24`
- contexto oficial: payload final de fixture do `Data_API_Official_Trunk_v1`
- outputs núcleo: `ledger`, `analytics`, `audit`, `tracking_summary`
- runner oficial desta fase: `run_smoke.py`
