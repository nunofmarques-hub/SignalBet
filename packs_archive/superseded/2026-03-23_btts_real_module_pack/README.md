# BTTS Real Module Pack

**Objetivo do pack**
Entregar o BTTS já em formato de módulo real de teste, com `src/` executável, fluxo mínimo, contrato de export e input esperado da Data/API Layer central.

**Ficheiros principais**
- `src/btts/engine.py` — motor mínimo executável BTTS
- `src/btts/models.py` — modelos internos
- `src/btts/loaders.py` — leitura dos outputs da Data/API Layer
- `src/btts/exporter.py` — export para `market_pick.v1.1`
- `src/btts/run_minimal_flow.py` — fluxo mínimo executável
- `src/btts/contracts/export_contract_market_pick_v1_1.json` — contrato de export do módulo
- `src/btts/contracts/input_from_data_layer.json` — input esperado da camada central
- `src/btts/examples/output/example_market_pick.json` — exemplo real de saída

**Dependências**
- Python 3.10+
- Biblioteca standard (`json`, `dataclasses`, `pathlib`, `datetime`)
- Sem dependências externas obrigatórias nesta versão de teste

**Destino final pretendido**
- `modules/btts/`

**Estado**
- `teste`

**Nota**
Este pack já é executável, mas continua em estado de teste porque a leitura da Data/API Layer ainda está a estabilizar, sobretudo nos campos ricos de statistics/odds.
