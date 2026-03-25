# Integração conceptual com UI

## A UI faz
- mostra o botão principal
- envia `run_request`
- mostra estado do sistema
- mostra resumo da última corrida
- mostra módulos corridos e ignorados
- mostra picks aprovadas e bloqueadas

## A UI não faz
- decidir ordem do pipeline
- decidir readiness
- descobrir módulos
- decidir tolerância a falhas

## Painel mínimo
- estado do ambiente
- estado da Data/API
- módulos disponíveis
- última corrida
- resumo da execução
- warnings e falhas bloqueantes
