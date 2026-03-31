# MEMORIA_OPERACIONAL_ATIVA_V12
## SignalBet / modules / v12

**frente:** v12  
**estado atual:** integrado  
**linha ativa:** limpa e pronta para substituição da pasta atual  
**upstream oficial nesta fase:** Orchestrator / App Core  
**modo de leitura:** corredor protegido / payload protegido  
**núcleo maduro ativo:** Over 1.5 equipa, Over 1.5 jogo, Under 3.5  
**data de atualização:** 2026-03-31

---

## papel atual
A v12 é um módulo analítico integrado do núcleo de golos e alimenta o bloco `game_cards` da app phase 1 com leitura curta, estável e comparável.

## o que entrega já
- latest.json ativo
- game_cards phase 1 curtos
- contrato curto de saída para Orchestrator
- exemplos parseáveis

## o que não entra nesta linha
- BTTS
- Over 2.5
- Under 2.5
- família Over/Under alargada
- profundidade analítica excessiva
- packs auxiliares antigos

## regra central
A v12 consome corredor protegido e não usa trunk direto nem provider direto dentro do módulo.

## estado operacional curto
- consumo protegido real já provado
- game_card v12 fechado
- linha apta para app phase 1

## próximo passo recomendado
consumo pelo Orchestrator no payload protegido único da app phase 1.
