# Under/Over Jogo — Protótipo Offline Forte
## SignalBet / ABC PRO

**Frente:** Under/Over Jogo  
**Estado:** protótipo offline forte desta fase  
**Relação com a v12:** v12 mantém-se como linha operacional válida da fase atual

## Objetivo
Transformar a baseline offline atual numa frente repetível, comparável e tecnicamente mais limpa, sem integração real.

## Estrutura
- `src/` lógica do runner offline
- `examples/inputs/` cenários mockados fixos
- `examples/outputs/` outputs versionados gerados pelo runner
- `docs/` documentação mínima local
- `run_under_over_jogo_offline.cmd` launcher local

## Cenários incluídos
- `cenario_controlado`
- `cenario_intermedio_2_3`
- `cenario_explosivo`

## Como correr
1. Abrir a pasta do pack
2. Executar `run_under_over_jogo_offline.cmd`
3. Ver os resultados no terminal
4. Consultar os ficheiros em `examples/outputs/`

## O que o runner faz
- lê inputs mockados fixos
- calcula `OU_Base_Score`
- calcula `lambda_match`
- avalia linhas
- aplica coerência familiar
- grava output JSON por cenário

## Output gerado
Cada cenário gera um JSON versionado com:
- `module_name`
- `module_version`
- `scenario_name`
- `base_state`
- `results` por linha

## O que ainda não cobre
- integração real
- corredor protegido
- trunk/provider live
- consumo downstream real
- promoção automática da frente

## Regra congelada importante
No cenário intermédio atual:
- `Over 1.5 = rejected`
- `Over 2.5 = rejected`

Isto mantém o corredor 2–3 como conservador por regra do modelo atual.
