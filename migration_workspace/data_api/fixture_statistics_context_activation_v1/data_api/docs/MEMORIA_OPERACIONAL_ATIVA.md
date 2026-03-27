# MEMORIA_OPERACIONAL_ATIVA

## Frente
Data/API Layer

## Estado atual
Baseline real mínima validada e segundo fluxo real controlado aberto em ativação curta.

## Segundo fluxo escolhido
Fixture statistics context.

## Motivo da escolha
É o fluxo complementar mais pequeno, útil e controlado ao corredor baseline de fixtures já validado. Enriquece o Orchestrator sem transformar enriquecimento em dependência.

## Perímetro desta fase
- consumidor principal: Orchestrator / App Core
- fixtures continuam a ser a base principal
- statistics context entra como camada complementar e não bloqueante
- UI fica apenas em acompanhamento
- sem live total, sem novos mercados, sem múltiplos providers, sem consumo direto por módulos analíticos

## Política mínima aplicada
- cache via storage oficial do trunk
- refresh controlado
- fallback explícito com `statistics_status = missing`
- erro do enrichment não quebra a baseline principal
- logs mínimos curtos por fixture e por run

## Estado da ativação
Fluxo preparado para leitura real de statistics por fixture sobre o mesmo cenário baseline validado.

## Próximo passo
Executar o smoke/runner desta ativação, provar consumo sem ambiguidade no Orchestrator e confirmar ausência de regressão no corredor já validado.
