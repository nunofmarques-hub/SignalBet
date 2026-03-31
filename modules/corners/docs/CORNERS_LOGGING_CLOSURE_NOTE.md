# CORNERS_LOGGING_CLOSURE_NOTE

## causa real do STEP CMD vazio
O step do Corners executava com `run_smoke.py`, mas o comando explícito não estava congelado para eco no log.

## correção aplicada
Foi fixado o comando oficial desta fase como:
`python run_smoke.py`

## entrypoint oficial confirmado
- script: `run_smoke.py`
- comando: `python run_smoke.py`

## prova curta
- `STEP START: Modulo Corners`
- `STEP CMD  : python run_smoke.py`
- `STEP OK   : Modulo Corners`

## impacto
logging corrigido, sem regressão funcional no corredor.
