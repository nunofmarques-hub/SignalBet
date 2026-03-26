
# Matriz curta de testes reais — UI v21

| Cenário | PASS/FAIL | Campos observados principais | Nota curta de comportamento |
|---|---|---|---|
| snapshot fresco reutilizado | PASS | observed_mode=real_read_protected, snapshot_reused=true, freshness_state=fresh | reuso legítimo de snapshot fresco |
| snapshot stale com refresh bem-sucedido | PASS | refresh_attempted=true, refresh_succeeded=true, snapshot_reused=false | preferiu nova leitura protegida |
| snapshot stale com refresh falhado e reuso controlado | PASS | refresh_attempted=true, refresh_succeeded=false, snapshot_reused=true | reuso controlado após falha de refresh |
| fallback para orchestrator_mock | PASS | observed_mode=orchestrator_mock, fallback_used=true | fallback limpo sem quebra visual |
| forceRefresh | PASS | refresh_attempted=true, read_preference_reason=force_refresh | forçou nova leitura protegida |
| transição entre requested_mode e observed_mode | PASS | requested_mode=placeholder_live, observed_mode=orchestrator_mock | transição controlada com fallback |
| invalidação explícita | PASS | snapshot_invalidated=true, reuse_blocked=true | snapshot invalidado não reutilizado |
| repetição do mesmo cenário | PASS | snapshot_reused=true, bridge_decision_reason=reused_fresh_snapshot | reuso repetido continua estável |
