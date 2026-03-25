def adapt_from_trunk(fixture_obj, fixture_statistics, context):
    return {'fixture_id': fixture_obj['fixture']['id'], 'competition': fixture_obj['league']['name'], 'home_team_name': fixture_obj['teams']['home']['name'], 'away_team_name': fixture_obj['teams']['away']['name'], 'context': context, 'fixture_statistics': fixture_statistics}
