# Corners Module Pack - Staging Plus

## objetivo do pack
Dar mais corpo de módulo ao Corners e aproximá-lo de integração real.

## estado do pack
staging

## dependências
- Python 3.x
- sem dependências externas

## ponto de entrada
- testes/run_demo.py

## ponto de saída
- output_contratual/example_engine_output.json
- output_contratual/example_market_pick.json

## referência ao contrato v1.1
Este pack emite candidate picks no schema market_pick.v1.1.

## como lê da Data/API Layer
- Lê um input oficial em motor/data_handoff/sample_input_from_data_layer_official.json
- O adapter em motor/data_handoff/data_adapter.py traduz esse input para o formato interno do motor
- O módulo não fala diretamente com a API externa

## destino final pretendido
modules/corners/
