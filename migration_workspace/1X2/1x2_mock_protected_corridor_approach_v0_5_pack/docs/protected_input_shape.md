# Protected Input Shape — Mock v0.5

## Objetivo
Definir a shape futura mínima de input protegido que a frente 1X2 espera consumir
numa aproximação controlada mockada ao corredor protegido.

## Envelope mínimo proposto

```json
{
  "source_line": "OR_protected_mock",
  "runtime_profile": "protected_mock",
  "readiness_level": "mock_ready",
  "protected_match_context": {
    "fixture_id": 100001,
    "league_id": 140,
    "season": 2024,
    "home_team": {"id": 501, "name": "Team A"},
    "away_team": {"id": 502, "name": "Team B"}
  },
  "protected_market_context": {
    "odd_home": 1.78,
    "odd_draw": 3.45,
    "odd_away": 4.90
  },
  "protected_team_strength_context": {
    "home_attack_rating": 1.65,
    "home_defense_rating": 0.92,
    "away_attack_rating": 0.88,
    "away_defense_rating": 1.41
  },
  "protected_form_context": {
    "home_form_points_last5": 11,
    "away_form_points_last5": 4
  },
  "protected_risk_context": {
    "market_warning_flag": false,
    "injury_noise_flag": false,
    "rotation_noise_flag": false
  }
}
```

## Regra desta ronda
Esta shape é **mockada e protegida**. Não prova ligação real, apenas compatibilidade futura.
