# v12 — clean full swap pack

Linha limpa da frente v12 preparada para troca integral da pasta do módulo.

## Objetivo desta linha
Fechar o bloqueio residual de runtime ligado à derivação de `league_id` no bundle protegido, mantendo:

- consumo apenas por camada protegida / central
- ausência de trunk direto no módulo
- ausência de provider direto no módulo
- foco apenas nos 3 motores maduros
- falha auditável (`hard_fail`) em vez de erro bruto

## Núcleo ativo
- Over 1.5 equipa
- Over 1.5 jogo
- Under 3.5

## Conteúdo principal
- `motor/provider_bridge.py` — ponte endurecida de consumo protegido
- `motor/input_adapter.py` — normalização do bundle protegido
- `motor/smoke_test.py` — rerun isolado da v12
- `runtime_inputs/protected_runtime_payload.json` — payload protegido de exemplo
- `schemas/runtime_fix_contract.md` — contrato curto da normalização
- `docs/runtime_fix_note.md` — nota curta do fecho residual
- `examples/runtime_fix_summary.json` — resumo do rerun esperado
- `MEMORIA_OPERACIONAL_ATIVA_V12.md` — memória ativa da frente

## Como usar
Trocar a pasta atual `modules/v12/` por esta pasta `v12/` completa.

Depois correr:

```bash
python motor/smoke_test.py
```

ou

```bash
py motor/smoke_test.py
```

## Resultado esperado
- deixa de falhar por ausência rígida de `league` / `league_id`
- tenta derivação semântica de `league_id` em múltiplas posições do bundle
- mantém `hard_fail` curto e auditável se o campo continuar realmente ausente
