# Cantos

Script incluído:
- `build_true_corners_master_2024.py`

Função:
- Percorre `raw/stats/fixture_*.json`
- Extrai:
  - Corner Kicks
  - Total Shots
  - Blocked Shots
  - Ball Possession
  - Passes %
- Junta ao `fixture_id`
- Gera `corners_master_2024.json`

Comando típico:
`python build_true_corners_master_2024.py --root .`