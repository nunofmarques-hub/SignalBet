# ORCHESTRATOR_CHAT_MEMORY_CURRENT

## feito
- Criado OR11 com intake nativo do trunk físico real.
- O Orchestrator deixa de depender de `baseline_state.json` artificial.
- A baseline passa a ser montada a partir de:
  - `storage/storage_snapshot_manifest.json`
  - `storage/state/league_140/season_2024/*.state.json`
  - `storage/raw/league_140/season_2024/catalog/fixtures_catalog_status_FT_AET_PEN.json`

## objetivo
- Consumir a baseline real diretamente do trunk.
- Expor estado operacional protegido para UI sem atalhos arquiteturais.

## decisão
- Preferência arquitetural por leitura nativa do trunk.
- Fallback demo apenas quando o trunk real não é encontrado.

## estado atual
- Pack OR11 pronto.
- Smoke local OK.
- Pronto para teste contra `PROJECT_ROOT` físico real.

## bloqueio
- Sem bloqueio estrutural no pack.
- Leitura real depende do path físico usado no teste.

## próximo passo
- Correr `RUN_OR11_BASELINE_REAL_PROJECT.cmd` com o root correto do projeto.
- Confirmar `source_mode=project`.
