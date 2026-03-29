# v12 — runtime fix contract

## Objetivo
Resolver a derivação de `league_id` no bundle protegido sem nesting rígido e sem erro bruto.

## Regra de derivação de `league_id`
A normalização tenta, por esta ordem:

1. `league_id`
2. `fixture.league_id`
3. `fixture.league.id`
4. `bundle.league_id`
5. `bundle.fixture.league_id`
6. `bundle.fixture.league.id`
7. `context.league_id`
8. `match_context.league_id`

Se nenhuma fonte existir:
- devolver `hard_fail`
- mensagem curta e auditável
- nunca lançar `KeyError` bruto

## Campos críticos mínimos
- `fixture_id`
- `league_id`
- `season`
- `home_team_id`
- `away_team_id`
- `source_mode`
- `observed_mode`
- `readiness_level`
- `provider_name`
- `provider_source`
- `input_profile`
