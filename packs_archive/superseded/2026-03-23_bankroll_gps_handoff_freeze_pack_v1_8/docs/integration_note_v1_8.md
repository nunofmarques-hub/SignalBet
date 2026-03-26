# Integration Note v1.8

## missão
Fechar o consumo do payload do GPS do lado da Banca, mantendo intacta a linguagem comparável do seletor e devolvendo linguagem financeira/operacional para Execution.

## posição da banca
- não recalcula `global_score`, `confidence_norm`, `risk_norm`, `edge_norm`, `priority_tier`
- aplica fixture lock, limites, stake, cortes, bloqueios e ordem operacional
- devolve Schema de decisão e payload de intake para Execution

## diferença para packs anteriores
Este pack já usa como referência direta o batch do GPS entregue em staging e endurece o contrato de consumo do lado da Banca.
