# SignalBet Corners + BTTS Pack

Este pack junta, numa única pasta, o que está disponível neste momento para gerir a recolha e a construção da master de Cantos.

## Inclui
- `scripts/signalbet_fixtures_pipeline.py` — pipeline base de recolha de fixtures
- `scripts/build_true_corners_master_2024.py` — gera o verdadeiro `corners_master_2024.json` a partir de `raw/stats/fixture_*.json`
- `scripts/START_SIGNALBET_FIXTURES_PIPELINE.cmd` — arranque rápido em Windows
- `README_signalbet_fixtures_pipeline.md` — notas de uso
- `docs/` — documentação de apoio de Cantos, BTTS e matriz mestra

## O que falta no pack
Os ficheiros separados dos módulos `signalbet_corners_pipeline.py`, `signalbet_btts_pipeline.py` e variantes `v2` não estão presentes neste ambiente neste momento, por isso não foram incluídos no ZIP.

## Uso prático
1. Colocar `api.env.txt` ao lado dos scripts, com o formato `API_KEY=...`
2. Correr a recolha base de fixtures
3. Garantir que existem ficheiros em `data_api_football/league_140/season_2024/raw/stats/fixture_*.json`
4. Correr `build_true_corners_master_2024.py` para gerar `masters/corners_master_2024.json`
