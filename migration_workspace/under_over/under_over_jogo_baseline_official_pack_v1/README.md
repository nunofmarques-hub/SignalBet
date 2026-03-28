# Under/Over Jogo — Baseline Offline Oficial
## SignalBet / ABC PRO

**Frente:** Under/Over Jogo  
**Estado:** baseline offline oficial congelada  
**Coordenação:** PM / coordenação do projeto  
**Relação com a v12:** v12 mantém-se como linha operacional válida da fase atual

---

## 1. Objetivo desta baseline

Esta baseline existe para fixar, de forma curta, clara e auditável, o estado oficial atual da frente **Under/Over Jogo**.

A frente deixa de estar em iteração aberta e passa a ter uma linha de referência oficial para continuidade futura.

---

## 2. O que a frente é hoje

A frente **Under/Over Jogo** deve ser lida hoje como:

- **arquitetura-alvo futura forte** da família de totais do jogo
- **baseline offline oficial congelada**
- **frente tecnicamente provada offline**
- **ainda sem integração real**
- **ainda sem corredor central**
- **ainda sem concorrência runtime com a v12**

---

## 3. O que já ficou provado

Fica provado nesta fase que a frente já passou por:

- base teórica
- compressão disciplinada
- expansão da família
- mini-spec executável
- pseudo-implementação disciplinada
- ensaio técnico offline
- ajuste técnico fino
- fecho disciplinado do corredor intermédio

---

## 4. O que fica congelado nesta baseline

Ficam congelados, nesta fase:

- **família multi-linha expandida**
- **hierarquia de linhas**
- **linhas operacionais iniciais**
- **papel de `Over 3.5` como expansão controlada**
- **fluxo offline base**
- **coerência multi-linha**
- **corredor intermédio conservador por regra do modelo atual**
- **limites atuais da frente**

---

## 5. Hierarquia congelada da família

### 5.1 Linhas operacionais iniciais
- **Over 1.5**
- **Over 2.5**
- **Under 3.5**
- **Under 2.5**

### 5.2 Linha de expansão controlada
- **Over 3.5**

### 5.3 Linhas de apoio preservadas
- Over 0.5
- Under 1.5
- Under 4.5

### 5.4 Linhas extremas preservadas
- Over 4.5
- Under 5.5
- Over 5.5
- Under 6.5
- Over 6.5

---

## 6. Regra congelada do corredor intermédio

Fica oficialmente congelado que, no cenário intermédio atualmente usado por esta frente:

- **Over 1.5 = rejected**
- **Over 2.5 = rejected**

Isto deixa de ser ambiguidade e passa a ser:

**regra atual do modelo.**

### Leitura operacional
O corredor **2–3** fica formalmente tratado, nesta grelha atual, como:

**corredor conservador por regra do modelo atual.**

---

## 7. Fluxo offline base congelado

O fluxo offline base da frente fica congelado assim:

`build_base_state -> evaluate_lines -> apply_family_coherence -> emit_output`

### Saída esperada por linha
- score
- probability
- fair_odds
- edge
- eligibility
- candidate_status
- rationale_short
- risk_flags

---

## 8. Coerência familiar congelada

Continua congelado como regra da família:

- monotonia Over/Under
- herança de força
- não contradição
- corredor plausível

A frente deve continuar a comportar-se como família e não como linhas soltas.

---

## 9. O que ainda não entra

Nesta baseline, continua fora:

- integração real
- corredor central
- runtime real
- concorrência com a v12
- código de integração
- trunk direto
- substituição operacional da v12

---

## 10. Gate para começar a bater código

A frente **ainda não deve entrar em código de produção nem código de integração real** nesta ronda.

### Caminho A — protótipo técnico offline
Pode existir quando houver decisão formal de coordenação após este congelamento.

### Caminho B — aproximação técnica ao corredor protegido
Só pode existir com decisão formal do PM, contrato mínimo e enquadramento controlado.

### Regra curta
Até nova decisão formal:
- **sim** a protótipo offline, se autorizado
- **não** a integração real
- **não** a trunk direto
- **não** a furar a posição operacional atual da v12

---

## 11. Formulação curta de fecho

A frente **Under/Over Jogo** fica oficialmente congelada nesta fase como **baseline offline oficial**, com família multi-linha expandida, pseudo-implementação já provada offline, ajuste técnico fino executado, corredor intermédio conservador por regra do modelo atual e sem integração real nem concorrência runtime com a v12.
