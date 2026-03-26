from __future__ import annotations

from typing import Any


def _normalize_market(market: str | None) -> str | None:
    if not market or market == 'Sem mercado':
        return None
    return market


def _engine_family(market: str | None) -> str:
    if not market:
        return ''
    if market.endswith('Over 1.5') and market != 'Over 1.5 jogo':
        return 'O15 equipa'
    if market == 'Over 1.5 jogo':
        return 'O15 jogo'
    if market == 'Under 3.5':
        return 'Under 3.5'
    return market


def _classify_alignment(v11_market: str | None, v12_market: str | None) -> str:
    v11_market = _normalize_market(v11_market)
    v12_market = _normalize_market(v12_market)
    if not v11_market and not v12_market:
        return 'Sem pick em ambos'
    if v11_market and v12_market and v11_market == v12_market:
        return 'Coincidem'
    if v11_market and not v12_market:
        return 'Só v11.5'
    if not v11_market and v12_market:
        return 'Só v12'
    return 'Divergem'



def _divergence_family(v11_row: dict[str, Any] | None, v12_row: dict[str, Any] | None) -> str:
    v11_market = _normalize_market(v11_row.get('market') if v11_row else None)
    v12_market = _normalize_market(v12_row.get('market') if v12_row else None)
    if v11_market and v12_market and v11_market == v12_market:
        return 'Alinhado'
    if v12_row and v12_row.get('engine') == 'U35':
        return 'Conservador under'
    if v12_row and v12_row.get('engine') == 'O15_TEAM':
        return 'Ofensivo dirigido'
    if v12_row and v12_row.get('engine') == 'O15_GAME':
        return 'Ofensivo global'
    if v11_market and not v12_market:
        return 'Exclusão por filtro'
    if v12_market and not v11_market:
        return 'Novo setup v12'
    return 'Sem ação'

def _build_note(v11_row: dict[str, Any] | None, v12_row: dict[str, Any] | None, analysis: dict[str, Any] | None) -> str:
    v11_market = _normalize_market(v11_row.get('market') if v11_row else None)
    v12_market = _normalize_market(v12_row.get('market') if v12_row else None)
    v11_edge = (v11_row or {}).get('edge', 0.0)
    v12_edge = (v12_row or {}).get('edge', 0.0)
    if v11_market and v12_market:
        if v11_market == v12_market:
            return 'Leitura semelhante entre baseline e sandbox.'
        if _engine_family(v11_market) == _engine_family(v12_market):
            return 'Mesma família de mercado, execução diferente.'
        if v12_row.get('engine') == 'U35':
            return 'Divergência por leitura conservadora do motor under.'
        if v12_row.get('engine') == 'O15_TEAM':
            return 'Divergência por motor ofensivo dirigido à equipa favorita.'
        if v12_row.get('engine') == 'O15_GAME':
            return 'Divergência por leitura global de golos no jogo.'
        return 'Motores diferentes com leitura própria.'
    if v11_market and not v12_market:
        if analysis:
            prefix = 'v12 quase entrou: ' if analysis.get('near_miss') else 'v12 bloqueou: '
            return prefix + (analysis.get('detail') or analysis.get('status') or 'sem detalhe.')
        return 'v12 descartou nos filtros base.'
    if v12_market and not v11_market:
        if v12_edge >= 0.06:
            return 'v12 encontrou setup forte no núcleo de 3 motores.'
        return 'v12 encontrou setup marginal no núcleo de 3 motores.'
    return 'Sem leitura acionável.'


def build_comparison_rows(v11_rows: list[dict[str, Any]], v12_best_rows: list[dict[str, Any]], match_analysis: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    by_game: dict[str, dict[str, Any]] = {}
    for row in v11_rows:
        by_game.setdefault(row.get('game', ''), {})['v11'] = row
    for row in v12_best_rows:
        by_game.setdefault(row.get('game', ''), {})['v12'] = row
    for row in (match_analysis or []):
        by_game.setdefault(row.get('game', ''), {})['analysis'] = row

    rows: list[dict[str, Any]] = []
    for game in sorted(by_game):
        pair = by_game[game]
        v11 = pair.get('v11')
        v12 = pair.get('v12')
        analysis = pair.get('analysis', {})
        rows.append({
            'game': game,
            'league': (v12 or v11 or {}).get('league', ''),
            'v11_market': v11.get('market') if v11 else '',
            'v11_edge': v11.get('edge', 0.0) if v11 else 0.0,
            'v11_value': v11.get('value', 'NO VALUE') if v11 else '',
            'v12_market': v12.get('market') if v12 else '',
            'v12_edge': v12.get('edge', 0.0) if v12 else 0.0,
            'v12_value': v12.get('value_label', 'NO VALUE') if v12 else '',
            'v12_engine': v12.get('engine', '') if v12 else '',
            'divergence_family': _divergence_family(v11, v12),
            'alignment': _classify_alignment(v11.get('market') if v11 else None, v12.get('market') if v12 else None),
            'blocker': analysis.get('status', ''),
            'near_miss': bool(analysis.get('near_miss')),
            'note': _build_note(v11, v12, analysis),
        })
    return rows


def build_comparison_summary(rows: list[dict[str, Any]]) -> dict[str, int]:
    summary = {'coincidem': 0, 'divergem': 0, 'so_v11': 0, 'so_v12': 0, 'sem_pick': 0, 'quase_entrou': 0}
    for row in rows:
        alignment = row.get('alignment')
        if alignment == 'Coincidem':
            summary['coincidem'] += 1
        elif alignment == 'Divergem':
            summary['divergem'] += 1
        elif alignment == 'Só v11.5':
            summary['so_v11'] += 1
        elif alignment == 'Só v12':
            summary['so_v12'] += 1
        else:
            summary['sem_pick'] += 1
        if row.get('near_miss'):
            summary['quase_entrou'] += 1
    return summary
