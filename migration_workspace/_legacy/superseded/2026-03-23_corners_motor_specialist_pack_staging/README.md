# Corners Motor Specialist Pack

## objetivo do pack
Fazer o módulo Corners mostrar corpo real de motor especialista do mercado de cantos.

## estado do pack
staging

## dependências
- Python 3.x
- sem dependências externas

## ponto de entrada
- testes/run_demo.py

## ponto de saída
- output_contratual/case_1_forte_market_pick.json
- output_contratual/case_2_media_market_pick.json
- output_contratual/case_3_rejeitada_market_pick.json

## referência ao contrato v1.1
Este pack emite candidate picks no schema market_pick.v1.1.

## como lê da Data/API Layer
- lê inputs oficiais em motor/data_handoff/sample_cases_from_data_api.json
- data_adapter.py traduz o input para o formato interno do motor
- o módulo não fala diretamente com a API externa

## destino final pretendido
modules/corners/
