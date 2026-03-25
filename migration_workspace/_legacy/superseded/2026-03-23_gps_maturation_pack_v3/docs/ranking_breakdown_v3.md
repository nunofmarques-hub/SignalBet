# Ranking Breakdown v3

## fórmula base
global_score_pre_adjustment =
0.50 * score_norm_base
+ 0.20 * confidence_points
+ 0.15 * risk_safety_points
+ 0.15 * edge_points

## componentes
- score_norm_base
- confidence_points
- risk_safety_points
- edge_points

## ajustamentos
- quality_adjustment
- conflict_adjustment
- correlation_adjustment
- rationale_adjustment
- completeness_adjustment

## score final
global_score_final =
global_score_pre_adjustment
+ quality_adjustment
+ conflict_adjustment
+ correlation_adjustment
+ rationale_adjustment
+ completeness_adjustment

## priority tier
- 90–100 = Best
- 82–89 = Top
- 72–81 = Actionable
- 60–71 = Watchlist
- <60 = Reject
