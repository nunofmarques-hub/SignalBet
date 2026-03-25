# Nota de integração v2.2

Este pack congela a camada financeira/operacional da banca sobre um upstream direto vindo do Global Pick Selector.

Fluxo assumido:
1. módulos analíticos ligados progressivamente ao Data_API_Official_Trunk_v1
2. Global Pick Selector normaliza e exporta shortlist para banca
3. banca aplica admissibilidade, sizing, exposure e decision status
4. execution consome apenas payload final limpo e sem ambiguidades

Corredor operacional preparado neste pack:
- `contracts/gps_to_bank_v22.json`
- `contracts/bank_resp_v22.json`
- `contracts/bank_to_exec_v22.json`
