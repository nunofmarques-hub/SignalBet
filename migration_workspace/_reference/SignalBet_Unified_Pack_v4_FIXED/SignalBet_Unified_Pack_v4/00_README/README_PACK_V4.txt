SignalBet / ABC PRO — Unified Pack v4

Este pack corrige o problema estrutural do v3.

O que mudou:
- data_api_football ficou numa raiz comum do pack
- api.env.txt ficou numa raiz comum do pack
- os launchers .cmd usam --root .. e apontam para a raiz correta
- Cantos, BTTS e pipeline base passaram a trabalhar sobre a mesma base de dados local

Ordem de execução:
1) Preencher api.env.txt na raiz do pack
2) 10_PIPELINE_BASE\START_SIGNALBET_FIXTURES_PIPELINE.cmd
3) 30_BTTS\START_SIGNALBET_BTTS_DATA.cmd
4) 20_CORNERS\START_SIGNALBET_CORNERS_DATA.cmd

Saídas principais:
- data_api_football\league_140\season_2024\masters\fixtures_master.json
- data_api_football\league_140\season_2024\masters\btts_match_master_2024.json
- data_api_football\league_140\season_2024\masters\corners_master_2024.json

Defaults:
- league = 140
- season = 2024
- status = FT-AET-PEN
