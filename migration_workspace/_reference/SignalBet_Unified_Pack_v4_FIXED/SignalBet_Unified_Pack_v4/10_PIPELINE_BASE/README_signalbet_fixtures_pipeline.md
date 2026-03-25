# Mini pipeline API-Football — SignalBet / ABC PRO

Este mini programa foi desenhado para o módulo de cantos.

## Objetivo
1. Descobrir fixtures por `league + season + status`
2. Extrair `fixture.id`
3. Criar cache local auditável
4. Enriquecer fixtures em batch via `fixtures?ids=...`
5. Validar estatísticas por `fixtures/statistics?fixture=...`

## Defaults já preparados
- League: `140` (LaLiga)
- Season: `2024`
- Status: `FT-AET-PEN`

## Pré-requisito
Na mesma pasta do script deve existir:
`api.env.txt`

Formato:
`API_KEY=coloca_aqui_a_tua_chave`

## Estrutura criada
O script cria:
`data_api_football/league_140/season_2024/...`

com:
- `catalog/`
- `raw/batches/`
- `raw/stats/`
- `masters/`
- `logs/`

## Comandos principais

### 1) Descobrir jogos concluídos e criar catálogo
```bash
python signalbet_fixtures_pipeline.py discover
```

### 2) Enriquecer em lotes via /fixtures?ids=
```bash
python signalbet_fixtures_pipeline.py hydrate-batches --chunk-size 20 --max-batches 3
```

### 3) Validar estatísticas em alguns jogos
```bash
python signalbet_fixtures_pipeline.py stats-probe --max-items 5
```

### 4) Fazer arranque rápido
```bash
python signalbet_fixtures_pipeline.py full-bootstrap
```

## Sequência recomendada
1. `discover`
2. `hydrate-batches`
3. `stats-probe`

## Decisão operacional incorporada
- Descoberta oficial: `/fixtures?league=...&season=...&status=FT-AET-PEN`
- Enriquecimento preferido: `/fixtures?ids=...`
- Fallback fino: `/fixtures/statistics?fixture=...`
- Cache local como base de trabalho
- Throttle conservador para plano Free
