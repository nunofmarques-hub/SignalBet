# Ligação ao project_root real

Esta ronda empurra o Orchestrator de demo forte para ensaio real de coordenação.

Prioridade de resolução do `project_root`:
1. `run_request.project_root`
2. variável `SIGNALBET_PROJECT_ROOT`
3. `examples/req/project_root.txt`
4. parent do pack
5. fallback demo do pack

Regras desta versão:
- não fingir integração real antes de ela existir
- quando `require_real_project_root=true`, o summary falha se cair em demo
- quando `require_real_module_feeds=true`, o summary falha se não detetar feeds de projeto
- `project_feed_coverage_ratio` resume a cobertura real detetada
