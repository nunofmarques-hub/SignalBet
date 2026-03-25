# Test Smoke

1. Abrir schemas em `schemas/`.
2. Correr `src/batch_runner.py` sobre `examples/multi_module_batch_inputs/batch_input_case_main.json`.
3. Confirmar existência de:
   - `global_score`
   - `priority_tier`
   - `rank_position`
   - `shortlist_bucket`
4. Confirmar export batch com `shortlist_size`.
