# SignalBet BTTS Data Collector

## Objetivo
Recolher e organizar dados da API-Football para o motor BTTS do projeto SignalBet / ABC PRO.

## Pré-requisito
Criar `api.env.txt` na mesma pasta do script com:

```txt
API_KEY=... 
```

## Defaults
- league: 140
- season: 2024
- status: FT-AET-PEN

## Comandos

### Descobrir fixtures e IDs
```bash
python signalbet_btts_data_collector.py discover --league 140 --season 2024 --status FT-AET-PEN
```

### Recolher núcleo BTTS
```bash
python signalbet_btts_data_collector.py collect-core --league 140 --season 2024 --status FT-AET-PEN
```

### Reforço observável / mercado
```bash
python signalbet_btts_data_collector.py collect-reinforcement --league 140 --season 2024 --with-predictions --with-odds
```

### Construir masters
```bash
python signalbet_btts_data_collector.py build-masters --league 140 --season 2024
```

### Fluxo completo
```bash
python signalbet_btts_data_collector.py full-bootstrap --league 140 --season 2024 --status FT-AET-PEN --with-reinforcement
```

## Outputs principais
- `data_api_football/league_140/season_2024/masters/btts_match_master_2024.json`
- `data_api_football/league_140/season_2024/masters/btts_match_master_2024.csv`
- `data_api_football/league_140/season_2024/masters/btts_team_profiles_overall_2024.json`
- `data_api_football/league_140/season_2024/masters/btts_data_contract.json`

## Campos derivados principais
- `btts_yes`
- `halftime_0_0`
- `first_goal_minute`
- `goal_until_30`
- `response_after_conceding`
- `score_rate_1plus`
- `concede_rate_1plus`
- `clean_sheet_inverse_rate`
- `bos_score_lite`
- `bvs_score_lite`
- `ami_score_lite`
- `tsi_score_lite`
- `xg_gap_proxy_lite`
