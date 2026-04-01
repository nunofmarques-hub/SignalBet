# BTTS — Handoff do integration feed

## O que este pack substitui
Substitui o `integration_feeds/btts/latest.json` atual quando a frente quiser alinhar o feed vivo com o game_card curto fechado para a app phase 1.

## O que passa a ser a linha ativa
- `integration_feeds/btts/latest.json` vindo deste pack

## O que sai da linha viva
- feeds antigos mais ricos
- payloads transitórios
- outputs redundantes para game_cards

## O que vai para arquivo / histórico / legacy
- versões anteriores do `latest.json` que já não sejam a linha viva
- qualquer feed intermédio usado apenas em staging

## Onde colar
Copiar:
- `integration_feeds/btts/latest.json`

Para:
- `integration_feeds/btts/latest.json` na árvore viva do projeto

## Regra
Manter apenas um `latest.json` vivo para BTTS.
