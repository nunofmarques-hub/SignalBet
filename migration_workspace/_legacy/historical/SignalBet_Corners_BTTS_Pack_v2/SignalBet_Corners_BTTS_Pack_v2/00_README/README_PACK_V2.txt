# SignalBet / ABC PRO — Pack v2

## Estrutura
- `00_README` — notas centrais do pack
- `10_PIPELINE_BASE` — pipeline base para descoberta de fixtures e cache local
- `20_CORNERS` — utilitário para gerar o `corners_master_2024.json` a partir de `raw/stats/fixture_*.json`
- `30_BTTS` — reservado para os utilitários BTTS quando forem centralizados neste pack
- `90_DOCS_REFERENCIA` — documentação técnica de apoio

## Ordem prática sugerida
1. Colocar `api.env.txt` ao lado do script base em `10_PIPELINE_BASE`
2. Correr a descoberta de fixtures e recolha/caching base
3. Garantir que existem ficheiros em:
   `data_api_football/league_140/season_2024/raw/stats/fixture_*.json`
4. Correr o utilitário de cantos para produzir:
   `data_api_football/league_140/season_2024/masters/corners_master_2024.json`

## Nota
Neste ambiente de trabalho estavam disponíveis o pipeline base e o utilitário de cantos.
Os scripts BTTS/Corners v2 podem ser adicionados mais tarde a esta mesma estrutura.