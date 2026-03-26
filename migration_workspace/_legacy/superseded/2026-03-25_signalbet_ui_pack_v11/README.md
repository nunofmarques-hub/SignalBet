# UI Frontend SignalBet v11

## Objetivo
Pack de continuação da frente UI / Frontend, focado em aproximar a camada visual dos snapshots e estados reais do Orchestrator, sem fingir integração real.

## Estado
staging_forte

## Conteúdo principal
- app shell navegável
- serviços de snapshot/pipeline mais próximos do runtime provado
- adapters mais próximos do output do Orchestrator
- view models alinhados com summary, module overview, pipeline steps, counts e button context
- painel visual oficial do botão “Pôr tudo a correr”

## Dependências
- contratos transversais do sistema
- estados e snapshots do Orchestrator (ainda mockados neste pack)
- Data_API_Official_Trunk_v1 como referência estrutural de dados

## Ponto de entrada
- `src/index.html`

## Ponto de saída
- shell navegável de frontend em staging

## Contrato
- referência operacional ao contrato v1.1

## Data/API Layer
Este pack não lê diretamente do trunk oficial. Usa adapters e services preparados para futura substituição por fontes reais.
