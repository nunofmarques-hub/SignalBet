# Estratégia de fecho da frente

## Melhor forma de executar a partir daqui
1. Consumir o `bank_to_exec_v24` físico assim que a Banca o entregar
2. Reapontar o settlement do payload-alvo para o provider físico do `Data_API_Official_Trunk_v1`
3. Repetir o mesmo smoke E2E sem mudar a linguagem do ledger
4. Se o smoke ficar verde, promover de `staging` para `pronto_para_integracao`

## O que não precisa de mais trabalho estrutural
- state machine
- ledger
- audit trail
- hygiene de pack
- smoke principal da camada
