# Corners Module Pack - Pré-integração

## objetivo do pack
Dar mais corpo ao módulo Corners, com input realista da Data/API Layer, candidate generation mais robusta e output contratual estável.

## estado do pack
staging

## dependências
- Python 3.x
- Sem dependências externas

## ponto de entrada
- `testes/run_demo.py`
- `motor/candidate_generation/generate_candidates.py`

## ponto de saída
- `output_contratual/example_engine_output.json`
- `output_contratual/example_market_pick.json`

## referência ao contrato v1.1
Este pack gera output no schema `market_pick.v1.1`.

## leitura da Data/API Layer
Lê um input já normalizado vindo da camada central através de:
- `motor/data_handoff/sample_input_from_data_layer_real.json`
- `motor/data_handoff/data_adapter.py`
