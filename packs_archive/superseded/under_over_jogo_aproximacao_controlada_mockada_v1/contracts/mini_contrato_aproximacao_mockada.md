# Mini-Contrato de Aproximação Controlada Mockada

## Input protegido mockado mínimo
Campos críticos:
- `fixture_id`
- `league_id`
- `season`
- `home_team_id`
- `away_team_id`
- `provider_name`
- `provider_source`
- `protected_match_context`

Bloco `protected_match_context` crítico:
- `lambda_league`
- `GPI_M`
- `DRI_M`
- `OPI_M`
- `NRI_M`
- `AttackAdj`
- `DefenseAdj`
- `PaceAdj`
- `RiskAdj`

## Output emitido via adapter
- `module_name`
- `module_version`
- `runtime_state`
- `fixture_id`
- `provider_name`
- `provider_source`
- `input_profile`
- `base_state`
- `results` por linha

## Política desta ronda
- sem integração real
- sem trunk
- sem provider live
- apenas consumo mockado do formato futuro
