# Handoff curto — substituição integral da pasta ativa UI

## Ação
Substituir integralmente a pasta ativa atual da frente UI por esta pasta.

## Foco desta atualização
- home principal mantida e limpa
- detalhe curto de jogo materializado como ecrã real
- ligação shortlist → detalhe já funcional
- limpeza da linha ativa
- remoção de redundâncias e ficheiros ultrapassados

## Onde entra o que foi pedido
### Detalhe curto de jogo
No `src/index.html`:
- abre por clique direto no item da shortlist
- chave do jogo: `fixture_id`
- chave da pick ativa: `pick_id`
- ecrã mostra:
  - cabeçalho do jogo
  - pick principal
  - game_cards do mesmo jogo
  - banca curta da pick ativa
  - tracking curto da pick ativa
  - botão `Voltar à shortlist`

## O que fica fora
- novo payload
- tabs ricas
- modal pesado
- redesign geral
- estatística rica
- tracking longo
- policy profunda da banca

## Estado final
Detalhe curto materializado com sucesso.
