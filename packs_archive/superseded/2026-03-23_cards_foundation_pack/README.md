# Cards migration pack

## Objetivo do pack
Entregar um pack modular de teste do módulo **Cartões** para migração controlada em `migration_workspace/cards/...`, cobrindo indicadores, estrutura do motor, output contratual e documentação operacional.

## Ficheiros principais
- `src/cards_module/` — esqueleto técnico-base do módulo Cartões v1
- `indicators/Cartoes_v1_Quadro_Tecnico_Indicadores_Scoring_Elegibilidade.pdf`
- `indicators/Cartoes_v1_Matriz_Implementacao_Executavel.pdf`
- `engine_structure/Cartoes_v1_Schema_Tecnico_Desenvolvimento_e_Pseudocodigo.pdf`
- `engine_structure/Cartoes_v1_Pacote_Implementacao_Real.pdf`
- `output_contractual/Alinhamento_Modulo_Cartoes_Contrato_v1_1.pdf`
- `output_contractual/Cartoes_v1_JSONs_Referencia_e_Casos_Teste_Integracao.pdf`
- `output_contractual/Cartoes_v1_Regras_Validacao_QA_Handoff_Opportunity_Pool.pdf`
- `output_contractual/Contrato_Transversal_Integracao_SignalBet_v1_1_Operacional.pdf`
- `docs/Modulo_Cartoes_Documento_Operacional_v1.pdf`
- `docs/SignalBet_Cartoes_Data_API_Layer_Requisitos.pdf`

## Dependências
- Python 3.11+
- `jsonschema` para validação de payloads
- Data/API Layer central com contexto do jogo, odds e sinais disciplinares
- Contrato transversal `market_pick.v1.1`

## Destino final pretendido
- Destino agora: `migration_workspace/cards/2026-03-23_cards_foundation_pack/`
- Destino final: `modules/cards/`

## Estado
**teste**
