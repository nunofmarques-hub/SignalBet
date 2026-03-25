# Validation Run — nota operacional

Este pack implementa um mini cenário executável de `validation_run` com estas regras:

- corre preflight e readiness reais sobre o `Data_API_Official_Trunk_v1`
- descobre módulos elegíveis por registry
- limita a corrida ao subset previsto no perfil `validation_run`
- usa payloads de sample por módulo para simular um pipeline controlado
- devolve `health_report`, `run_summary` e `ui_status`
- salta execution real, mantendo `execution_status = SKIPPED`
