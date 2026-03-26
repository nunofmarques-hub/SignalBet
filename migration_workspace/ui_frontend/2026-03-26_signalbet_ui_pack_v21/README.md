# UI Frontend — SignalBet v21

## Objetivo do pack
Ronda de **validação comportamental da bridge protegida**.

Este pack foca-se em:
- validar comportamento de reuso, refresh, invalidação, fallback e transição entre modos
- fechar o ciclo do bloqueio local observado em `mock-data.js`
- manter a frente UI em staging disciplinado, sem fingir live total

## Estado do pack
**staging**

## Dependências
- browser moderno
- servidor local simples para servir `src/`
- sem dependência de trunk live ou orchestrator live

## Ponto de entrada
- `src/index.html`

## Ponto de saída
- shell navegável da UI
- painel do orchestrator com metadata da bridge
- docs de teste e bloqueios locais

## Contrato
Referência ao contrato transversal v1.1 e ao contrato operacional observado do Orchestrator.

## Data/API / Orchestrator
Este pack continua a usar leitura protegida e fontes mockadas/controladas.
Não liga live ao sistema real.
