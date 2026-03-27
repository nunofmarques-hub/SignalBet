# Trunk native intake

## regra central
O Orchestrator deve ler a baseline real a partir do trunk físico, não de um ficheiro artificial criado só para o teste.

## ordem de descoberta
1. localizar a raiz `.../data_api`
2. ler `storage/storage_snapshot_manifest.json`
3. ler `storage/state/league_140/season_2024/*.state.json`
4. ler `storage/raw/league_140/season_2024/catalog/fixtures_catalog_status_FT_AET_PEN.json`

## objetivo
Transformar a baseline real validada em estado operacional protegido e legível.
