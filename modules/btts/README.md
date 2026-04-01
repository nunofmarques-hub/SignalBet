# BTTS

## objetivo do pack
Substituição integral limpa da linha viva do módulo BTTS, alinhada com o fecho obrigatório do `game_card` da app phase 1.

## estado do pack
integrado

## papel atual
Fornecedor curto e estável de `game_cards` para o payload protegido da app phase 1 via Orchestrator.

## ponto de entrada
`run_smoke.py`

## ponto de saída
`latest.json`

## output ativo
O output vivo desta linha é o `latest.json` com `game_cards` curtos.

## o que este pack substitui
Substitui a linha viva anterior do BTTS que ainda misturava output rico de mercado, artefactos de handoff transitórios e exemplos redundantes.

## o que passa a ser a linha ativa
Este pack passa a ser a linha oficial viva do BTTS na pasta `modules/btts/`.

## o que sai da pasta viva
- outputs ricos antigos não necessários nesta ronda
- notas transitórias duplicadas de handoff
- artefactos de runtime já ultrapassados
- exemplos redundantes que competiam com a linha ativa

## o que deve ir para arquivo / histórico / legacy
- packs anteriores
- outputs ricos antigos
- notas de aproximação e runtime já consolidadas
- exemplos superseded
