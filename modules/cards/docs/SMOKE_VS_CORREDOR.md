# SMOKE VS CORREDOR — Cards

## smoke técnico local
Execução curta do módulo para validar runtime, imports, package layout e integridade mínima do output.

## smoke contratual
Execução de `run_smoke.py --mode contract-smoke` para provar que o provider oficial resolve, o pipeline curto corre limpo e o output é validável segundo o contrato do módulo.

## runner mínimo de corredor nesta fase
Para a frente Cards, o runner oficial desta fase é `run_smoke.py`. Serve para confirmar o módulo de forma disciplinada antes da run final de corredor.

## o que não deve ser usado como entrypoint oficial nesta ronda
- `run_demo.py`
- chamadas ad hoc a partir de notebooks ou shells sem bootstrap
- imports manuais dependentes do diretório corrente

## distinção operacional
- `run_smoke.py` = runner oficial desta fase
- `run_demo.py` = demo/local, não runner oficial do corredor
