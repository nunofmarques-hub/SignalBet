# Nota Curta de Handoff Local Simulado

## O que este handoff simula
Este pack simula, localmente, o comportamento futuro da frente Under/Over Jogo quando receber uma shape protegida do corredor.

## O que entra
- payload protegido mockado
- metadata mínima de proveniência
- bloco `protected_match_context`
- opcionalmente odds

## O que o adapter faz
- valida campos críticos
- decide `ready`, `degraded_run` ou `hard_fail`
- adapta para o modelo local
- emite output final da frente

## O que sai
- `runtime_state`
- `base_state`
- `results` por linha
- metadata mínima de proveniência

## Leitura disciplinada
Isto ainda não é handoff real de corredor.
É apenas prova local de que a frente já sabe consumir e emitir no formato futuro esperado.
