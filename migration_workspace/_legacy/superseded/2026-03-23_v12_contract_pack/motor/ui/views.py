from __future__ import annotations

from html import escape
from typing import Any


def _html_head(title: str) -> str:
    return f"""
<!doctype html>
<html lang=\"pt\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>{escape(title)}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; background:#0f172a; color:#e2e8f0; }}
    h1,h2 {{ margin: 0 0 12px 0; }}
    .muted {{ color:#94a3b8; }}
    table {{ border-collapse: collapse; width: 100%; margin: 18px 0 28px 0; background:#111827; }}
    th, td {{ border:1px solid #334155; padding:10px; font-size:14px; text-align:left; vertical-align: top; }}
    th {{ background:#1e293b; }}
    .tag {{ display:inline-block; padding:2px 8px; border-radius:999px; background:#1d4ed8; color:white; font-size:12px; }}
    .ok {{ color:#86efac; }} .warn {{ color:#fde68a; }} .bad {{ color:#fca5a5; }}
    .wrap {{ max-width: 1450px; margin: 0 auto; }}
    .card {{ background:#111827; border:1px solid #334155; padding:16px; border-radius:12px; margin-bottom:18px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:10px; }}
    .mini {{ background:#0b1220; border:1px solid #334155; border-radius:10px; padding:10px; }}
    code {{ color:#c4b5fd; }}
  </style>
</head><body><div class=\"wrap\">"""


def _html_tail() -> str:
    return '</div></body></html>'


def render_toolbar(date_str: str) -> str:
    return ('<div class="card" style="border:2px solid #60a5fa;">'
            '<form method="get" style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">'
            '<label><strong>Data</strong></label>'
            f'<input type="date" name="date" value="{escape(date_str)}" style="padding:8px;border-radius:8px;border:1px solid #334155;background:#0f172a;color:#e2e8f0">'
            '<button type="submit" style="padding:8px 14px;border-radius:8px;border:1px solid #334155;background:#1d4ed8;color:white;cursor:pointer">Run</button>'
            '</form></div>')


def render_config_notes(api_config: dict[str, Any], source: str, fixture_count: int) -> str:
    key_status = 'OK' if api_config.get('api_key') else 'EM FALTA'
    odds_status = 'ATIVO' if api_config.get('odds_enabled') else 'DESLIGADO'
    hint = ''
    if fixture_count == 0 and source == 'CACHE' and not api_config.get('api_key'):
        hint = "<p class='warn'>Sem chave ativa e sem cache útil para esta data. Coloca <code>api.env.txt</code> na pasta raiz com <code>API_KEY=...</code> ou preenche <code>data/api_config.json</code>.</p>"
    return ('<div class="card"><h2>Configuração</h2>'
            f"<p class='muted'>API key: {escape(key_status)} · Odds automáticas: {escape(odds_status)}</p>"
            "<p class='muted'>Round 10 focada no polimento final do núcleo: U35 mais competitivo em jogos equilibrados, O15_TEAM ligeiramente suavizado no desempate e leitura de divergência por família.</p>" + hint + '</div>')


