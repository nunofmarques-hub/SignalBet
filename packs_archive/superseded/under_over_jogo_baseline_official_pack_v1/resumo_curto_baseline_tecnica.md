# Resumo Curto da Baseline Técnica
## Under/Over Jogo

### Identidade atual
Baseline offline oficial congelada da frente Under/Over Jogo.

### Núcleo congelado
- Over 1.5
- Over 2.5
- Under 3.5
- Under 2.5
- Over 3.5 como expansão controlada

### Fluxo base
`build_base_state -> evaluate_lines -> apply_family_coherence -> emit_output`

### Regra crítica congelada
No cenário intermédio atual:
- Over 1.5 = rejected
- Over 2.5 = rejected

Leitura:
**corredor intermédio conservador por regra do modelo atual**

### Estado da frente
- provada offline
- sem integração real
- sem corredor central
- sem concorrência runtime com a v12

### Gate futuro
Pode avançar apenas com decisão formal para:
- protótipo offline
ou
- aproximação técnica controlada ao corredor protegido
