# UI Frontend SignalBet v13 — Controlled Read Bridge Pack

## Objetivo
Este pack evolui a frente UI / Frontend do SignalBet para um estado de **ponte controlada de leitura**.

Foco principal:
- endurecer `runtimeBridgeService.js`
- aproximar snapshots mockados do output real esperado do Orchestrator
- preparar uma primeira ligação controlada de leitura real, parcial e protegida
- manter a disciplina de staging sem fingir integração live completa

## Estado do pack
- **status:** staging_forte
- **provider_type:** ui_frontend_shell
- **contract_version:** v1.1

## O que existe
- app shell navegável
- 5 ecrãs navegáveis
- design system base utilizável
- providers, adapters, services, runtime bridge e view models
- painel visual “Pôr tudo a correr” com estados mais próximos do runtime
- modo `placeholder_live` protegido via `runtimeBridgeService.js`

## O que ainda não existe
- consumo live real do trunk
- consumo live real do Orchestrator
- autenticação / stack frontend definitiva

## Source modes suportados
- `contract_mock`
- `orchestrator_mock`
- `placeholder_live`

## Como correr
### Browser
Abrir `src/index.html`

### Smoke test
- Windows: `run_smoke.bat`
- Unix: `run_smoke.sh`

## Estrutura principal
- `src/` app shell e código UI
- `docs/` notas de arquitetura e ponte UI ↔ Orchestrator
- `contracts/` notas de contrato e campos
- `examples/` snapshots de exemplo
- `tests/` validação estrutural mínima

## Entrada e saída
- **ponto de entrada:** `src/index.html`
- **ponto de saída:** shell navegável com leitura mock/protegida do runtime

## Ligação à Data/API Layer / Orchestrator
Ainda não existe ligação real. Este pack prepara a troca futura por adapters/provedores reais sem reescrita pesada.
