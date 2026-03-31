# Nullability rules

- `result = null` quando ainda não há resultado final.
- `pnl = null` quando ainda não há settlement final.
- `pnl = 0.0` só deve ser usado quando existe fecho real com impacto líquido zero.
- Ausência de settlement nunca deve ser representada por `0.0`.
