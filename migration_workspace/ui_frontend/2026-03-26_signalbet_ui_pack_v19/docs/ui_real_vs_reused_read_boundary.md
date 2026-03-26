# UI Real vs Reused Read Boundary

## Objetivo
Tornar explícita a fronteira entre:
- nova leitura protegida
- snapshot reutilizado
- fallback mock

## Sinais visuais expostos pela UI
- `observed_mode`
- `snapshot_reused`
- `freshness_state`
- `fallback_used`
- `bridge_decision_reason`

## Interpretação
- nova leitura protegida: `observed_mode=real_read_protected` e `snapshot_reused=false`
- snapshot reutilizado: `observed_mode=real_read_protected` e `snapshot_reused=true`
- fallback mock: `observed_mode=orchestrator_mock`
