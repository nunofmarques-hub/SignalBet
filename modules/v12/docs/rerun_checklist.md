# Rerun checklist

- confirmar que `runtime_inputs/protected_runtime_payload.json` existe
- correr `python motor/smoke_test.py`
- verificar que `examples/runtime_fix_summary.json` foi gerado
- confirmar `v12_runtime_fix = OK`
- confirmar presença de `league_id`
- só depois voltar ao shadow run ponta a ponta
