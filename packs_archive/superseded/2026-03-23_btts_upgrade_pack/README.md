# BTTS Upgrade Pack

**objetivo do pack**  
Fechar o handoff mínimo do módulo BTTS com a arquitetura comum, mostrando leitura de um sample input oficial da Data/API Layer, execução de fluxo mínimo e geração de output estável no contrato `market_pick.v1.1`.

**estado do pack**  
staging

**dependências**  
- Python 3.11+
- Data/API Layer central a fornecer um payload compatível com `sample_input/official_data_api_input.json`
- Contrato Transversal de Integração SignalBet v1.1 Operacional

**ponto de entrada**  
`src/btts/run_minimal_flow.py`

**ponto de saída**  
`sample_output/market_pick_v1_1_btts.json`

**referência ao contrato v1.1**  
O output do módulo é gerado no envelope `market_pick.v1.1` para a Opportunity Pool.

**como lê da Data/API Layer**  
Lê um payload único por evento com:
- contexto base do jogo
- snapshots por equipa
- odds
- metadados de qualidade
- sinais temporais mínimos para FGT

Se a Data/API Layer ainda não fornecer algum campo opcional, o fluxo continua com fallbacks e marca isso em `data_quality_flag` e em `module_specific_payload.input_context.missing_fields`.

**destino atual**  
`migration_workspace/btts/2026-03-23_btts_upgrade_pack/`

**destino final pretendido**  
`modules/btts/`
