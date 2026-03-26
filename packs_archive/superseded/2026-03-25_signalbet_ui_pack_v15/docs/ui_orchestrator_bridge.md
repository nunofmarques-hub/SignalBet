# UI ↔ Orchestrator Bridge

O v15 mantém a disciplina do v14 e formaliza o perímetro da bridge.

## Requested vs observed
A UI expõe:
- requested mode
- observed mode
- fallback used
- bridge status

## Status possíveis
- `mock_only`
- `mock_runtime`
- `real_partial_protected`
