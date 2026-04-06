# SignalBet — Orchestrator Payload Writer Pack

## Objetivo
Materializar no **Orchestrator / App Core** o writer único do payload oficial vivo do ciclo, eliminando payloads paralelos, colagem manual entre camadas e fallback manual residual.

## Estado
staging_forte

## Frente
Orchestrator / App Core

## Problema que este pack fecha
Até aqui, o corredor central já estava validado em termos de handoff e semântica, mas faltava materializar fisicamente um **writer único** responsável por:
- criar o payload oficial do ciclo
- atualizar sempre o mesmo payload ao longo das fases
- preservar o mesmo `pick_id` e a mesma identidade operacional
- impedir competição entre fontes paralelas

## O que este pack traz
- `src/orchestrator_payload_writer/payload_writer.py` — writer único do payload vivo
- `src/orchestrator_payload_writer/contracts.py` — shape mínima do payload e regras de semântica
- `src/orchestrator_payload_writer/demo_cycle.py` — demo local de ciclo curto completo
- `run_smoke.py` — smoke test do writer
- `examples/official_cycle_payload.json` — output de exemplo
- `docs/orchestrator_payload_writer_notes.md` — nota operacional curta
- `manifest.json` — metadados do pack
- `pack_check_report.txt` — verificação mínima

## Papel deste pack na arquitetura
Este pack **não reabre arquitetura**.
Apenas materializa a decisão já fechada de que:
- o **Orchestrator / App Core** é a fonte oficial única do payload do ciclo
- o payload é único e vivo
- o update loop decorre dentro da app
- a UI lê o payload final; não o constrói

## Fases cobertas pelo payload
1. shortlist
2. decisão da Banca
3. intake / tracking da Execution
4. settlement

## Regras que este pack preserva
- 1 caso único por ciclo
- 1 `pick_id` único e estável do início ao fim
- naming estável
- zero payload paralelo
- zero colagem manual entre camadas
- handoff oficial sem atalhos
- não duplicação obrigatória

## Como correr o smoke test
```bash
python run_smoke.py
```

## Resultado esperado do smoke
- payload criado com sucesso
- updates aplicados em sequência no mesmo payload
- `pick_id` preservado ao longo de todo o ciclo
- transições semânticas válidas
- ficheiro `examples/official_cycle_payload.json` atualizado

## Próximo passo recomendado
Ligar este writer ao runner oficial do Orchestrator / App Core e substituir qualquer writer lateral, `latest.json` manual ou montagem intermédia como fonte operacional concorrente.
