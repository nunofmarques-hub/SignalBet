# UI / Frontend — Official Live Line Final

## Estado
Linha oficial viva da frente UI / Frontend.

## Objetivo
Fechar a base visual e funcional da App Phase 1 e da evolução curta já validada, sem reabrir arquitetura nem voltar a staging prolongado.

## Esta linha inclui
- `src/index.html` final consolidado
- tracking final coerente
- `recent_closed_cases`
- empty state correto
- metadata curta do caso ativo
- leitura estável de caso ativo, banca curta, tracking curto e bloco secundário

## Runner oficial
- `run_smoke.bat`

## Upstream oficial
- Orchestrator / App Core

## Conteúdo da linha viva
- `src/`
- `runtime_outputs/app_phase1_protected_payload.json`
- `README.md`
- `manifest.json`
- `run_smoke.bat`
- `run_smoke.sh`
- `docs/`
- `pack_check_report.txt`
- `UI_CHAT_MEMORY_CURRENT.md`
- `tests/`

## O que este pack substitui
Substitui integralmente a linha ativa anterior com payloads de teste antigos, cmd transitórios, backups, docs redundantes e artefactos já absorvidos.

## Destino físico pretendido
- `modules/ui_frontend/`

## Nota final
Esta pasta deve passar a ser a base oficial viva da frente UI / Frontend.
