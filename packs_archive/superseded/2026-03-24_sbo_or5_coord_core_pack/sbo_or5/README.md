# 2026-03-24_app_core_orchestrator_coordination_core_pack

## Objetivo do pack
Evoluir o App Core / Orchestrator de validation layer forte para camada real de coordenação da app. Esta ronda aproxima o `validation_run` do pipeline real: valida ambiente, confirma readiness do `Data_API_Official_Trunk_v1`, descobre módulos elegíveis, consome outputs reais quando existem por paths de projeto, corre GPS e Banca em draft, marca Execution como `SKIPPED` no profile de validação e devolve resumo final utilizável por UI, logs e auditoria.

## Estado do pack
`staging`

## Módulo / frente
App Core / Orchestrator

## Dependências
- Python 3.11+
- `data_api/Data_API_Official_Trunk_v1/`
- outputs JSON de módulos em paths de projeto ou fallback demo do pack

## Ponto de entrada
`run_smoke.py`

## Ponto de saída
- `out/last_health.json`
- `out/last_sum.json`
- `out/last_ui.json`
- `examples/out/sample_health.json`
- `examples/out/sample_sum.json`
- `examples/out/sample_ui.json`

## Ligação à Data/API Layer
Este pack trata o `Data_API_Official_Trunk_v1` como caminho oficial ativo. O `project_root` é resolvido por esta ordem:
1. `project_root` no pedido
2. variável `SIGNALBET_PROJECT_ROOT`
3. raiz deduzida pela posição do pack em `migration_workspace/`
4. fallback para `examples/project/`

No `project_root` resolvido, o Orchestrator valida `data_api/Data_API_Official_Trunk_v1/` e procura evidência mínima de `README.md`, `providers/providers.json`, `contracts/`, `services/` e `storage/`.

## Como correr o smoke test
Na raiz do pack:

```bash
python run_smoke.py
```

Para testar contra projeto real:

```bash
SIGNALBET_PROJECT_ROOT=/caminho/do/projeto python run_smoke.py
```

## Notas finais
- O botão “Pôr tudo a correr” pertence visualmente à UI; a coordenação técnica pertence ao Orchestrator.
- O fluxo segue a ordem oficial: config/environment, readiness da Data/API, discovery, corrida dos módulos, GPS, Banca, Execution, resumo final.
- O `validation_run` identifica explicitamente `modules_eligible`, `modules_run`, `modules_skipped` e `modules_failed`.
- Quando o projeto real não está montado, o pack usa `examples/project/` sem fingir integração já provada fora do pack.
