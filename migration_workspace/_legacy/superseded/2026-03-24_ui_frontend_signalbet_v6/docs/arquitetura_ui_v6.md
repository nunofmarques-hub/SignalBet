# Arquitetura UI v6

## Objetivo
Elevar a frente UI de shell navegável forte para base visual séria da app principal SignalBet.

## Melhorias do v6
- App shell mais real e mais coeso
- Painel visual do botão/orchestrator integrado na shell
- Estados transversais `loading / empty / error / success` por ecrã
- Estrutura de componentes mais clara
- Melhor representação do pipeline do sistema
- Logo como asset SVG dedicado no pack

## Ecrãs incluídos
- Home / Dashboard
- Opportunity Pool
- Banca / Decision View
- Execution / Tracking
- Histórico / Validação

## Pipeline visual representado
Data/API → módulos → GPS → banca → execution → histórico

## Nota
A coordenação técnica da corrida continua fora da UI. Este pack apenas prepara a camada visual e os estados de apresentação do orquestrador.
