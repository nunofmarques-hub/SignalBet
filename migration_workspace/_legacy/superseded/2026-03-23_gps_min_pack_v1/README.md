# Global Pick Selector — Minimum Functional Pack v1

## objetivo do pack
Entregar a primeira base física mínima do módulo Global Pick Selector, cobrindo validação de schema, normalização raw -> normalized, ranking global inicial, regras de prioridade, flags mínimas e export formal para a banca.

## ficheiros principais
- `schemas/market_pick_v1_1_min.json`
- `schemas/selector_pick_v1_1_min.json`
- `src/schema_validator.py`
- `src/normalization.py`
- `src/ranking.py`
- `src/priority_rules.py`
- `src/flags.py`
- `src/exports_to_bankroll.py`
- `examples/input_v12.json`
- `examples/input_corners.json`
- `examples/input_btts.json`
- `examples/output_selector_v12.json`
- `examples/output_selector_corners.json`
- `examples/output_selector_btts.json`

## dependências
- Python 3.11+
- standard library apenas nesta versão
- Contrato Transversal de Integração SignalBet v1.1 Operacional

## destino final pretendido
- `modules/global_pick_selector/`

## estado
- `teste`
