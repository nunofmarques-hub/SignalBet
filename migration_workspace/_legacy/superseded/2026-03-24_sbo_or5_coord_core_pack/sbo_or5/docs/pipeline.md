# Pipeline oficial refletido no draft

1. `config_check`
2. `environment_check`
3. `data_api_readiness_check`
4. `module_discovery`
5. `run_market_modules`
6. `collect_candidates`
7. `run_global_pick_selector`
8. `run_bankroll_manager`
9. `register_execution`
10. `build_run_summary`
11. `return_ui_status`

No `validation_run`, a Execution fica em `SKIPPED`, mas o resto do fluxo é percorrido.
