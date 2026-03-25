# bankroll_risk_manager_official_pack_v1

## objetivo_do_pack
Transformar a shortlist do Global Pick Selector em decisões mínimas de stake, exposição e payload para Execution.

## estado_do_pack
staging

## dependencias
- Python 3.11+
- shortlist do `global_pick_selector_official_pack_v1`
- contrato v1.1 como referência estrutural

## ponto_de_entrada
- `run_smoke.cmd`
- `src/bankroll_smoke.py`

## ponto_de_saida
- `examples/bankroll_smoke_output_generated.json`

## contrato
- referência ao contrato v1.1

## como_le_do_fluxo_anterior
Nesta v1, a banca lê a shortlist de exemplo em `examples/gps_shortlist_input.json`.
A fase seguinte deve ligar este input diretamente ao output do GPS em staging.

## o_que_este_pack_prova
- leitura de shortlist
- aplicação mínima de regras de stake
- controlo simples de exposição
- geração de payload claro para Execution

## o_que_ainda_nao_faz
- regras avançadas de correlação
- gestão completa de banca dinâmica
- ligação direta automática ao GPS no filesystem do projeto
