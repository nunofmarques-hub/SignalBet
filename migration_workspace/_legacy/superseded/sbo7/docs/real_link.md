# Ligação ao tronco real

## Precedência do project_root
1. `run_request.project_root`
2. variável de ambiente `SIGNALBET_PROJECT_ROOT`
3. `examples/req/project_root.txt`
4. parent do pack
5. fallback demo do pack

## Regra
Se existir `data_api/Data_API_Official_Trunk_v1` no root resolvido, o pack entra em `project_mode = real_like`. Caso contrário, fica em `project_mode = demo`.

## Importante
O pack não deve fingir integração real antes de a provar.
