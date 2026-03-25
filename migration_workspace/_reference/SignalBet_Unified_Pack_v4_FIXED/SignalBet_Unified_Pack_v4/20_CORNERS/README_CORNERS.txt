Cantos

Ordem:
1) Colocar a API em api.env.txt na raiz do pack
2) Correr 10_PIPELINE_BASE\START_SIGNALBET_FIXTURES_PIPELINE.cmd
3) Correr 20_CORNERS\START_SIGNALBET_CORNERS_DATA.cmd

O launcher de Cantos usa a raiz do pack (--root ..), por isso vai procurar os stats em:
data_api_football\league_140\season_2024\raw\stats\fixture_*.json

Saída:
data_api_football\league_140\season_2024\masters\corners_master_2024.json
