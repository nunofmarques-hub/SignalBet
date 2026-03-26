# Output stability rules

O output é considerado estável quando:
- `schema_version` permanece `market_pick.v1.1`
- `module_id` permanece `v12`
- enums principais não variam
- `module_specific_payload.motor_id` e `market_variant` mantêm naming canónico
- campos obrigatórios nunca desaparecem entre runs

Mudanças futuras devem ser versionadas em `module_version` ou `schema_version`, nunca por drift silencioso.
