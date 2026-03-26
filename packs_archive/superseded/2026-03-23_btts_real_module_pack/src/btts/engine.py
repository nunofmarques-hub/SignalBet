from __future__ import annotations
from .models import TeamProfile, MatchRecord, MarketResult


class BTTSEngine:
    """Versão mínima executável do motor BTTS para pack de teste.
    Consome output da Data/API Layer central já tratado em match master + team profiles.
    """

    def evaluate(self, match: MatchRecord, home: TeamProfile, away: TeamProfile) -> MarketResult:
        bos = self._bos(home, away)
        bvs = self._bvs(home, away)
        ami = self._ami(home, away)
        tsi = self._tsi(home, away)
        fgt = self._fgt(match)
        xg_gap = self._xg_gap(match, home, away)
        sbi = self._sbi(home, away)

        penalties: list[str] = []
        score = (
            0.28 * bos +
            0.28 * bvs +
            0.12 * ami +
            0.08 * fgt +
            0.08 * tsi +
            0.08 * xg_gap +
            0.08 * sbi
        )

        if min(home.score_rate_1plus, away.score_rate_1plus) < 0.45:
            score -= 10
            penalties.append('underdog_or_side_offensively_weak')
        if abs(home.bos_score_lite - away.bos_score_lite) > 0.45:
            score -= 6
            penalties.append('offensive_asymmetry')
        if match.halftime_0_0 and (match.first_goal_minute or 999) > 60:
            score -= 8
            penalties.append('deadlock_risk')

        score = max(0.0, min(100.0, round(score, 2)))
        confidence = 5 if score >= 80 else 4 if score >= 70 else 3 if score >= 60 else 2 if score >= 45 else 1
        risk = 1 if score >= 80 else 2 if score >= 70 else 3 if score >= 55 else 4
        edge = 'strong' if score >= 78 else 'acceptable' if score >= 62 else 'weak'
        eligibility = score >= 60
        match_label = f"{match.home_team_name} vs {match.away_team_name}"
        drivers = []
        if bos >= 65: drivers.append('bos_supportive')
        if bvs >= 65: drivers.append('bvs_supportive')
        if fgt >= 60: drivers.append('fgt_positive')
        if tsi >= 60: drivers.append('tsi_stable_enough')
        if xg_gap >= 60: drivers.append('xg_gap_positive')
        summary = self._summary(score, penalties)
        return MarketResult(
            fixture_id=match.fixture_id,
            match_label=match_label,
            score_raw=score,
            confidence_raw=confidence,
            risk_raw=risk,
            edge_raw=edge,
            eligibility=eligibility,
            rationale_summary=summary,
            main_drivers=drivers,
            penalties=penalties,
            data_quality_flag='partial',
            module_specific_payload={
                'btts_direction': 'yes',
                'scoring_support': {'bos': round(bos,2), 'ami_bilateral': round(ami,2), 'xg_gap_aggregated': round(xg_gap,2)},
                'concession_support': {'bvs': round(bvs,2), 'fgt_btts': round(fgt,2), 'sbi': round(sbi,2)},
                'tsi_bilateral': round(tsi,2),
            }
        )

    def _bos(self, home: TeamProfile, away: TeamProfile) -> float:
        return min(100.0, 100 * (0.30 * ((home.bos_score_lite + away.bos_score_lite) / 2) + 0.35 * ((home.score_rate_1plus + away.score_rate_1plus) / 2) + 0.35 * (((home.goals_for/max(home.matches,1)) + (away.goals_for/max(away.matches,1))) / 2 / 2.0)))

    def _bvs(self, home: TeamProfile, away: TeamProfile) -> float:
        return min(100.0, 100 * (0.40 * ((home.bvs_score_lite + away.bvs_score_lite) / 2) + 0.30 * ((home.concede_rate_1plus + away.concede_rate_1plus) / 2) + 0.30 * ((home.clean_sheet_inverse_rate + away.clean_sheet_inverse_rate) / 2)))

    def _ami(self, home: TeamProfile, away: TeamProfile) -> float:
        return min(100.0, 100 * ((home.ami_score_lite + away.ami_score_lite) / 2) / 1.5)

    def _tsi(self, home: TeamProfile, away: TeamProfile) -> float:
        return min(100.0, 100 * ((home.tsi_score_lite + away.tsi_score_lite) / 2) / 1.2)

    def _sbi(self, home: TeamProfile, away: TeamProfile) -> float:
        gap = abs(home.goals_for / max(home.matches,1) - away.goals_for / max(away.matches,1))
        return max(0.0, 100 - gap * 40)

    def _fgt(self, match: MatchRecord) -> float:
        score = 50.0
        if match.goal_until_30:
            score += 20
        if match.response_after_conceding:
            score += 15
        if match.halftime_0_0:
            score -= 15
        if match.first_goal_minute is not None:
            if match.first_goal_minute <= 15:
                score += 10
            elif match.first_goal_minute >= 60:
                score -= 10
        return max(0.0, min(100.0, score))

    def _xg_gap(self, match: MatchRecord, home: TeamProfile, away: TeamProfile) -> float:
        if match.xg_gap_proxy_lite is not None:
            return max(0.0, min(100.0, 50 + 30 * float(match.xg_gap_proxy_lite)))
        return max(0.0, min(100.0, 100 * ((home.btts_rate_proxy + away.btts_rate_proxy) / 2 - 0.35)))

    def _summary(self, score: float, penalties: list[str]) -> str:
        if score >= 75:
            base = 'Perfil BTTS forte com bilateralidade ofensiva e concessão útil.'
        elif score >= 60:
            base = 'Perfil BTTS utilizável com suporte suficiente do módulo.'
        else:
            base = 'Perfil BTTS fraco ou demasiado condicionado para a Opportunity Pool.'
        if penalties:
            return base + ' Penalizações principais: ' + ', '.join(penalties) + '.'
        return base
