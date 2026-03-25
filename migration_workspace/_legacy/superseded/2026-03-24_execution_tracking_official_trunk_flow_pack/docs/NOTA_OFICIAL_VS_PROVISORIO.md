# Nota curta — oficial vs provisório

## Já oficial nesta frente
- Origem do intake: Banca / Bankroll & Risk Manager.
- Caso de intake usado neste pack: baseado no handoff real `execution_intake_candidate.v1.8` + `bankroll_response_batch.v1.8`.
- Referência de dados operacionais/settlement: `Data_API_Official_Trunk_v1` passa a ser a referência oficial atual da Data/API Layer.
- Output formal para analytics/audit: contrato estabilizado nesta frente como `execution-analytics-output.v1`.

## Ainda provisório nesta frente
- O payload de fixture aqui usado para settlement já está orientado ao tronco oficial, mas continua a ser um payload de trabalho da Execution até a Data/API congelar e publicar o contrato exato do provider/reader de fixture usado no settlement.
- O hook de settlement está pronto para ler do tronco, mas a ligação técnica final ao provider oficial ainda depende do pacote oficial da Data/API Layer.
- O crosswalk Banca → Execution continua resolvido nesta frente, mas o handoff unificado definitivo ainda deve ser congelado do lado da Banca quando o pipeline GPS → Banca → Execution for formalmente fechado.

## Leitura prática
Este pack já sai do modo “preparado para” e entra em modo fluxo operacional real de trabalho, mantendo apenas o settlement provider como ponto ainda provisório do lado da Data/API.
