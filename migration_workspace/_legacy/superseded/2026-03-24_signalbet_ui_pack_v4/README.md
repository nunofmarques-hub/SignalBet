# SignalBet UI Frontend Pack v4

## Objetivo do pack
Entregar uma base **navegável e implementável** da frente UI / Frontend do SignalBet, já alinhada com a arquitetura oficial do sistema e com a regra de **Pack Hygiene + Environment Discipline**.

## Estado do pack
`staging`

## Módulo / frente
`ui_frontend`

## Dependências
- Browser moderno (Chrome, Edge, Firefox)
- Sem backend obrigatório nesta fase
- Mock data local coerente com contratos transversais
- Preparado para futura ligação à `Data_API_Official_Trunk_v1`

## Ponto de entrada
- `src/index.html`

## Ponto de saída
- Shell navegável com 5 ecrãs:
  - Home / Dashboard
  - Opportunity Pool
  - Banca / Decision View
  - Execution / Tracking
  - Histórico / Validação

## Contrato
Este pack referencia o **Contrato Transversal de Integração v1.1 Operacional** através dos campos mockados apresentados na UI:
- `global_score`
- `confidence_norm`
- `edge_norm`
- `risk_norm`
- `priority_tier`
- `eligibility`
- `decision_status`
- `execution_status`
- `data_quality_flag`

## Ligação à Data/API Layer
Este pack **ainda não consome diretamente** a `Data_API_Official_Trunk_v1`.

Estado atual:
- dados mockados locais em `data/mock-data.js`
- estrutura dos payloads alinhada com a arquitetura oficial
- preparado para substituição futura por provider/adapter real

## Estrutura do pack
- `manifest.json`
- `run_smoke.sh`
- `run_smoke.bat`
- `pack_check_report.txt`
- `src/`
- `docs/`
- `examples/`
- `contracts/`

## Como correr
### Linux / macOS
```bash
./run_smoke.sh
```

### Windows
```bat
run_smoke.bat
```

Ou abrir diretamente `src/index.html` no browser.

## O que este pack já traz
- app shell real
- design system base utilizável
- componentes reutilizáveis simples
- 5 ecrãs navegáveis
- botão visual **"Pôr tudo a correr"** no App Shell
- representação mais clara do pipeline do sistema

## O que ainda falta
- ligação real à Data/API Layer oficial
- integração com App Core / Orchestrator
- estados loading/error/empty mais ricos
- asset final rigoroso do logo aprovado
