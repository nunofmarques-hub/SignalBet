# Normalization Matrix v2

## princípio
Raw e normalized coexistem sempre. O módulo mantém ownership dos campos raw; o GPS traduz para a linguagem comparável oficial.

## score_raw -> global_score
### v12
- escala esperada: 0–100
- tradução: direta

### corners
- escala esperada: 0–100
- tradução: direta

### btts
- escala esperada: 0–10 ou 0–100
- tradução:
  - <=10 -> multiplicar por 10
  - >10 -> tratar como 0–100

### cards
- escala esperada: 0–100
- tradução: direta

## confidence_raw -> confidence_norm
### texto
- muito baixa -> 1
- baixa -> 2
- média -> 3
- alta -> 4
- muito alta -> 5

### número 0–100
- 0–24 -> 1
- 25–44 -> 2
- 45–64 -> 3
- 65–84 -> 4
- 85–100 -> 5

### número 1–5
- manter dentro do range

## risk_raw -> risk_norm
Mesmo mapa da confiança, mas semântica invertida no ranking:
- 1 = muito baixo
- 5 = muito alto

## edge_raw -> edge_norm
### percentagem
- <3 -> weak
- 3 a <6 -> acceptable
- 6 a <10 -> strong
- >=10 -> very_strong

### texto
- weak
- acceptable
- strong
- very_strong

## ajustamentos automáticos
- data_quality partial -> -4
- data_quality fragile -> -9
- data_quality invalid -> bloqueio
- edge_missing -> -2
- rationale fraco -> -1
- payload incompleto -> -1 a -3
