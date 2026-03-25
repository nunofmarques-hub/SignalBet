# README de integração BTTS

## Objetivo
Clarificar como o módulo BTTS lê da base central e como devolve a pick candidata para a Opportunity Pool.

## Fluxo mínimo
1. Data/API Layer central constrói `central_match_input.json`
2. Engine BTTS consome esse payload
3. Engine calcula score raw e breakdown técnico
4. Exporter gera `market_pick.v1.1`
5. Payload segue para a Opportunity Pool

## Destino final
`modules/btts/`

## Estado atual
`teste`
