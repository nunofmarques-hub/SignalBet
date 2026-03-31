# UI / Frontend — linha ativa limpa

## Estado
Linha ativa limpa, preparada para substituir integralmente a pasta ativa da frente.

## O que foi feito
- limpeza de redundâncias, docs transitórias e ficheiros ultrapassados
- manutenção apenas dos artefactos úteis da linha ativa
- atualização do `src/index.html` para materialização visual forte da home e do detalhe curto de jogo
- preservação da regra de consumo: 1 payload protegido, vindo apenas do Orchestrator

## Estrutura mantida
- `src/index.html`
- `src/styles/main.css`
- `runtime_outputs/app_phase1_protected_payload.json`
- `run_smoke.bat`
- `run_smoke.sh`
- `manifest.json`
- `README.md`
- `docs/`
- `tests/`

## Limpeza aplicada
Removidos da linha ativa:
- `Antigos/`
- docs v25/v26 já absorvidas
- samples/mockups concorrentes
- notas intermédias redundantes
- contratos/notas já sem papel operacional atual
- lixo documental fora da linha viva

## Leitura final
Esta pasta deve substituir integralmente a pasta ativa atual da frente UI.
