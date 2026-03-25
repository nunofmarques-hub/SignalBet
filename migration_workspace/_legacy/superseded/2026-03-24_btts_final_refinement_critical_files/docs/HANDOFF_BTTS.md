# HANDOFF_BTTS

## Estado
- estado_pack: staging
- provider_principal: direct_official_trunk_provider
- fallback: apoio técnico isolado
- output_estavel: sim

## Fonte oficial
`Data_API_Official_Trunk_v1`

## Fluxo principal
`Data_API_Official_Trunk_v1 -> direct_official_trunk_provider -> official_trunk_loader -> engine -> exporter -> market_pick.v1.1`

## Regra do fallback
O fallback não faz parte do fluxo principal do módulo.
Fica isolado em `support/fallback/` e serve apenas para smoke test técnico quando o tronco não estiver montado no ambiente.
