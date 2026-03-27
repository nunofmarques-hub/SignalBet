# SignalBet UI v26 — OR16 minimal panel reinforcement

## Estado
staging

## Upstream oficial
OR16 / Orchestrator / App Core

## Objetivo desta execução
Aplicar apenas o encaixe mínimo aprovado no painel de estado da UI, usando o payload protegido do Orchestrator como única fonte.

## O que foi implementado
- manutenção do botão principal sem alterações
- adição de 1 resumo operacional curto no painel de estado
- leitura humana derivada de `central_health`, `baseline_availability`, `complementary_availability` e `corridor_summary`
- sem exposição de campos técnicos em bruto ao utilizador

## Regra de resumo adotada
- `healthy_enriched` + baseline disponível + complemento disponível -> **Corredor central saudável**
- baseline disponível + complemento disponível -> **Baseline e complemento disponíveis**
- apenas baseline disponível -> **Baseline disponível**
- restante -> **Estado central em atualização**

## Fonte ativa
`../runtime_outputs/ui_runtime_snapshot.json`

## Perímetro preservado
A UI lê, interpreta e apresenta. Não liga ao trunk físico, não fala com provider real e não duplica lógica do Orchestrator.
