# SBO OR11 — Trunk Native Baseline Pack

## objetivo
Fazer o Orchestrator consumir a baseline real diretamente da estrutura física do Data_API_Official_Trunk_v1, sem ficheiro adaptador artificial.

## foco desta ronda
- intake direto do trunk
- leitura do manifest de storage
- leitura dos ficheiros de state da baseline validada
- leitura do catálogo `fixtures_catalog_status_FT_AET_PEN.json`
- exposição protegida de estado à UI

## paths reais esperados
O pack tenta descobrir a baseline real em estruturas como:
- `<PROJECT_ROOT>/data_api/Data_API_Official_Trunk_v1/data_api/...`
- `<PROJECT_ROOT>/Data_API_Official_Trunk_v1/data_api/...`
- `<PROJECT_ROOT>/data_api/...`

## baseline oficial
- `league_140 / season_2024 / status FT-AET-PEN`
- fluxo real: `fixtures`
- consumidor principal: `Orchestrator`
