# Mini-contrato de adaptação — v0.5

## Função
Transformar `protected_*` contexts do payload mockado em input interno estável do 1X2.

## Mapeamento mínimo

- `protected_match_context.fixture_id` -> `fixture_id`
- `protected_match_context.league_id` -> `league_id`
- `protected_match_context.season` -> `season`
- `protected_match_context.home_team.id` -> `home_team_id`
- `protected_match_context.away_team.id` -> `away_team_id`
- `protected_match_context.home_team.name` -> `home_team_name`
- `protected_match_context.away_team.name` -> `away_team_name`

- `protected_market_context.odd_home` -> `odd_home`
- `protected_market_context.odd_draw` -> `odd_draw`
- `protected_market_context.odd_away` -> `odd_away`

- `protected_team_strength_context.home_attack_rating` -> `home_attack_rating`
- `protected_team_strength_context.home_defense_rating` -> `home_defense_rating`
- `protected_team_strength_context.away_attack_rating` -> `away_attack_rating`
- `protected_team_strength_context.away_defense_rating` -> `away_defense_rating`

- `protected_form_context.home_form_points_last5` -> `home_form_points_last5`
- `protected_form_context.away_form_points_last5` -> `away_form_points_last5`

- `protected_risk_context.*` -> flags internas de risco

## Estados semânticos
- `input_status`: ok | hard_fail
- `adaptation_status`: adapted_ok | adapted_with_defaults | adaptation_fail
- `run_status`: success | runtime_fail
- `decision_status`: primary_decision | degraded_decision | rejected_decision
- `candidate_status`: candidate | watchlist | rejected
