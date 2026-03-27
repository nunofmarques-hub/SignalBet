# UI / Botão

O botão `Pôr tudo a correr` pertence visualmente à UI.
A coordenação técnica pertence ao App Core / Orchestrator.

Nesta versão, `ui_status` devolve:
- `button_context`
- `module_overview`
- `integration_state`
- `pipeline_steps`
- `last_run_summary`

Objetivo: aproximar o payload do painel real sem fingir que a integração física já foi provada.
