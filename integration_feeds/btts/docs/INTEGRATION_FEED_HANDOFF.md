# BTTS — Handoff do integration feed

## o que este pack substitui
Substitui o `integration_feeds/btts/latest.json` atual quando a frente quiser alinhar o feed vivo com o `game_card` curto fechado para a app phase 1.

## o que passa a ser a linha ativa
- `integration_feeds/btts/latest.json` vindo deste pack

## o que sai da linha viva
- feeds antigos mais ricos
- payloads transitórios
- outputs redundantes para `game_cards`

## o que vai para arquivo / histórico / legacy
- versões anteriores do `latest.json` que já não sejam a linha viva
- qualquer feed intermédio usado apenas em staging

## onde colar
Copiar `integration_feeds/btts/latest.json` para a árvore viva do projeto em `integration_feeds/btts/latest.json`.

## regra
Manter apenas um `latest.json` vivo para BTTS.
