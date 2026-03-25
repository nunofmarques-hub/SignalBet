def eval_case(adapted):
    h=adapted['home']; a=adapted['away']; c=adapted['context']
    est=((h['corners_for_home_away_avg']+a['corners_for_home_away_avg']+h['corners_against_home_away_avg']+a['corners_against_home_away_avg'])/2.0)+((c['expected_pace_shape']-50)/18.0)
    est=round(max(0.0,est),2)
    prod=(h['corners_for_avg']*10+h['shots_avg']*4+h['shots_on_target_avg']*8+h['final_third_pressure']+h['crossing_volume']+h['territorial_proxy'])/6
    prod2=(a['corners_for_avg']*10+a['shots_avg']*4+a['shots_on_target_avg']*8+a['final_third_pressure']+a['crossing_volume']+a['territorial_proxy'])/6
    conc=(h['corners_against_avg']*10+a['corners_against_avg']*10+h['total_match_corners_avg']*5+a['total_match_corners_avg']*5)/4
    freq=(h['hit_rate_over_8_5']*100+h['hit_rate_over_9_5']*100+h['hit_rate_over_10_5']*100+a['hit_rate_over_8_5']*100+a['hit_rate_over_9_5']*100+a['hit_rate_over_10_5']*100)/6
    qual=(min(100,h['sample_size']*10)+min(100,a['sample_size']*10)+h['opponent_adjustment_quality']+a['opponent_adjustment_quality'])/4
    over_raw=round(min(100,max(0,(prod*0.26+prod2*0.22+conc*0.20+freq*0.16+c['expected_pace_shape']*0.10+c['expected_game_state_volatility']*0.03+qual*0.03))),2)
    under_raw=round(min(100,max(0,((100-prod)*0.18+(100-prod2)*0.16+(100-conc)*0.18+(100-freq)*0.12+(100-c['expected_pace_shape'])*0.14+(100-c['expected_game_state_volatility'])*0.12+qual*0.10))),2)
    direction='Over' if over_raw>=under_raw else 'Under'
    line=10.5 if direction=='Over' and est>=11.2 else (9.5 if direction=='Over' and est>=10.0 else (8.5 if direction=='Over' else (9.5 if est<=8.8 else (10.5 if est<=10.0 else 11.5))))
    diff=est-line
    line_strength=round(max(0,min(100,(52+diff*20) if direction=='Over' else (52+(-diff)*20))),2)
    score_pre=round((over_raw if direction=='Over' else under_raw)*0.66 + line_strength*0.34,2)
    alerts=[]; exclusions=[]
    if c['low_data_quality']: exclusions.append('qualidade de dados insuficiente')
    if h['sample_size']<4 or a['sample_size']<4: exclusions.append('amostra insuficiente')
    if h['opponent_adjustment_quality']<35 or a['opponent_adjustment_quality']<35: exclusions.append('ajustamento por adversário demasiado fraco')
    if c['likely_rotation']: alerts.append('rotação provável')
    if c['unstable_tactical_profile']: alerts.append('perfil tático instável')
    penalties=[]; final=score_pre
    if 'rotação provável' in alerts: final-=6; penalties.append('penalty_rotacao')
    if 'perfil tático instável' in alerts: final-=8; penalties.append('penalty_instabilidade')
    if exclusions: final-=25; penalties+=['penalty_exclusion::'+x for x in exclusions]
    final=round(max(0,final),2)
    band='Elite' if final>=86 else ('Forte' if final>=72 else ('Observação' if final>=58 else 'Rejeitar'))
    status='candidate' if (not exclusions and band in ('Elite','Forte')) else ('watchlist' if (not exclusions and band=='Observação') else 'rejected')
    conf_composite=final*0.7+line_strength*0.3-(6 if alerts else 0)
    confidence='Alta' if conf_composite>=80 else ('Média' if conf_composite>=64 else 'Baixa')
    risk_score=100 - (final*0.55 + line_strength*0.25 + (0 if exclusions else 12) + (0 if not alerts else 6))
    risk='Baixo' if risk_score<=28 else ('Médio' if risk_score<=48 else 'Alto')
    profile='Volume Alto' if est>=11.2 else ('Volume Médio/Alto' if est>=9.6 else ('Volume Médio' if est>=8.3 else 'Volume Baixo'))
    bias='Over' if diff>=1.2 else ('Under' if diff<=-1.2 else 'Zona Cinzenta')
    if (bias=='Over' and direction=='Under') or (bias=='Under' and direction=='Over'): alerts.append('leitura contraditória entre grelha e contexto')
    if abs(est-line)<=0.8: alerts.append('mercado de fronteira')
    return {'fixture_id': adapted['fixture_id'],'game': f"{adapted['home_team_name']} vs {adapted['away_team_name']}",'competition': adapted['competition'],'market': f"{direction} {line} cantos jogo",'score': final,'confidence': confidence,'risk': risk,'eligible': status!='rejected','candidate_status': status,'band': band,'estimated_total_corners': est,'main_drivers': ['produção combinada acima do padrão','perfil de concessão favorável','contexto de jogo favorável a volume'] if direction=='Over' else ['produção combinada abaixo do ideal','perfil de concessão baixo'],'alerts': alerts+exclusions,'penalty_codes': penalties,'team_scores': {'home': round((h['corners_for_avg']*10+h['final_third_pressure'])/2,2), 'away': round((a['corners_for_avg']*10+a['final_third_pressure'])/2,2)},'game_profile': profile,'market_bias': bias,'line_grid': [{'market': f"{direction} 8.5 cantos",'score': round(max(0,min(100,(52+((est-8.5)*20) if direction=='Over' else (52+((8.5-est)*20))))),2)}, {'market': f"{direction} 9.5 cantos",'score': round(max(0,min(100,(52+((est-9.5)*20) if direction=='Over' else (52+((9.5-est)*20))))),2)}, {'market': f"{direction} 10.5 cantos",'score': round(max(0,min(100,(52+((est-10.5)*20) if direction=='Over' else (52+((10.5-est)*20))))),2)}, {'market': f"{direction} 11.5 cantos",'score': round(max(0,min(100,(52+((est-11.5)*20) if direction=='Over' else (52+((11.5-est)*20))))),2)}],'rationale': {'score_base_over': over_raw,'score_base_under': under_raw,'selected_direction': direction,'selected_line': line,'line_strength': line_strength,'score_pre_penalty': score_pre,'band': band,'candidate_status': status,'confidence_logic': confidence,'risk_logic': risk},'operational_conclusion': f"Jogo com perfil {profile.lower()} para cantos. A linha principal escolhida foi {line} porque a projeção estimada ficou em {est}. O score final caiu em banda {band.lower()}, a confiança ficou {confidence.lower()} e o risco ficou {risk.lower()}."}
