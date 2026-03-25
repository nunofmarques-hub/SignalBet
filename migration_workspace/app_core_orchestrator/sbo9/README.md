# SBO OR9 — Real Proof Pack

Estado: staging transversal muito forte / prova real preparada

## Objetivo
Empurrar o App Core / Orchestrator de ensaio real convincente para prova real preparada da corrida global da app.

## O que sobe nesta ronda
- prioridade total a `project_root` real por request, variável `SIGNALBET_PROJECT_ROOT` ou `examples/req/project_root.txt`
- novo perfil `validation_run_proof`
- gates estritos para `project_root` real e feeds reais
- `run_summary` com `readiness_level`
- `ui_status` com `cta_state` mais maduro (`ready_rehearsal`, `ready_partial`, `ready_live`, `blocked`)
- `run_real_proof.py` para correr a prova real apontando a uma árvore física

## Como correr
Smoke demo:
`python run_smoke.py`

Prova real:
`python run_real_proof.py C:\SB`

ou definir `examples/req/project_root.txt`.

## Regra de honestidade
Se o `project_root` real não existir ou não tiver feeds reais detetados, a prova real falha e o pack não mascara sucesso.
