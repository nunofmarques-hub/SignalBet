# SBO OR8 — Real Rehearsal Pack

Pack oficial de staging da frente App Core / Orchestrator.

## Objetivo desta ronda
Empurrar o Orchestrator de demo forte para ensaio real de coordenação:
- ligação mais apontável ao `project_root` físico
- procura de feeds reais dos módulos antes do fallback demo
- `validation_run` mais próximo do pipeline verdadeiro
- `run_summary` e `ui_status` mais maduros para o futuro botão `Pôr tudo a correr`

## Estado
staging transversal muito forte / ensaio real inicial

## Como correr
```bash
python run_smoke.py
```

## Nota de honestidade técnica
O pack continua a distinguir explicitamente entre:
- modo demo
- ligação ao tronco físico real

Não sugere integração real antes de ela estar provada.
