# BTTS — Handoff curto para Orchestrator

## Ficheiro principal
Usa este ficheiro como **payload curto do BTTS para o Orchestrator**:

- `BTTS_latest_game_cards_phase1.json`

## Onde colar no pack BTTS
A ordem mais limpa é esta:

1. **Se o pack já tem `latest.json`**
   - substituir o conteúdo atual do `latest.json` por este envelope
   - ou copiar o bloco `game_cards` para dentro do `latest.json` oficial, se esse ficheiro já tiver envelope maior controlado pela tua linha

2. **Se o pack tem pasta de sample output / exemplo parseável**
   - copiar também este mesmo conteúdo para um ficheiro de exemplo
   - nome sugerido: `sample_game_cards_phase1.json`

3. **Se existe ficheiro de handoff ao Orchestrator**
   - referenciar este JSON como output curto oficial do BTTS para a app fase 1

## Onde NÃO colar
Não meter este bloco:
- em ficheiros internos do motor
- em ficheiros de fórmula / cálculo
- em documentação conceptual
- em output rico com odd justa, edge ou blocos internos

## Regra funcional
Este payload serve apenas para:
- `game_cards` curtos
- leitura de oportunidade BTTS
- consumo pelo Orchestrator
- fase 1 da app

## Campos entregues
- `pick_id`
- `fixture_id`
- `match_label`
- `module_name`
- `market_family`
- `market_code`
- `selection_label`
- `raw_module_score`
- `score_band`
- `eligibility`
- `candidate_status`
- `rationale_short`
- `risk_flags`

## Campos que não seguem nesta ronda
- odd justa
- edge final
- blocos internos do motor

## Formulação curta
O BTTS entrega ao Orchestrator `game_cards` curtos e estáveis para a app fase 1, sem profundidade excessiva e sem expor a camada interna do motor.
