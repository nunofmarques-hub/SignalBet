from __future__ import annotations

import json
import threading
import webbrowser
from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from core.comparator import build_comparison_rows, build_comparison_summary
from core.data_layer import build_match_objects, get_fixtures
from core.decision_engine import analyze_match_markets, select_best_of_day
from core.explain import build_pick_reason
from core.indicators import build_match_indicators
from core.odds_layer import resolve_market_odd
from core.probability_engine import build_market_probabilities
from core.settings import load_api_config
from core.value_engine import enrich_market_with_value
from storage.json_store import data_path, ensure_json_file, save_json
from ui.views import render_v12_page

try:
    import main as v11_main
except Exception:
    v11_main = None

V12_INDICATORS_FILE = data_path('v12_indicators.json')
V12_ANALYSIS_FILE = data_path('v12_analysis.json')


def bootstrap_support_files() -> None:
    api_config = load_api_config()
    ensure_json_file(data_path('api_config.json'), api_config)
    ensure_json_file(data_path('market_odds.json'), {})


def run_v12(date_str: str) -> dict:
    bootstrap_support_files()
    api_config = load_api_config()
    fixtures, source = get_fixtures(date_str)
    matches = build_match_objects(fixtures, source=source)

    indicator_rows = []
    market_rows = []
    best_per_match = []
    match_analysis = []

    for match in matches:
        indicators = build_match_indicators(match)
        indicator_rows.append(indicators)

        probabilities = build_market_probabilities(indicators, context=indicators.get('context'))
        enriched = []
        for row in probabilities:
            market_odd, odd_source = resolve_market_odd(match.fixture_id, row['market'])
            item = enrich_market_with_value(row, market_odd=market_odd, odd_source=odd_source)
            item['game'] = match.game_label
            item['fixture_id'] = match.fixture_id
            item['favorite_margin'] = indicators.get('favorite_margin', 0.0)
            item['fdi'] = indicators.get('fdi', 0.0)
            item['uli'] = indicators.get('uli', 0.0)
            item['ltr'] = indicators.get('ltr', 0.0)
            item['over_game_strength'] = indicators.get('over_game_strength', 0.0)
            enriched.append(item)
            market_rows.append(item)

        for item in enriched:
            item['risk_balance'] = indicators.get('risk_balance', 0.0)

        analysis = analyze_match_markets(enriched)
        match_analysis.append({
            'game': match.game_label,
            'league': match.league,
            'status': analysis.get('status', ''),
            'detail': analysis.get('detail', ''),
            'near_miss': analysis.get('near_miss', False),
        })

        best_market = analysis.get('selected')
        if best_market:
            best_market = dict(best_market)
            best_market['game'] = match.game_label
            best_market['league'] = match.league
            best_market['reason'] = build_pick_reason(match.to_dict(), best_market, indicators)
            best_per_match.append(best_market)

    best_of_day = select_best_of_day(best_per_match, limit=2)

    v11_rows = []
    if v11_main is not None:
        try:
            v11_rows, _best, _source, _count = v11_main.run_engine(date_str)
        except Exception:
            v11_rows = []
    comparison_rows = build_comparison_rows(v11_rows, best_per_match, match_analysis)
    comparison_summary = build_comparison_summary(comparison_rows)

    payload = {
        'date': date_str,
        'source': source,
        'fixture_count': len(fixtures),
        'api_config': {
            'api_key': '***' if api_config.get('api_key') else '',
            'odds_enabled': bool(api_config.get('odds_enabled')),
        },
        'indicator_rows': indicator_rows,
        'market_rows': market_rows,
        'best_of_day': best_of_day,
        'comparison_rows': comparison_rows,
        'comparison_summary': comparison_summary,
    }
    save_json(V12_INDICATORS_FILE, {'date': date_str, 'rows': indicator_rows, 'source': source})
    save_json(V12_ANALYSIS_FILE, payload)
    return payload


class Handler(BaseHTTPRequestHandler):
    def _json(self, payload: dict) -> None:
        raw = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        requested_date = query.get('date', [date.today().isoformat()])[0]

        if parsed.path == '/':
            payload = run_v12(requested_date)
            html = render_v12_page(
                requested_date,
                payload['source'],
                payload['fixture_count'],
                payload['indicator_rows'],
                payload['market_rows'],
                payload['best_of_day'],
                payload['api_config'],
                payload['comparison_rows'],
                payload['comparison_summary'],
            )
            raw = html.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)
            return

        if parsed.path == '/api':
            self._json(run_v12(requested_date))
            return

        self.send_response(404)
        self.end_headers()


def main() -> None:
    bootstrap_support_files()
    threading.Timer(1, lambda: webbrowser.open('http://127.0.0.1:8018')).start()
    HTTPServer(('127.0.0.1', 8018), Handler).serve_forever()


if __name__ == '__main__':
    main()
