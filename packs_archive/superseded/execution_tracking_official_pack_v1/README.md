# execution_tracking_official_pack_v1

## objetivo_do_pack
Provar intake real vindo da banca, registo mínimo, settlement básico e output formal para analytics/audit.

## estado_do_pack
staging

## dependencias
- Python 3.11+
- payload da banca em `examples/bankroll_execution_input.json`
- contrato v1.1 como referência estrutural

## ponto_de_entrada
- `run_smoke.cmd`
- `src/execution_smoke.py`

## ponto_de_saida
- `examples/execution_smoke_output_generated.json`

## contrato
- referência ao contrato v1.1

## como_le_do_fluxo_anterior
Nesta v1, a execution lê o payload de exemplo vindo da banca a partir de `examples/bankroll_execution_input.json`.
A fase seguinte deve ligar este input diretamente ao output oficial da banca em staging.

## o_que_este_pack_prova
- intake real vindo da banca
- registo mínimo de apostas
- settlement básico por estado
- output formal para analytics/audit

## o_que_ainda_nao_faz
- settlement completo com resultados oficiais automáticos
- reconciliação avançada
- integração plena com UI / analytics externos
