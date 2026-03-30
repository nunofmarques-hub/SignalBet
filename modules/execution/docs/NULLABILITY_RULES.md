# NULLABILITY_RULES — tracking_summary

## result
- `null` quando ainda não existe resultado final da pick.
- valores permitidos quando fechado: `WIN`, `LOSS`, `PUSH`, `VOID`, `HALF_WIN`, `HALF_LOSS`.

## pnl
- `null` quando ainda não existe settlement final.
- número quando a pick já está fechada.

## Regra de leitura
Não usar `0.0` para representar ausência de resultado.
`0.0` só deve aparecer quando existe settlement final e o P/L real é neutro.
