# Global Pick Selector — Maturation Pack v3

## objetivo do pack
Evoluir o Global Pick Selector de handoff inicial para contrato comparável maduro do sistema, reforçando:
- normalização por módulo mais robusta
- ranking com breakdown explícito
- batch real multi-módulo
- schema final congelado para a banca
- documentação clara de ownership e flags

## estado do pack
staging

## dependências
- Python 3.11+
- standard library apenas nesta versão
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- payloads de entrada produzidos pelos módulos de mercado

## ponto de entrada
- `schemas/gps_multi_module_batch_v1.json`
- `examples/multi_module_batch_inputs/batch_input_case_main.json`
- `src/batch_runner.py`

## ponto de saída
- `schemas/bankroll_export_batch_frozen_v1.json`
- `examples/bankroll_export_outputs/bankroll_export_case_main.json`

## referência ao contrato v1.1
Este pack assume o Contrato Transversal de Integração SignalBet v1.1 Operacional como base de ownership, enums, normalização e passagem GPS -> Banca.

## indicação explícita de como lê da Data/API Layer ou do que falta para isso
Este pack não lê diretamente da Data/API Layer. Consome picks já produzidas pelos módulos de mercado. A ligação à Data/API é indireta e depende de cada módulo fornecedor usar providers oficiais da `data_api/`.

## destino final pretendido
- `modules/global_pick_selector/`
