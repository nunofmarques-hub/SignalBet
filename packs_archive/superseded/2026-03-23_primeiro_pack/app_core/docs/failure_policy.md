# Política de falhas

## Aborta corrida
- falta `api.env.txt`
- falta API key
- `data_api/` indisponível
- GPS indisponível em `daily_run`
- Banca indisponível em `daily_run`
- Execution indisponível quando `dry_run=false`

## Permite corrida com warning
- módulo opcional indisponível
- snapshot não mais recente, mas utilizável
- provider secundário ausente
- módulo disabled por maturidade

## Permite skip controlado
- BTTS e Corners fora do ar, desde que o núcleo principal esteja operacional
