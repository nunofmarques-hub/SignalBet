# Execution / Tracking

## Objetivo do pack
Pack limpo de substituição integral da linha ativa da Execution / Tracking, pronto para ocupar `modules/execution/` como linha viva oficial desta fase.

## Estado do pack
`linha oficial ativa`

## Módulo / frente
Execution / Tracking

## Dependências
- upstream oficial: Bankroll / Banca (`bank_to_exec_v24`)
- contexto oficial: provider de fixture do `Data_API_Official_Trunk_v1`
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
Esta linha lê settlement/contexto oficial a partir do payload final de fixture do `Data_API_Official_Trunk_v1`.

## Como correr o smoke test
```bash
python run_smoke.py
```

## O que este pack substitui
Substitui a linha viva atual por uma versão limpa e consolidada, removendo exemplos/handoffs superseded e notas transitórias já absorvidas.

## O que sai da pasta viva
- variantes intermédias de intake
- handoffs antigos de alinhamento
- notas de provisório já ultrapassadas
- staging redundante

## O que fica congelado nesta linha
- input oficial: `bank_to_exec_v24`
- settlement oficial com payload de fixture do `Data_API_Official_Trunk_v1`
- outputs núcleo: `ledger`, `analytics`, `audit`, `tracking_summary`
- runner oficial: `run_smoke.py`
