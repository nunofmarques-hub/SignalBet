# Global Pick Selector -> Banca -> Execution Handoff Pack v1

## objetivo do pack
Congelar o handoff formal do Global Pick Selector para a Banca e deixar uma ponte explícita para o intake da Execution / Tracking.

## estado do pack
staging

## dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- payload final do Global Pick Selector
- resposta formal da Banca
- intake da Execution / Tracking

## ponto de entrada
- `schemas/gps_shortlist_batch_v1.json`
- `examples/gps_shortlist_batch_example_v1.json`

## ponto de saída
- `schemas/execution_intake_candidate_v1.json`
- `examples/execution_intake_candidate_example_v1.json`

## referência ao contrato v1.1
Este pack assume o Contrato Transversal de Integração SignalBet v1.1 Operacional como base semântica de ownership, normalização e passagem entre camadas.

## indicação explícita de como lê da Data/API Layer ou do que falta para isso
Este pack não lê diretamente da Data/API Layer. Consome payload já produzido pelo Global Pick Selector a partir de picks vindas dos módulos de mercado. Dependência indireta: o GPS deve receber input oficial da Data/API via módulos fornecedores.

## destino final pretendido
- `modules/global_pick_selector/`
