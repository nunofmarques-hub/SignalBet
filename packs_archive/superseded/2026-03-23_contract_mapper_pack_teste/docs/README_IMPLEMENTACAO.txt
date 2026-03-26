README IMPLEMENTAÇÃO

PASSO 1
Copiar para a pasta-mãe do módulo:
- motor/contract_mapper.py
- motor/candidate_pick_builder.py

PASSO 2
No ponto onde o módulo já tem a sua saída final de leitura:
corners_output = run_from_payload(payload)

Adicionar:
from candidate_pick_builder import build_candidate_pick

candidate_pick = build_candidate_pick(
    corners_output,
    module_version="corners.v2_logicfix",
    kickoff_datetime=None,
    odds=None,
    edge_raw=None,
    expiry_context="pre_match_same_day",
)

PASSO 3
Gravar ou enviar candidate_pick para a Opportunity Pool

NOTA
Este pack:
- não fala em stake
- não decide sizing
- não faz comparação global
- apenas converte o output do módulo de Cantos para o contrato oficial v1.1
