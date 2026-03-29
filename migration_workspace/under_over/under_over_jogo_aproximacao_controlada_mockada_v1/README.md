# Under/Over Jogo — Aproximação Controlada Mockada ao Corredor Protegido v1
## SignalBet / ABC PRO

**Frente:** Under/Over Jogo  
**Estado:** staging forte offline bem disciplinado  
**Objetivo desta ronda:** provar consumo mockado do formato futuro, sem integração real  
**Relação com a v12:** v12 mantém-se como linha operacional válida da fase atual

## O que este pack faz
Este pack mostra, de forma controlada e local, como a frente consumiria um payload protegido no futuro.

Inclui:
- adapter local
- input protegido mockado
- output final emitido via adapter
- semântica curta de degradação

## Estrutura
- `src/run_mock_adapter_under_over_jogo.py`
- `examples/inputs/`
- `examples/outputs/`
- `contracts/`
- `docs/`
- `run_mock_adapter_under_over_jogo.cmd`

## Casos incluídos
- `input_ready_mock.json` → caso pronto
- `input_degraded_mock.json` → caso sem odds, com `degraded_run`
- `input_hard_fail_mock.json` → caso com falta crítica, `hard_fail`

## Como correr
1. abrir a pasta
2. executar `run_mock_adapter_under_over_jogo.cmd`
3. verificar os outputs em `examples/outputs/`

## O que ainda não faz
- integração real
- consumo do Orchestrator live
- trunk direto
- consumo por GPS/Banca
- promoção da frente para linha integrada
