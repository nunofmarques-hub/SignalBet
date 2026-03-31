# UI / Frontend — memória operacional ativa

## Frente
UI / Frontend

## Linha oficial ativa
UI v26

## Estado atual
linha oficial ativa

## Owner
UI / Frontend

## Upstream oficial
Orchestrator / App Core

## Downstream oficial
camada visível da app / operador humano

## Runner oficial desta fase
`run_smoke.bat`

## Papel atual na app phase 1
Consumir o payload protegido único da app phase 1 e materializar:
- home principal
- detalhe curto de jogo
- navegação shortlist → detalhe por `fixture_id` e `pick_id`

## Ajuste principal desta atualização
O ecrã de detalhe curto de jogo foi materializado como ecrã real:
- cabeçalho forte do jogo
- retorno claro à shortlist
- pick principal da shortlist
- game_cards do mesmo `fixture_id`
- banca curta por `pick_id`
- tracking curto por `pick_id`

## O que ficou fora deliberadamente
- novo payload
- tabs ricas
- modal pesado
- redesign geral
- estatística rica
- comparação profunda
- tracking longo
- policy da banca

## Bloqueios residuais
sem bloqueio estrutural nesta fase

## Próximo passo
Seguir com a linha ativa limpa e o fluxo home → detalhe já real e utilizável.
