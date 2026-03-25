README CURTO

Objetivo do pack
Dar mais corpo ao módulo Corners, deixando explícitos:
- input realista vindo da Data/API Layer central
- blocos internos de motor (indicadores, elegibilidade, scoring, interpretação e seleção)
- candidate generation real
- output contratual estável em market_pick.v1.1

Ficheiros principais
- motor/data_handoff/sample_input_from_data_layer_real.json
- motor/data_handoff/input_contract_corners.md
- motor/data_handoff/data_adapter.py
- motor/engine/indicators.py
- motor/engine/eligibility.py
- motor/engine/scoring.py
- motor/engine/interpretation.py
- motor/engine/candidate_selection.py
- motor/candidate_generation/generate_candidates.py
- motor/contract_output/contract_mapper.py
- motor/contract_output/candidate_pick_builder.py
- testes/run_demo.py
- output_contratual/example_engine_output.json
- output_contratual/example_market_pick.json

Dependências
- Python 3.x
- Sem dependências externas
- generate_candidates.py depende de:
  - motor/data_handoff/data_adapter.py
  - motor/engine/*
  - motor/contract_output/*

Destino final pretendido
modules/corners/

Estado
staging
