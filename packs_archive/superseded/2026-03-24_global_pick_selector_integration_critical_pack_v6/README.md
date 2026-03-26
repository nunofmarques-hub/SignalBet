# Global Pick Selector — Integration Critical Pack v6

## objetivo do pack
Consolidar o Global Pick Selector como camada central de comparação madura do sistema, com:
- batch real multi-módulo
- normalização robusta por módulo
- ranking explícito e auditável
- schema final congelado para a banca
- ownership, flags e boundary claros
- hygiene oficial completa de pack

## estado do pack
staging

## módulo/frente
global_pick_selector

## dependências
- Python 3.11+
- standard library apenas nesta versão
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- módulos fornecedores ligados ao `Data_API_Official_Trunk_v1`

## ponto de entrada
- `contracts/gps_multi_module_batch_v3.json`
- `examples/multi_module_batch_inputs/batch_input_case_main.json`
- `src/batch_runner.py`

## ponto de saída
- `contracts/bankroll_export_batch_frozen_v3.json`
- `examples/bankroll_export_outputs/bankroll_export_case_main.json`
