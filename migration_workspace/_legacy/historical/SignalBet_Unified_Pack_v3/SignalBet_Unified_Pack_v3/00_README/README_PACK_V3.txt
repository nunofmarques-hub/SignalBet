SignalBet / ABC PRO — Unified Pack v3

Estrutura
- 00_README: notas centrais do pack
- 10_PIPELINE_BASE: pipeline base para descoberta de fixtures e cache local
- 20_CORNERS: utilitário para gerar corners_master_2024.json a partir de raw/stats/fixture_*.json
- 30_BTTS: coletor de dados BTTS e outputs base
- 90_DOCS_REFERENCIA: documentação técnica de apoio

Ordem prática sugerida
1. Colocar api.env.txt junto dos scripts que vão fazer chamadas à API
2. Correr o pipeline base para descoberta de fixtures e cache local
3. Para Cantos, garantir que existem ficheiros em:
   data_api_football/league_140/season_2024/raw/stats/fixture_*.json
4. Correr o utilitário de Cantos para produzir:
   data_api_football/league_140/season_2024/masters/corners_master_2024.json
5. Correr o coletor BTTS para produzir masters e perfis do módulo BTTS

Defaults operacionais
- league = 140
- season = 2024
- status = FT-AET-PEN
