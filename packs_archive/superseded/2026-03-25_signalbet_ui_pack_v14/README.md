# UI Frontend — SignalBet v14

## Objetivo do pack
Primeira ponte real, parcial e protegida do lado UI para leitura de snapshots do Orchestrator, mantendo fallback limpo para `orchestrator_mock`.

## Estado do pack
staging_forte

## Objetivo operacional desta ronda
- endurecer o `runtimeBridgeService`
- introduzir um ponto de entrada controlado para leitura real via snapshot JSON
- manter fallback limpo para `orchestrator_mock`
- explicitar claramente o que é real, o que é mock e o que bloqueia ligação live completa
- alinhar estrutura, naming e staging com o repositório oficial SignalBet em `main`

## Dependências
- Browser moderno com suporte a ES Modules
- Execução local estática via `file://` ou servidor simples
- Não depende de trunk live nem de Orchestrator live nesta fase

## Ponto de entrada
- `src/index.html`

## Ponto de saída
- UI navegável com:
  - Home / Dashboard
  - Opportunity Pool
  - Banca / Decision View
  - Execution / Tracking
  - Histórico / Validação
  - painel "Pôr tudo a correr"
- Leitura de snapshot:
  - `orchestrator_mock`
  - `real_read_protected` via import manual de ficheiro JSON

## Contrato / runtime
Este pack continua a respeitar os campos e estados já alinhados com:
- contrato v1.1
- runtime metadata / observed vs declared
- Orchestrator snapshot shape esperado

## Leitura da Data/API Layer
A UI não consome diretamente a `Data_API_Official_Trunk_v1` como motor.
Usa:
- mock data contratualmente coerente
- snapshot importado manualmente como primeira leitura real controlada
A ligação live completa continua bloqueada pela ausência do adapter certo e do ponto de leitura controlado do runtime real.

## O que já é real
- capacidade de importar manualmente um snapshot JSON externo na UI
- validação mínima do shape do snapshot
- normalização via `orchestratorAdapters`
- observação explícita do source mode usado
- fallback limpo em caso de erro

## O que ainda é mock
- `contract_mock`
- `orchestrator_mock`
- provider `placeholder_live`

## O que bloqueia a live completa
- ausência de endpoint/runtime source oficial
- ausência de adapter live definitivo
- ausência de política final de fallback/live source selection validada pelo App Core / Orchestrator
