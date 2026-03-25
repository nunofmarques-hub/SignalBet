from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class RawAssessment:
    market: str
    selection: str
    line: Optional[float]
    odds: Optional[float]
    score_raw: float
    confidence_raw: int
    risk_raw: int
    edge_raw: str
    eligibility: bool
    rationale_summary: str
    main_drivers: List[str] = field(default_factory=list)
    penalties: List[str] = field(default_factory=list)
    data_quality_flag: str = "clean"
    module_rank_internal: int = 1
    expiry_context: str = "refresh_if_market_moves"
    module_specific_payload: Dict[str, Any] = field(default_factory=dict)
