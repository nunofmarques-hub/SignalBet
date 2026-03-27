# SBO OR9U1 — Discovery Rule Freeze Update Pack

Estado: staging transversal muito forte / prova real preparada

## Objetivo
Congelar a regra oficial de discovery do Orchestrator nesta fase e remover a ambiguidade de path na prova real.

## O que sobe neste update curto
- `integration_feeds/<module>/latest.json` passa a ter prioridade máxima
- `integration_feeds/<module>/<module>_output.json`, `module_output.json` e `output.json` passam a ser caminhos oficiais secundários do mesmo bloco `integration_feeds/`
- `examples/`, outputs antigos e scans recursivos passam a ficar explicitamente como fallback
- classificação de `output_invalid` e `output_missing` alinhada com a nota operacional
- sem alteração do objetivo central do OR9: prova real preparada, sem mascarar sucesso

## Precedência oficial de discovery
1. `integration_feeds/<module>/latest.json`
2. `integration_feeds/<module>/<module>_output.json`
3. `integration_feeds/<module>/module_output.json`
4. `integration_feeds/<module>/output.json`

Só depois entram fallbacks secundários:
- `runtime/mod_out/<module>/...`
- `mod_out/<module>/...`
- `migration_workspace/<module>/...`
- `modules/<module>/out/...`
- `modules/<module>/examples/...`
- scans recursivos nesses blocos

## Como correr
Smoke demo:
`python run_smoke.py`

Prova real:
`python run_real_proof.py C:\SB`

ou definir `examples/req/project_root.txt`.

## Regra de honestidade
Se o `project_root` real não existir ou não tiver feeds reais válidos detetados, a prova real falha e o pack não mascara sucesso.


## Update OR9u2
A discovery rule foi congelada com `integration_feeds/<module>/latest.json` em prioridade máxima. Os scans recursivos só entram depois de todos os paths diretos, e `examples/` fica explicitamente como fallback tardio.
