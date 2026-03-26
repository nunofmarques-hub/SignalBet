# UI Frontend — SignalBet v12 Controlled Runtime Bridge Pack

## Objetivo do pack
Este pack faz a ponte entre a UI em staging forte e o runtime esperado do Orchestrator, sem fingir ligação live.

## Estado do pack
staging

## Objetivos desta ronda
- consolidar adapters do Orchestrator
- reduzir diferença entre mock snapshot e snapshot real esperado
- preparar ponto de entrada controlado para futura ligação live
- reforçar o painel visual “Pôr tudo a correr”
- manter disciplina estrutural sem reescrita pesada

## Dependências
- Contrato Transversal v1.1 Operacional
- Data_API_Official_Trunk_v1 (referência conceptual; não consumido diretamente neste pack)
- outputs esperados do App Core / Orchestrator (mockados nesta ronda)

## Ponto de entrada
- `src/index.html`

## Ponto de saída
- app shell navegável com 5 ecrãs
- painel do Orchestrator com estados normalizados
- camada de providers/adapters/services preparada para futura troca de fonte

## Contrato v1.1
A UI continua a trabalhar com payloads e snapshots coerentes com os campos nucleares do sistema:
- global_score
- confidence_norm
- edge_norm
- risk_norm
- priority_tier
- eligibility
- decision_status
- execution_status
- data_quality_flag

## Data/API Layer
Este pack não lê diretamente da Data/API Layer. Usa snapshots mockados alinhados com o formato esperado do Orchestrator e deixa explícita a ponte futura para fontes reais.

## Como correr
Abrir `src/index.html` no browser ou correr `run_smoke.bat` / `run_smoke.sh`.
