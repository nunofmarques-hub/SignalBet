# MEMORIA_OPERACIONAL_ATIVA

## frente
Data/API Layer

## estado anterior da frente
Linha oficial funcional e validada, com limpeza já praticamente fechada, mas ainda com um pack de exportação ao Orchestrator a competir visualmente no topo da frente e com lixo técnico residual (`__pycache__`, `.pyc`, ficheiro solto sem função viva).

## ruído identificado
- pack `data_api_health_core_to_orchestrator_v1/` ainda no topo da frente, a competir com a linha oficial ativa
- `__pycache__/` e `.pyc` residuais no trunk e no pack de exportação
- ficheiro solto sem função viva no trunk oficial
- falta de índice curto atualizado para leitura rápida da frente

## decisão de limpeza aplicada
- manter `Data_API_Official_Trunk_v1/` como linha oficial ativa inequívoca
- manter `_support_live/compat/` como apoio vivo
- mover `data_api_health_core_to_orchestrator_v1/` para `_support_live/orchestrator_exports/`
- remover `__pycache__/`, `.pyc` e ficheiro solto sem função viva
- atualizar a memória operacional ativa
- adicionar índice curto no topo da frente
- adicionar nota curta no trunk sobre o health core mínimo para o Orchestrator

## o que foi mantido ativo
- `Data_API_Official_Trunk_v1/`

## o que foi mantido como apoio vivo
- `_support_live/compat/`
- `_support_live/orchestrator_exports/data_api_health_core_to_orchestrator_v1/`

## o que foi movido para apoio vivo ou removido
- `data_api_health_core_to_orchestrator_v1/` -> `_support_live/orchestrator_exports/data_api_health_core_to_orchestrator_v1/`
- `__pycache__/` e `.pyc` removidos
- ficheiro solto sem função viva removido

## estado final da frente
Topo da `data_api/` mais limpo, trunk oficial visualmente inequívoco, apoio vivo concentrado em `_support_live/`, exportação curta ao Orchestrator separada da linha viva e menos ruído técnico para consumo futuro.

## próximo passo recomendado
Usar `Data_API_Official_Trunk_v1/` como única linha viva da frente e ler `_support_live/` apenas como apoio vivo não concorrente. A entrega ao Orchestrator do health core deve continuar curta e estável, sem subir detalhe técnico interno a produto.
