# runtime_inputs

## estado
Pasta reposta neste pack para **swap limpo** com a linha atual que ainda a expõe em `modules/corners`.

## leitura operacional
Nesta revisão do pack, `runtime_inputs/` é mantida como **ponte de compatibilidade estrutural** e não como dependência runtime ativa do smoke desta ronda.

## confirmação curta
- `run_smoke.py` não depende de `runtime_inputs/`
- não existe referência ativa a `runtime_inputs/` dentro deste pack para o smoke de readiness
- a pasta fica presente para evitar ambiguidade estrutural no swap da linha atual

## regra desta revisão
Se a coordenação confirmar mais à frente que `runtime_inputs/` já não tem papel vivo na linha oficial, a pasta pode ser removida numa ronda futura, com nota explícita de remoção intencional.
