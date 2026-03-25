# Pipeline v1

## Fluxo ponta a ponta
1. Clique do utilizador na UI.
2. A UI envia um `run_request` ao launcher.
3. O launcher cria `run_id`, resolve o perfil e arranca contexto.
4. O Orchestrator corre preflight / health checks.
5. Se os checks bloqueantes passarem, valida readiness da Data/API Layer.
6. Descobre módulos elegíveis para esta execução.
7. Corre os módulos analíticos pela ordem oficial.
8. Junta as candidatas numa Opportunity Pool.
9. Envia as candidatas ao Global Pick Selector.
10. Envia a shortlist à Banca.
11. Regista as aprovadas na Execution / Tracking.
12. Constrói `run_summary` e devolve `ui_status`.

## Ordem oficial do pipeline
- config_check
- environment_check
- data_api_readiness_check
- module_discovery
- run_market_modules
- collect_candidates
- run_global_pick_selector
- run_bankroll_manager
- register_execution
- build_run_summary
- return_ui_status
