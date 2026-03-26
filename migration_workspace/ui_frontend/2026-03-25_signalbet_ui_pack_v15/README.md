# UI Frontend SignalBet v15

## Objetivo
Pack de staging da frente UI / Frontend focado em clarificar a bridge real já provada no v14 e preparar a expansão controlada da leitura real.

## Estado do pack
staging_forte

## O que este pack faz
- clarifica o que entra por ponte real
- clarifica o que continua mock
- formaliza os limites da bridge atual
- define próximos passos para ampliar leitura real sem perder controlo
- reforça a UI com metadata visível sobre source mode, source observed, fallback e bridge status

## Dependências
- Browser moderno para abrir `src/index.html`
- Não depende de backend live nesta fase

## Ponto de entrada
- `src/index.html`

## Ponto de saída
- UI navegável com Home, Opportunity Pool, Banca, Execution e Histórico
- Painel “Pôr tudo a correr” com leitura explícita da bridge

## Contrato
Este pack mantém alinhamento com o contrato operacional comum e com a leitura do Orchestrator já provada em staging forte.

## Leitura de dados
- modo real protegido via import de snapshot JSON externo
- fallback limpo para `orchestrator_mock`
- sem ligação live automática nesta fase

## O que já é real
- leitura externa controlada de snapshot JSON
- normalização protegida via `orchestratorAdapters.js`
- bridge com metadata de origem observada

## O que continua mock
- `contract_mock`
- `orchestrator_mock`
- `placeholder_live`

## O que bloqueia live completa
- ausência de adapter/live source oficial entregue à frente UI
- necessidade de handshake controlado com o Orchestrator real
