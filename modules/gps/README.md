# GPS — Clean Integral Replacement Pack

## objetivo do pack
Substituição integral limpa da linha ativa do módulo GPS / Global Pick Selector, pronta para ocupar `modules/gps/`.

## estado do pack
pronto_para_substituicao_integral_limpa

## linha oficial ativa
- GPS v6 clean line

## o que este pack substitui
- a linha viva atual fragmentada em staging / packs intermédios do GPS
- a necessidade de competir visualmente entre versões antigas do GPS

## o que passa a ser a linha ativa
- o conteúdo deste pack em `modules/gps/`

## o que sai da pasta viva
- packs intermédios do GPS
- variantes antigas já absorvidas
- staging que compita com a linha ativa

## o que vai para arquivo / histórico / legacy
- versões anteriores do GPS tratadas como superseded
- packs de maturação, handoff e correções já ultrapassados
- artefactos transitórios antigos sem papel operacional atual

## conteúdo principal desta linha
- batch multi-módulo estável
- normalização robusta
- ranking auditável
- contrato GPS -> banca congelado nesta fase
- export app phase 1 do bloco shortlist em leitura de produto

## runner oficial desta fase
- `run_smoke.py`

## docs e contratos congelados nesta fase
- `docs/`
- `contracts/`

## nota curta final
frente pronta para substituição integral limpa
