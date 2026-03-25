# INTEGRATION_NOTES

- estado do pack: staging
- leitura principal: provider direto do tronco oficial
- fallback: apoio técnico separado
- referência contratual: `market_pick.v1.1`
- ponto de entrada: `src/btts/run_minimal_flow.py`
- ponto de saída: `sample_output/market_pick_v1_1_btts.json`

## ajuste aplicado
- `pack_root` corrigido no runner
- provider endurecido para recalcular o fallback se receber um path errado
