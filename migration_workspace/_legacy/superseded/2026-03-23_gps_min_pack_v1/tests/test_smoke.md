# Test Smoke

## objetivo
Validar leitura rápida do pack mínimo.

## checks manuais esperados
- schemas existem e abrem
- `schema_validator.py` valida obrigatórios, enums e tipos mínimos
- `normalization.py` converte raw para normalized
- `ranking.py` calcula `global_score`
- `priority_rules.py` atribui tier
- `flags.py` gera flags mínimas
- `exports_to_bankroll.py` gera payload formal para a banca
- examples mostram input/output coerente para v12, Corners e BTTS
