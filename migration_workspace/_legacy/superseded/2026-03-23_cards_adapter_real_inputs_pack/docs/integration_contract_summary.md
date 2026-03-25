# Integration Contract Summary

## Input esperado da Data/API Layer
- `fixture`
- `competition_context`
- `teams.home.discipline_profile`
- `teams.away.discipline_profile`
- `referee_profile`
- `market_snapshot`
- `data_quality`

## Output oficial do módulo
- `schema_version = market_pick.v1.1`
- payload base da Opportunity Pool
- `module_specific_payload` com leitura disciplinar/contextual
