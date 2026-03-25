# BTTS IO handoff pack

**Objetivo do pack**  
Fechar o handoff de integração do módulo BTTS com a futura Data/API Layer central e com a Opportunity Pool.

**Ficheiros principais**  
- `sample_input/central_match_input.json`
- `sample_output/market_pick_v1_1_btts.json`
- `docs/HANDOFF_BTTS_DATA_API.md`
- `docs/IO_MAPPING_BTTS.md`
- `docs/README_INTEGRATION_BTTS.md`

**Dependências**  
- Data/API Layer central a produzir o payload de input do jogo
- Engine BTTS a consumir esse input e a exportar `market_pick.v1.1`
- Contrato transversal SignalBet v1.1 operacional

**Destino final pretendido**  
`modules/btts/`

**Estado**  
`teste`
