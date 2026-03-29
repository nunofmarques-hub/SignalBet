# Under/Over Jogo — Mini Fluxo Ponta a Ponta Local v1
## SignalBet / ABC PRO

**Frente:** Under/Over Jogo  
**Estado:** staging forte offline bem disciplinado  
**Objetivo desta ronda:** provar localmente o handoff futuro simulado, sem integração real  
**Relação com a v12:** v12 mantém-se como linha operacional válida da fase atual

## O que este pack prova
Este pack mostra um mini fluxo ponta a ponta local:

- input protegido mockado
- adapter local
- output final emitido
- handoff local simulado

## Fluxo
`input protegido mockado -> adapter local -> output final`

## Casos incluídos
- `ready`
- `degraded_run`
- `hard_fail`

## Como correr
1. abrir a pasta
2. executar `run_local_handoff_under_over_jogo.cmd`
3. consultar o terminal
4. abrir os JSONs em `examples/outputs/`

## O que ainda não é
- integração real
- consumo live do Orchestrator
- corredor real
- handoff downstream real para GPS/Banca
