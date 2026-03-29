# CORNERS_LOGGING_CLOSURE_NOTE

## causa real do STEP CMD vazio
O step do Corners estava a usar o entrypoint oficial `run_smoke.py`, mas o runner/logging não tinha uma string de comando congelada para ecoar. O step existia e corria, mas o campo `STEP CMD` ficava vazio porque o comando não estava explicitado como valor de display.

## correção aplicada
Foi congelado o comando oficial desta fase como `python run_smoke.py` e esse comando passou a ficar declarado de forma explícita no pack (`manifest.json`, `README.md`, `pack_check_report.txt`) e na prova curta de log.

## entrypoint oficial confirmado
- script oficial: `run_smoke.py`
- comando oficial: `python run_smoke.py`

## impacto
- logging corrigido
- sem regressão no corredor
