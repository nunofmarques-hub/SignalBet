# Normalization Matrix v4

## score_raw -> global_score
- v12: 0–100 direto
- corners: 0–100 direto
- btts: <=10 multiplicar por 10; >10 tratar como 0–100
- cards: 0–100 direto

## confidence_raw / risk_raw
- texto muito baixa..muito alta -> 1..5
- numérico 0–100 -> bandas 1..5
- numérico 1–5 -> manter

## edge_raw -> edge_norm
- <3 weak
- 3 a <6 acceptable
- 6 a <10 strong
- >=10 very_strong
