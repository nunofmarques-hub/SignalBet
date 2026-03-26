# Integration Notes BTTS

## Situação atual
O módulo BTTS já tem:
- motor conceptual fechado
- grelha matemática
- output formal alinhado com `market_pick.v1.1`
- testes autónomos por bloco
- bateria de validação do motor completo
- primeira validação semi-real e rolling

## O que ainda não deve ser assumido como final
- cobertura total da API-Football para shots/statistics/odds
- xG real consistente
- export em produção para a Opportunity Pool
- integração plena em `modules/`

## Regra operacional
Enquanto a camada de API estiver em evolução, o módulo deve continuar em `estado: teste` e a migração deve acontecer por packs controlados.

## Critério para passar a staging
- match master preenchido com coverage suficiente
- team profiles rolling pré-jogo sem leakage
- exporter `market_pick.v1.1` validado em fixtures reais
- 1 battery validation + 1 semi-real run coerentes
