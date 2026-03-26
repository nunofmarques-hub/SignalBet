# global_pick_selector_official_pack_v1

## objetivo_do_pack
Materializar o Global Pick Selector como agregador mínimo real de oportunidades vindas de módulos em staging.

## estado_do_pack
staging

## dependencias
- Python 3.11+
- outputs de exemplo de módulos em staging
- contrato v1.1 como referência estrutural

## ponto_de_entrada
- `run_smoke.cmd`
- `src/gps_smoke.py`

## ponto_de_saida
- `examples/gps_smoke_output_generated.json`

## contrato
- referência ao contrato v1.1

## como_le_dos_modulos
Nesta v1, o GPS lê inputs de exemplo multi-módulo a partir de `examples/module_inputs/`.
A fase seguinte deve ligar estes inputs diretamente aos packs dos módulos em staging.

## o_que_este_pack_prova
- ingestão multi-módulo
- normalização mínima
- ranking explícito
- shortlist única do sistema

## o_que_ainda_nao_faz
- leitura direta automática de outputs reais dos módulos no filesystem do projeto
- handoff final para banca
- regras avançadas de conflito/exposição
