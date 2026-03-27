# v12 — contrato protegido de entrada

## 1. objetivo do contrato
Este contrato define o input mínimo protegido que a v12 precisa para um primeiro ensaio de aproximação controlada ao corredor central.

A v12 lê por camada protegida / central e nunca por sourcing direto.

---

## 2. escopo funcional desta ronda
### motores cobertos
- Over 1.5 equipa
- Over 1.5 jogo
- Under 3.5

### fica fora
- BTTS
- Over 2.5
- Under 2.5
- novas linhas
- tuning pesado
- expansão de família Over/Under

---

## 3. schema curto de input protegido

## 3.1 campos obrigatórios
### identidade do evento
- `fixture_id`
- `league_id`
- `season`
- `home_team_id`
- `away_team_id`

### metadata mínima de proveniência e readiness
- `source_mode`
- `observed_mode`
- `readiness_level`
- `provider_name`
- `provider_source`
- `input_profile`

### bloco mínimo analítico
- `fixture_context`
- `team_context`
- `stats_core`

---

## 3.2 campos úteis
- `baseline_status`
- `complementary_status`
- `central_health`
- `corridor_summary`
- `stats_complementary`
- `availability_flags`

---

## 3.3 semântica dos blocos
### `fixture_context`
Contexto protegido do evento: estado, liga, timing e informação base suficiente para enquadrar o jogo.

### `team_context`
Contexto protegido comparável das equipas: perfil casa/fora, força relativa mínima, leitura curta do confronto.

### `stats_core`
Bloco mínimo para suportar os 3 motores maduros. Deve trazer apenas leitura suficiente para decisão e não payload cru de provider.

### `stats_complementary`
Enriquecimento não bloqueante. Pode reforçar decisão, mas a sua ausência não obriga automaticamente a `hard_fail`.

---

## 4. política operacional fechada

### `full_read`
Usar quando todos os campos obrigatórios estão presentes e o bloco mínimo analítico está coerente.

Resultado:
- os 3 motores podem ser avaliados
- a v12 pode gerar output normal
- pode existir candidato forte, se o score e o risco o permitirem

### `degraded_run`
Usar quando o input mínimo obrigatório existe, mas falta parte do contexto útil ou enriquecimento não crítico.

Resultado:
- a v12 pode correr
- convicção operacional reduzida
- pode degradar elegibilidade ou candidate status
- não inventa fallback fora do corredor

### `watchlist_only`
Usar quando há contexto suficiente para observação comparável, mas não para decisão forte.

Resultado:
- a v12 não deve emitir candidato forte de pipeline
- pode emitir apenas watchlist
- a limitação deve ficar explícita no output

### `hard_fail`
Usar quando faltam campos críticos de identidade, proveniência ou bloco mínimo analítico.

Resultado:
- a v12 não corre decisão
- não continua silenciosamente
- deve devolver falha explícita e curta

---

## 5. mapping input -> decisão do módulo

## 5.1 motor Over 1.5 equipa
### alimentado por
- `team_context`
- `stats_core.offense_home_or_favorite`
- `stats_core.opponent_defense`
- `fixture_context`
- metadata de readiness

### bloqueios principais
- falta de leitura mínima ofensiva da equipa-alvo
- falta de leitura mínima defensiva do adversário
- `watchlist_only` ou `hard_fail`

---

## 5.2 motor Over 1.5 jogo
### alimentado por
- `team_context`
- `stats_core.match_offense_balance`
- `stats_core.match_open_profile`
- `fixture_context`
- metadata de readiness

### bloqueios principais
- contexto ofensivo bilateral insuficiente
- input parcial que não sustente leitura de dinâmica do jogo
- `watchlist_only` ou `hard_fail`

---

## 5.3 motor Under 3.5
### alimentado por
- `team_context`
- `stats_core.match_control_profile`
- `stats_core.defensive_stability`
- `fixture_context`
- metadata de readiness

### bloqueios principais
- ausência de leitura mínima de controlo/ritmo
- sinais críticos em falta para enquadrar jogo fechado
- `watchlist_only` ou `hard_fail`

---

## 5.4 o que acontece quando falta parte do input
### falta enriquecimento não crítico
- manter decisão possível
- classificar como `degraded_run`
- reduzir convicção e explicar a perda

### falta bloco mínimo para score robusto
- impedir candidato forte
- permitir apenas `watchlist_only` se ainda existir observação comparável

### falta identidade/proveniência/bloco crítico
- `hard_fail`

---

## 5.5 o que impede candidato forte
- `degraded_run` com perda material de leitura
- `watchlist_only`
- risco elevado sem compensação forte
- ausência de parte crítica do `stats_core`
- incoerência entre readiness e input observado

## 5.6 o que permite só watchlist
- input mínimo não completamente fiável
- contexto suficiente para leitura, mas insuficiente para elegibilidade forte
- ausência de sinais críticos para convicção operacional

---

## 6. output esperado

## 6.1 núcleo mínimo do output contratual
- `module_name`
- `module_version`
- `pick_id`
- `generated_at`
- `fixture_id`
- `league_id`
- `season`
- `home_team_id`
- `away_team_id`
- `market_family`
- `market_code`
- `selection_label`
- `raw_module_score`
- `score_band`
- `eligibility`
- `candidate_status`
- `rationale_short`
- `key_factors`
- `risk_flags`
- `provider_name`
- `provider_source`
- `input_profile`
- `contract_version`
- `runtime_state`

## 6.2 semântica do output
- `eligibility`: pode ou não seguir pipeline
- `candidate_status`: `candidate`, `watchlist`, `rejected`
- `runtime_state`: `full_read`, `degraded_run`, `watchlist_only`, `hard_fail`

---

## 7. limites explícitos
- sem trunk direto
- sem provider direto
- sem novos mercados
- sem tuning pesado
- sem expansão fora dos 3 motores

---

## 8. regra final desta ronda
O objetivo deste contrato é deixar a v12 pronta para um primeiro ensaio real de aproximação controlada, ainda sem integração total. fileciteturn1file0
