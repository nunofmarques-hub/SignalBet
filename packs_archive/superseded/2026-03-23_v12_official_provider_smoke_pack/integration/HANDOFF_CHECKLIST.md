# Handoff checklist — v12

## Antes de promover
- [ ] Confirmar provider oficial em `data_api/`
- [ ] Validar shape real contra `schemas/input_shape_provider_real.json`
- [ ] Correr `motor/smoke_test.py` sem editar outputs manuais
- [ ] Confirmar saída em `market_pick.v1.1`
- [ ] Confirmar enums estáveis e `module_specific_payload` v12

## Dependências mínimas de dados
- fixture/contexto
- standings context
- team stats season/recent
- odds snapshot ou fallback controlado

## Destino seguinte
Integração parcial após ligação a provider oficial da Data/API Layer.
