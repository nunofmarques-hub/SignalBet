# Ponte UI v12 ↔ Orchestrator

## Shape mock atual
A UI consome um snapshot runtime com:
- metadata do run
- readiness
- summary
- módulos
- etapas da pipeline
- issues
- resultado final

## Shape real esperado
A expectativa é receber os mesmos blocos conceptuais, ainda que nomes internos possam variar.

## Diferenças ainda em aberto
- fonte live não ligada
- mapping final de issue severity pode mudar
- eventual split entre summary global e summary por etapa

## Resultado desta ronda
A UI fica preparada para trocar `orchestrator_mock` por `placeholder_live` com o mínimo de alteração estrutural.
