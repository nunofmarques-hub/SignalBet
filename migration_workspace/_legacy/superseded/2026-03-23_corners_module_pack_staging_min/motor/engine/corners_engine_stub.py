def run_corners_engine(adapted):
    est_total = round((adapted['home']['corners_for_home_away_avg'] + adapted['away']['corners_for_home_away_avg'] + adapted['home']['corners_against_home_away_avg'] + adapted['away']['corners_against_home_away_avg']) / 4, 2)
    direction = 'Over' if est_total >= 10.5 else 'Under'
    line = 9.5 if direction == 'Over' else 11.5
    score = 88.0 if direction == 'Over' else 74.0
    return {
        'fixture_id': adapted['fixture_id'],
        'game': f"{adapted['home_team_name']} vs {adapted['away_team_name']}",
        'competition': adapted['competition'],
        'market': f"{direction} {line} cantos jogo",
        'score': score,
        'confidence': 'Alta' if score >= 78 else 'Média',
        'risk': 'Baixo',
        'eligible': True,
        'estimated_total_corners': est_total,
        'main_drivers': ['produção combinada acima do padrão'] if direction == 'Over' else ['produção combinada abaixo do ideal'],
        'alerts': [],
        'team_scores': {'home': 76.86, 'away': 54.94},
        'game_profile': 'Volume Alto' if est_total >= 11.2 else 'Volume Médio/Alto',
        'market_bias': 'Over' if direction == 'Over' else 'Under',
        'line_grid': [{'market': f"{direction} {line} cantos", 'score': score, 'confidence': 'Alta', 'risk': 'Baixo', 'eligible': True}],
        'operational_conclusion': f"Jogo com perfil {'volume alto' if est_total >= 11.2 else 'volume médio/alto'} para cantos. O sinal principal aparece em {direction.lower()} {line} cantos jogo com força {'muito forte' if score >= 86 else 'forte'}."
    }
