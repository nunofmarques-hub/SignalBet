# Nota curta final — polimento Cards

## pontos polidos
- `run_smoke.py` fixado como runner oficial desta fase
- `run_demo.py` marcado explicitamente como demo/local
- layout de runtime endurecido com `bootstrap_runtime.py`
- `providers` e `cards_module` tratados como packages explícitos
- imports previsíveis e independentes do diretório corrente
- smoke isolado a passar limpo

## pontos ainda assumidos
- modo `live` continua dependente de `data_api/` físico montado no ambiente
- runner oficial do corredor ponta a ponta continua a pertencer ao Orchestrator, não ao `run_demo.py` do módulo

## decisão
Cards polido e pronto para run final de confirmação.