def render_best_of_day(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return '<div class="card"><h2>Best of Day</h2><p class="muted">Sem picks com edge mínimo nesta simulação.</p></div>'
    items = []
    for row in rows:
        items.append(
            f"<p><span class='tag'>{escape(row['market'])}</span> <strong>{escape(row['game'])}</strong> <span class='muted'>[{escape(row.get('engine',''))}]</span><br>"
            f"Score motor {row.get('engine_score',0.0):.2f} · Prob. {round(row['probability']*100,1)}% · Odd Justa {row['fair_odd']} · Mercado {row['market_odd']} · Edge {round(row['edge']*100,1)}%<br>"
            f"<span class='muted'>{escape(row.get('reason',''))}</span></p>"
        )
    return '<div class="card"><h2>Best of Day</h2>' + ''.join(items) + '</div>'


def render_v12_indicator_table(rows: list[dict[str, Any]]) -> str:
    body = []
    for row in rows:
        favorite = row.get('favorite_team') or 'Equilibrado'
        body.append('<tr>'
                    f"<td>{escape(row['league'])}</td><td>{escape(row['game'])}</td><td>{row['home_tsi']}</td><td>{row['away_tsi']}</td><td>{row['fdi']}</td><td>{row['over_game_strength']}</td><td>{row['uli']}</td><td>{row['ltr']}</td><td>{row['mtd']}</td><td>{escape(favorite)}</td>"
                    '</tr>')
    return ('<div class="card"><h2>Round 10 · Indicadores núcleo</h2><table><thead><tr><th>Liga</th><th>Jogo</th><th>TSI Casa</th><th>TSI Fora</th><th>FDI</th><th>O15 Jogo</th><th>ULI</th><th>LTR</th><th>MTD</th><th>Favorito</th></tr></thead><tbody>' + ''.join(body) + '</tbody></table></div>')


def render_v12_market_table(rows: list[dict[str, Any]]) -> str:
    body = []
    for row in rows:
        label = row.get('value_label', 'NO VALUE')
        cls = 'ok' if 'STRONG' in label else 'warn' if label == 'VALUE' else 'bad'
        body.append('<tr>'
                    f"<td>{escape(row['game'])}</td><td>{escape(row['market'])}</td><td>{escape(row.get('engine',''))}</td><td>{row.get('engine_score',0.0):.2f}</td><td>{round(row['probability']*100,1)}%</td><td>{row['fair_odd']}</td><td>{row['market_odd']}</td><td>{round(row['edge']*100,1)}%</td><td class=\"{cls}\">{escape(label)}</td>"
                    '</tr>')
    return ('<div class="card"><h2>Mercados núcleo v12</h2><table><thead><tr><th>Jogo</th><th>Mercado</th><th>Motor</th><th>Score</th><th>Prob.</th><th>Odd Justa</th><th>Odd Mercado</th><th>Edge</th><th>Classe</th></tr></thead><tbody>' + ''.join(body) + '</tbody></table></div>')


def render_comparison(rows: list[dict[str, Any]], summary: dict[str, int]) -> str:
    body = []
    for row in rows:
        alignment = row.get('alignment', '')
        cls = 'ok' if alignment == 'Coincidem' else 'warn' if alignment in {'Divergem', 'Só v12', 'Só v11.5'} else 'muted'
        body.append('<tr>'
                    f"<td>{escape(row['game'])}</td><td>{escape(row.get('v11_market') or '—')}</td><td>{round(row.get('v11_edge',0.0)*100,1)}%</td><td>{escape(row.get('v12_market') or '—')}</td><td>{escape(row.get('v12_engine') or '—')}</td><td>{round(row.get('v12_edge',0.0)*100,1)}%</td><td class=\"{cls}\">{escape(alignment)}</td><td>{escape(row.get('blocker') or '—')}</td><td>{'Sim' if row.get('near_miss') else 'Não'}</td><td>{escape(row.get('note',''))}</td>"
                    '</tr>')
    summary_html = ('<div class="grid">'
                    f"<div class='mini'><strong>Coincidem</strong><br>{summary.get('coincidem',0)}</div>"
                    f"<div class='mini'><strong>Divergem</strong><br>{summary.get('divergem',0)}</div>"
                    f"<div class='mini'><strong>Só v11.5</strong><br>{summary.get('so_v11',0)}</div>"
                    f"<div class='mini'><strong>Só v12</strong><br>{summary.get('so_v12',0)}</div>"
                    f"<div class='mini'><strong>Sem pick</strong><br>{summary.get('sem_pick',0)}</div>"
                    f"<div class='mini'><strong>Quase entrou</strong><br>{summary.get('quase_entrou',0)}</div></div>")
    return ('<div class="card"><h2>Round 10 · Comparador v11.5 vs v12</h2>' + summary_html + '<table><thead><tr><th>Jogo</th><th>v11.5</th><th>Edge v11</th><th>v12</th><th>Motor v12</th><th>Edge v12</th><th>Leitura</th><th>Família</th><th>Bloqueio</th><th>Quase?</th><th>Nota</th></tr></thead><tbody>' + ''.join(body) + '</tbody></table></div>')


def render_v12_page(date_str: str, source: str, fixture_count: int, indicator_rows: list[dict[str, Any]], market_rows: list[dict[str, Any]], best_rows: list[dict[str, Any]], api_config: dict[str, Any], comparison_rows: list[dict[str, Any]], comparison_summary: dict[str, int]) -> str:
    return (_html_head('ABC PRO v12 Sandbox · Round 10')
            + f"<h1>ABC PRO · v12 Sandbox <span class='tag'>Round 10</span></h1><p class='muted'>Data {escape(date_str)} · Fonte {escape(source)} · Jogos elegíveis {fixture_count}</p>"
            + render_toolbar(date_str)
            + render_config_notes(api_config, source, fixture_count)
            + render_best_of_day(best_rows)
            + render_comparison(comparison_rows, comparison_summary)
            + render_v12_indicator_table(indicator_rows)
            + render_v12_market_table(market_rows)
            + _html_tail())
