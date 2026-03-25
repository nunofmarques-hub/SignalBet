from __future__ import annotations

from typing import Any

from core.settings import load_team_ratings
from models.match import Match

TEAM_RATINGS = load_team_ratings()

LEAGUE_PROFILE = {
    'Bundesliga': {'attack': 7.4, 'defense': 5.6, 'tempo': 7.4, 'liga_score': 6.2},
    'Premier League': {'attack': 7.0, 'defense': 6.1, 'tempo': 6.9, 'liga_score': 6.0},
    'La Liga': {'attack': 6.6, 'defense': 6.7, 'tempo': 6.2, 'liga_score': 6.7},
    'Serie A': {'attack': 6.8, 'defense': 6.5, 'tempo': 6.4, 'liga_score': 7.1},
    'Ligue 1': {'attack': 6.9, 'defense': 6.0, 'tempo': 6.8, 'liga_score': 6.1},
    'Primeira Liga': {'attack': 6.4, 'defense': 6.5, 'tempo': 6.0, 'liga_score': 7.0},
    'Eredivisie': {'attack': 7.7, 'defense': 5.2, 'tempo': 7.7, 'liga_score': 5.8},
    'Jupiler Pro League': {'attack': 6.9, 'defense': 5.9, 'tempo': 6.9, 'liga_score': 6.0},
    'Super League': {'attack': 6.6, 'defense': 5.8, 'tempo': 6.6, 'liga_score': 5.9},
}


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def normalize_0_10(value: float, min_value: float, max_value: float) -> float:
    if max_value <= min_value:
        return 5.0
    clipped = clamp(value, min_value, max_value)
    return round(((clipped - min_value) / (max_value - min_value)) * 10.0, 2)


def base_team_strength(team_name: str) -> float:
    key = team_name.strip().lower()
    if key in TEAM_RATINGS:
        return float(TEAM_RATINGS[key])
    ascii_score = sum(ord(char) for char in key if char.isalpha())
    return round(5.35 + (ascii_score % 210) / 100.0, 2)


def get_league_context(league_name: str) -> dict[str, float]:
    return LEAGUE_PROFILE.get(league_name, {'attack': 6.5, 'defense': 6.2, 'tempo': 6.4, 'liga_score': 6.2})


def estimate_favorite(home_team: str, away_team: str) -> tuple[str | None, float, float, float]:
    home_strength = base_team_strength(home_team) + 0.32
    away_strength = base_team_strength(away_team)
    margin = round(home_strength - away_strength, 2)
    if abs(margin) < 0.20:
        return None, round(home_strength, 2), round(away_strength, 2), margin
    return (home_team if margin > 0 else away_team), round(home_strength, 2), round(away_strength, 2), margin


def compute_attack_score(team_name: str, league_context: dict[str, float], is_home: bool) -> float:
    base = base_team_strength(team_name)
    adjusted = base * 0.70 + league_context['attack'] * 0.20 + league_context['tempo'] * 0.10 + (0.22 if is_home else 0.0)
    return normalize_0_10(adjusted, 4.8, 9.4)


def compute_defense_weakness(opponent_name: str, league_context: dict[str, float]) -> float:
    opponent_strength = base_team_strength(opponent_name)
    weakness_proxy = (10.3 - opponent_strength) * 0.62 + (10.0 - league_context['defense']) * 0.38
    return normalize_0_10(weakness_proxy, 1.6, 5.6)


def compute_defensive_solidity(team_name: str, league_context: dict[str, float], is_home: bool) -> float:
    base = base_team_strength(team_name)
    adjusted = base * 0.50 + league_context['defense'] * 0.40 + (0.18 if is_home else 0.0)
    return normalize_0_10(adjusted, 4.5, 8.9)


def compute_defensive_context(team_name: str, opponent_name: str, league_context: dict[str, float]) -> float:
    team_strength = base_team_strength(team_name)
    opponent_strength = base_team_strength(opponent_name)
    context_score = team_strength * 0.42 + league_context['defense'] * 0.38 + (10.0 - opponent_strength) * 0.20
    return normalize_0_10(context_score, 4.0, 8.5)


def compute_tsi(team_name: str, opponent_name: str, league_context: dict[str, float], is_home: bool) -> float:
    attack_score = compute_attack_score(team_name, league_context, is_home=is_home)
    defense_weakness = compute_defense_weakness(opponent_name, league_context)
    return round(attack_score * 0.60 + defense_weakness * 0.40, 2)


def compute_dci(team_name: str, opponent_name: str, league_context: dict[str, float], is_home: bool) -> float:
    solidity = compute_defensive_solidity(team_name, league_context, is_home=is_home)
    context = compute_defensive_context(team_name, opponent_name, league_context)
    return round(solidity * 0.70 + context * 0.30, 2)


