# Nota para PM — validação do mini fluxo ponta a ponta local
## SignalBet / ABC PRO

**Frente:** Under/Over Jogo  
**Estado:** staging forte offline bem disciplinado  
**Relação com a v12:** v12 mantém-se como linha operacional válida da fase atual

---

## 1. Resultado da ronda

Foi executado com sucesso o **mini fluxo ponta a ponta local de aproximação futura ao corredor**.

O fluxo provado localmente foi:

`input protegido mockado -> adapter local -> output final`

---

## 2. O que ficou provado

### 2.1 Caso `ready`
Ficou provado que, com input protegido mockado completo e odds presentes, a frente:

- adapta a shape protegida
- calcula score, lambda e profile
- emite output final por linha
- preserva coerência da família

### 2.2 Caso `degraded_run`
Ficou provado que, quando faltam odds mas o input crítico existe, a frente:

- não falha
- entra em `degraded_run`
- emite score, probabilidade e fair odds
- deixa `edge` como `null`
- mantém decisão disciplinada por linha

### 2.3 Caso `hard_fail`
Ficou provado que, quando faltam campos críticos do input protegido, a frente:

- não tenta fingir output normal
- devolve `runtime_state = hard_fail`
- lista `missing_fields`

---

## 3. Leitura operacional

A frente Under/Over Jogo já não está apenas em:

- baseline
- protótipo offline
- preparação mockada

A frente passa a ter também:

**prova local executada de consumo futuro simulado do corredor protegido.**

Isto ainda não significa:
- integração real
- consumo live
- subida ao corredor real
- consumo downstream por GPS/Banca

Mas significa:
- adapter local provado
- semântica de degradação provada
- handoff local simulado provado
- output final emitido via adapter provado

---

## 4. Estado atual da frente

Leitura atual correta da frente:

**Under/Over Jogo = staging forte offline bem disciplinado, com aproximação controlada mockada já provada e mini fluxo ponta a ponta local validado.**

---

## 5. Formulação curta de fecho

A frente Under/Over Jogo executou com sucesso o mini fluxo ponta a ponta local da aproximação futura ao corredor, provando localmente input protegido mockado, adapter, output final e semântica de `ready / degraded_run / hard_fail`, mantendo-se ainda fora de integração real.
