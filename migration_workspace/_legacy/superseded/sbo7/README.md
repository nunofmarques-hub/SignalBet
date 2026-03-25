# 2026-03-24_sbo_or7_pointable_core_pack

## Objetivo do pack
Evoluir o App Core / Orchestrator de coordenação forte em staging para base real e apontável da corrida global da app.

## Estado do pack
staging

## Frente
App Core / Orchestrator

## Missão
Coordenar a corrida técnica do sistema: config/environment check, readiness da Data/API, discovery de módulos, corrida dos módulos, envio ao GPS, envio à Banca, registo na Execution e resumo final para UI / logs / audit.

## Dependências
- Data_API_Official_Trunk_v1
- outputs reais de módulos quando existirem
- bridges draft para GPS, Banca e Execution

## Provider oficial
- provider_type: official_trunk
- provider_name: Data_API_Official_Trunk_v1
- provider_object: providers/contracts/services/storage + module feeds

## Entrada
- run_smoke.py
- src/app_orch/launcher/run_val.py

## Saída
- out/last_health.json
- out/last_sum.json
- out/last_ui.json

## Como correr o smoke test
```bash
python run_smoke.py
```

Para apontar ao teu projeto real:
```bash
set SIGNALBET_PROJECT_ROOT=C:\SB\meu_projeto
python run_smoke.py
```

Também podes preencher `examples/req/project_root.txt`.

## O que esta ronda acrescenta
- prioridade a project_root real antes do fallback demo
- resumo com origem dos feeds por módulo
- pipeline steps para UI/logs/audit
- distinção explícita entre modo demo e modo real
- payload mais próximo do botão “Pôr tudo a correr”

## Notas finais
Este pack tenta primeiro um `project_root` real. Se não encontrar uma árvore válida com `data_api/`, cai para o projeto demo do próprio pack. Essa distinção fica explícita no `run_summary` e no `ui_status`.
