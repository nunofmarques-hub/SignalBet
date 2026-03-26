from __future__ import annotations

from pathlib import Path
import json

from provider_bridge import FileCentralProvider, ProviderBridge
from input_adapter import build_v12_input
from contract_output import build_market_pick_v11

MODULE_VERSION = 'v12.10-real-provider-smoke'

def _derive_candidates(v12_input: dict) -> list[dict]:
    fixture = v12_input
    stats = fixture['team_stats_season']
    standings = fixture['standings_context']
    league = fixture['league_market_profile']
    timing = fixture['timing_profile']
    scoreline = fixture['scoreline_profile']
    odds = fixture['odds_snapshot']
    risk = fixture['risk_flags']
    quality = fixture['adapter_meta']['data_quality_flag']

    home_name = fixture['home_team_name']
    away_name = fixture['away_team_name']
    home_rank = standings.get('home_rank', 99)
    away_rank = standings.get('away_rank', 99)
    favorite_team = home_name if home_rank < away_rank else away_name

    home_gf = stats['home']['goals_for_per_game']
    away_gf = stats['away']['goals_for_per_game']
    home_ga = stats['home']['goals_against_per_game']
    away_ga = stats['away']['goals_against_per_game']
    rank_gap = standings.get('rank_gap', abs(home_rank-away_rank))
    corridor = scoreline.get('corridor_under_35_fit', 0.5)
    first_goal = timing.get('away_avg_first_goal_minute', 35)
    european_context = risk.get('european_context', False)

    fdi = round(min(10, 1.4 + rank_gap * 0.18 + max(home_gf, away_gf) + max(home_ga, away_ga) * 0.4), 2)
    tsi = round(((home_gf + away_gf) * 2.2 + league.get('match_over_15', 0.7) * 3), 2)
    uli = round((corridor * 7 + (league.get('match_under_35', 0.6) * 2.5)), 2)
    ltr = round((max(0, first_goal - 25) / 20) * 5 + corridor * 3, 2)
    mtd = round((1.2 if european_context else 0.4) + (0.6 if odds.get('source') != 'api_market_snapshot' else 0.2), 2)

    selected_odd = float(odds.get('selected_odd', 1.80))
    common_snapshot = {'FDI': fdi, 'TSI': tsi, 'ULI': uli, 'LTR': ltr, 'MTD': mtd}
    return [
        {
            'engine': 'O15_TEAM', 'score_raw': round(64 + fdi * 2.1 - mtd * 2, 2),
            'confidence_raw': 4 if fdi >= 4.0 else 3, 'risk_raw': 2 if mtd < 1.5 else 3,
            'edge_raw': '6.4%', 'odds': selected_odd, 'eligibility': True,
            'rationale_summary': 'Favoritismo e suporte ofensivo suficientes para Team Over 1.5.',
            'main_drivers': ['FDI forte', 'TSI favorável', 'perfil ofensivo suficiente'],
            'penalties': ['contexto parcial' if quality != 'clean' else 'penalização leve'],
            'favorite_team': favorite_team, 'indicator_snapshot': common_snapshot,
            'driver_scores': {'favoritism_strength': fdi, 'offensive_support': tsi, 'price_support': 6.4},
            'penalty_scores': {'market_risk': mtd},
        },
        {
            'engine': 'O15_GAME', 'score_raw': round(62 + tsi * 1.8 - mtd, 2),
            'confidence_raw': 4 if tsi >= 6.5 else 3, 'risk_raw': 2, 'edge_raw': '5.3%',
            'odds': max(1.35, selected_odd - 0.18), 'eligibility': True,
            'rationale_summary': 'Leitura global de golos favorável para Match Over 1.5.',
            'main_drivers': ['TSI combinado', 'liga favorável ao over', 'ritmo compatível'],
            'penalties': ['sem penalização crítica'], 'favorite_team': favorite_team,
            'indicator_snapshot': common_snapshot,
            'driver_scores': {'global_goal_push': tsi, 'league_support': league.get('match_over_15', 0.0), 'price_support': 5.3},
            'penalty_scores': {'market_risk': mtd},
        },
        {
            'engine': 'U35', 'score_raw': round(60 + uli * 2 + ltr - mtd, 2), 'confidence_raw': 3 if uli < 6.5 else 4,
            'risk_raw': 2, 'edge_raw': '4.9%', 'odds': 1.72, 'eligibility': True,
            'rationale_summary': 'Corredor curto e ritmo compatível com Under 3.5.',
            'main_drivers': ['ULI favorável', 'LTR favorável', 'corredor de scoreline'],
            'penalties': ['favorito ofensivo pode pressionar'], 'favorite_team': favorite_team,
            'indicator_snapshot': common_snapshot,
            'driver_scores': {'under_shape': uli, 'tempo_control': ltr, 'price_support': 4.9},
            'penalty_scores': {'market_risk': mtd},
        },
    ]

def run_smoke(sample_path: str) -> dict:
    provider = FileCentralProvider(sample_path=sample_path)
    bridge = ProviderBridge(provider=provider)
    central_payload = bridge.get_central_payload(878317)
    v12_input = build_v12_input(central_payload)
    candidates = _derive_candidates(v12_input)
    outputs = []
    for rank, candidate in enumerate(sorted(candidates, key=lambda x: x['score_raw'], reverse=True), start=1):
        outputs.append(build_market_pick_v11(
            module_version=MODULE_VERSION, fixture_id=v12_input['fixture_id'], match_label=v12_input['match_label'],
            competition=v12_input['competition'], kickoff_datetime=v12_input['kickoff_datetime'], engine=candidate['engine'],
            score_raw=candidate['score_raw'], confidence_raw=candidate['confidence_raw'], risk_raw=candidate['risk_raw'],
            edge_raw=candidate['edge_raw'], odds=candidate['odds'], eligibility=candidate['eligibility'],
            rationale_summary=candidate['rationale_summary'], main_drivers=candidate['main_drivers'], penalties=candidate['penalties'],
            data_quality_flag=v12_input['adapter_meta']['data_quality_flag'], module_rank_internal=rank, favorite_team=candidate['favorite_team'],
            indicator_snapshot=candidate['indicator_snapshot'], driver_scores=candidate['driver_scores'], penalty_scores=candidate['penalty_scores'],
            source_notes=v12_input['adapter_meta']['adapter_notes'],
        ))
    return {'provider_meta': central_payload.get('_provider_meta', {}), 'adapter_meta': v12_input['adapter_meta'], 'outputs': outputs}

if __name__ == '__main__':
    sample = Path(__file__).resolve().parent.parent / 'examples' / 'provider_real_input_sample.json'
    result = run_smoke(str(sample))
    print(json.dumps(result, indent=2, ensure_ascii=False))
