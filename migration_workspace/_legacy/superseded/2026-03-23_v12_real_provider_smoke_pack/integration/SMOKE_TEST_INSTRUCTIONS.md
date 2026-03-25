# Smoke test instructions

## Execução
```bash
cd migration_workspace/v12/2026-03-23_v12_real_provider_smoke_pack
python motor/smoke_test.py
```

## Esperado
- 1 payload central consumido
- 3 candidatos gerados (`O15_TEAM`, `O15_GAME`, `U35`)
- outputs em schema `market_pick.v1.1`
- `data_quality_flag` coerente

## Falha crítica
- missing root keys
- `fixture_id` mismatch
- output sem campo obrigatório do contrato
