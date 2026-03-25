# Data requirements — v12

## Núcleo ativo
- Over 1.5 equipa
- Over 1.5 jogo
- Under 3.5

## Blocos de dados esperados da Data/API Layer
- `fixture`
- `teams`
- `standings_context`
- `team_stats_season`
- `team_stats_recent`
- `league_market_profile`
- `odds_snapshot`
- `timing_profile`
- `scoreline_profile`
- `risk_flags`

## Campos críticos mínimos
- fixture_id, match_label, competition, kickoff_datetime
- team ids e nomes
- posição, pontos, goal difference, split casa/fora
- goals for/against per game, shots, shots on target, xG/xGA se disponível
- forma recente 3/5 jogos
- taxa histórica do mercado por liga
- odds do mercado no momento de geração
- flags de risco básicas

## Dependências analíticas principais
- FDI / TSI para `O15_TEAM`
- IPO combinado / TPD / TLI para `O15_GAME`
- ULI / LTR / LigaScore under / TLI para `U35`
