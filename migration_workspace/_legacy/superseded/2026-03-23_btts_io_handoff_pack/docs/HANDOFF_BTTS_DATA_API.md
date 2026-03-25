# HANDOFF BTTS -> Data/API Layer

## O que o BTTS espera receber
Um payload central por jogo com:
- identificação do evento
- contexto competitivo
- odds pré-jogo
- snapshot de liga
- snapshot do mandante
- snapshot do visitante
- metadata de qualidade e fontes

## Campos mínimos para a v1 robusta
- `event_id`
- `kickoff_datetime`
- `competition.league_id`
- `competition.season`
- `match.home_team_id`, `match.away_team_id`
- `market_context.btts_yes_odds`
- `home_snapshot.goals_for_90`
- `home_snapshot.goals_against_90`
- `home_snapshot.score_rate_1plus`
- `home_snapshot.concede_rate_1plus`
- `away_snapshot.goals_for_90`
- `away_snapshot.goals_against_90`
- `away_snapshot.score_rate_1plus`
- `away_snapshot.concede_rate_1plus`

## Reforço desejável
- shots on target
- métricas recentes
- timing do primeiro golo
- proxies de estabilidade
- xG proxy
