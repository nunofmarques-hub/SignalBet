# Trunk Assumption and Boundaries v2

## assunção oficial
O Global Pick Selector assume que os inputs válidos chegam de módulos fornecedores ligados ao `Data_API_Official_Trunk_v1`.

## upstream confirmado neste pack
- v12
- BTTS
- Cards
- Corners

## o que o GPS não faz
- não consome API externa diretamente
- não chama providers da Data/API Layer diretamente
- não recalcula o motor analítico do módulo de origem

## o que o GPS faz
- valida contrato
- normaliza score/confiança/risco/edge
- compara picks heterogéneas
- produz ranking global auditável
- gera shortlist formal
- exporta payload congelado para a banca
