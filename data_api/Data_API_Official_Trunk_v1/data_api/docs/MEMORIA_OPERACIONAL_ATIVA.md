# MEMORIA_OPERACIONAL_ATIVA

## frente
Data/API Layer

## estado anterior da frente
Linha oficial funcional e validada, mas topo da `data_api/` ainda com competição visual entre trunk ativo, packs de fase já absorvidos, apoio útil e auxiliares temporários.

## ruído identificado
- packs de live activation e calibração ainda visíveis como se fossem linhas ativas
- packs de statistics context já absorvidos ainda a competir com o trunk oficial
- `compat/` sem separação clara face à linha oficial
- `_temporary_aux/` ainda no topo ativo
- `__pycache__`, `.pyc` e logs redundantes espalhados

## decisão de limpeza aplicada
- manter `Data_API_Official_Trunk_v1/` como linha oficial ativa inequívoca
- mover apoio vivo para `_support_live/`
- mover packs absorvidos e auxiliares temporários para `_archive_superseded/`
- remover lixo técnico (`__pycache__`, `.pyc`, logs redundantes)
- adicionar índice curto no topo da frente para leitura futura

## o que foi mantido ativo
- `Data_API_Official_Trunk_v1/`

## o que foi mantido como apoio vivo
- `_support_live/compat/`

## o que foi movido para arquivo ou removido
- `_temporary_aux/` -> `_archive_superseded/_temporary_aux/`
- `coverage_increase_order_v1/` -> `_archive_superseded/coverage_increase_order_v1/`
- `fixture_statistics_context_activation_v1/` -> `_archive_superseded/fixture_statistics_context_activation_v1/`
- `fixture_statistics_context_to_trunk_official_v1/` -> `_archive_superseded/fixture_statistics_context_to_trunk_official_v1/`
- `live_data_activation_phase1_real_fixtures_snapshot_pack_v1/` -> `_archive_superseded/live_data_activation_phase1_real_fixtures_snapshot_pack_v1/`
- `real_data_calibration_reliability_phase_v1_1_1/` -> `_archive_superseded/real_data_calibration_reliability_phase_v1_1_1/`
- `real_data_calibration_reliability_phase_v1_1_2/` -> `_archive_superseded/real_data_calibration_reliability_phase_v1_1_2/`
- `real_data_calibration_reliability_phase_v1_1_3/` -> `_archive_superseded/real_data_calibration_reliability_phase_v1_1_3/`
- `__pycache__/`, `.pyc` e logs redundantes removidos

## estado final da frente
Topo da `data_api/` limpo, trunk oficial visualmente inequívoco, apoio vivo separado, histórico fora da linha ativa e frente mais legível para consumo futuro por outras frentes e módulos.

## próximo passo recomendado
Usar `Data_API_Official_Trunk_v1/` como única linha viva da frente e só reabrir novas iterações Data/API quando houver novo objetivo funcional explícito do corredor central.