def build_match_indicators(match: Match) -> dict[str, Any]:
    league_context = get_league_context(match.league)
    favorite_team, home_power, away_power, favorite_margin = estimate_favorite(match.home_team, match.away_team)
    home_tsi = compute_tsi(match.home_team, match.away_team, league_context, is_home=True)
    away_tsi = compute_tsi(match.away_team, match.home_team, league_context, is_home=False)
    home_dci = compute_dci(match.home_team, match.away_team, league_context, is_home=True)
    away_dci = compute_dci(match.away_team, match.home_team, league_context, is_home=False)

    attack_total = round(home_tsi + away_tsi, 2)
    defense_total = round(home_dci + away_dci, 2)
    home_attack_signal = round(home_tsi - away_dci * 0.34, 2)
    away_attack_signal = round(away_tsi - home_dci * 0.34, 2)
    balance_gap = round(abs(home_attack_signal - away_attack_signal), 2)
    risk_balance = round(max(0.0, 1.15 - balance_gap), 2)

    liga_score = round(league_context.get('liga_score', 6.2), 2)
    tpd = round(clamp((attack_total - defense_total) + league_context['tempo'] * 0.30, 0.0, 10.0), 2)
    ipo_home = round(clamp(home_attack_signal + league_context['attack'] * 0.28, 0.0, 10.0), 2)
    ipo_away = round(clamp(away_attack_signal + league_context['attack'] * 0.28, 0.0, 10.0), 2)
    ipo_combined = round((ipo_home + ipo_away) / 2.0, 2)
    tli = round(clamp(8.7 - abs(2.10 - (1.55 + abs(favorite_margin) * 0.22)), 0.0, 10.0), 2)
    mtd = round(clamp(risk_balance * 4.2 + (0.8 if favorite_team is None else 0.0), 0.0, 10.0), 2)

    if favorite_team == match.home_team:
        fav_tsi = home_tsi
        fav_ipo = ipo_home
        opp_dci = away_dci
        opp_fragility = round(clamp(10.0 - away_dci, 0.0, 10.0), 2)
        hfa = 1.25
    elif favorite_team == match.away_team:
        fav_tsi = away_tsi
        fav_ipo = ipo_away
        opp_dci = home_dci
        opp_fragility = round(clamp(10.0 - home_dci, 0.0, 10.0), 2)
        hfa = 0.25
    else:
        fav_tsi = max(home_tsi, away_tsi)
        fav_ipo = max(ipo_home, ipo_away)
        opp_dci = min(home_dci, away_dci)
        opp_fragility = round(clamp(10.0 - opp_dci, 0.0, 10.0), 2)
        hfa = 0.0

    favorite_dominance = round(clamp(abs(favorite_margin) * 3.2 + max(home_attack_signal, away_attack_signal) * 0.55, 0.0, 10.0), 2)
    fdi = round(clamp(liga_score * 0.10 + hfa * 0.80 + tpd * 0.16 + fav_ipo * 0.18 + fav_tsi * 0.18 + favorite_dominance * 0.18 + opp_fragility * 0.16 - mtd * 0.12, 0.0, 10.0), 2)
    uli = round(clamp(defense_total * 0.32 + liga_score * 0.16 + (10.0 - ipo_combined) * 0.20 + balance_gap * 0.08 + tli * 0.14 - mtd * 0.08, 0.0, 10.0), 2)
    ltr = round(clamp(defense_total * 0.24 + (10.0 - league_context['tempo']) * 0.18 + (10.0 - tpd) * 0.20 + balance_gap * 0.18 + tli * 0.12, 0.0, 10.0), 2)
    over_game_strength = round(clamp(attack_total * 0.26 + ipo_combined * 0.24 + tpd * 0.22 + league_context['tempo'] * 0.16 + liga_score * 0.08 + tli * 0.04 - mtd * 0.10, 0.0, 10.0), 2)

    return {
        'fixture_id': match.fixture_id,
        'league': match.league,
        'country': match.country,
        'league_id': match.league_id,
        'season': match.season,
        'game': match.game_label,
        'home_team': match.home_team,
        'away_team': match.away_team,
        'favorite_team': favorite_team,
        'favorite_margin': favorite_margin,
        'home_power': home_power,
        'away_power': away_power,
        'home_tsi': home_tsi,
        'away_tsi': away_tsi,
        'home_dci': home_dci,
        'away_dci': away_dci,
        'attack_total': attack_total,
        'defense_total': defense_total,
        'home_attack_signal': home_attack_signal,
        'away_attack_signal': away_attack_signal,
        'balance_gap': balance_gap,
        'favorite_dominance': favorite_dominance,
        'risk_balance': risk_balance,
        'liga_score': liga_score,
        'hfa': round(hfa, 2),
        'tpd': tpd,
        'ipo_home': ipo_home,
        'ipo_away': ipo_away,
        'ipo_combined': ipo_combined,
        'tli': tli,
        'mtd': mtd,
        'fdi': fdi,
        'uli': uli,
        'ltr': ltr,
        'over_game_strength': over_game_strength,
        'context': league_context,
        'source': match.source,
    }
