# Integration note

Este pack assume o contrato de input oficial vindo da Data/API Layer, com blocos:
- `market_context`
- `discipline_context`
- `referee_context`
- `quality_context`

O módulo Cards lê esse payload via provider explícito, normaliza para handoff interno e exporta output oficial `market_pick.v1.1`.
