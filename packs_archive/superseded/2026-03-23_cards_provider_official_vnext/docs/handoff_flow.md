# Handoff curto

1. Data/API Layer exporta payload central de cartões.
2. `providers/official_cards_provider.py` valida e mapeia o input.
3. `src/cards_module/core/orchestrator.py` corre scoring + elegibilidade.
4. `src/cards_module/io/exporter.py` produz `market_pick.v1.1`.
5. `src/cards_module/io/validator.py` valida antes de colocar em `out/`.
