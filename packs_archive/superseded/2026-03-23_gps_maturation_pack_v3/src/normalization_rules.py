from __future__ import annotations

TEXT_TO_LEVEL = {
    "muito baixa":1,"baixa":2,"média":3,"media":3,"alta":4,"muito alta":5,
    "muito baixo":1,"baixo":2,"moderado":3,"alto":4,"muito alto":5
}
EDGE_BUCKETS = ("weak","acceptable","strong","very_strong")

def to_number(value):
    if isinstance(value, (int, float)):
        return float(value)
    return float(str(value).strip().replace("%","").replace(",","."))

def score_rule(module_id: str, score_raw):
    score = to_number(score_raw)
    if module_id == "btts" and score <= 10:
        return max(0.0, min(100.0, score * 10.0))
    return max(0.0, min(100.0, score))

def level_rule(raw_value):
    if isinstance(raw_value, int):
        return max(1, min(5, raw_value))
    if isinstance(raw_value, float):
        if raw_value <= 5:
            return max(1, min(5, round(raw_value)))
        if raw_value < 25: return 1
        if raw_value < 45: return 2
        if raw_value < 65: return 3
        if raw_value < 85: return 4
        return 5
    text = str(raw_value).strip().lower()
    if text in TEXT_TO_LEVEL:
        return TEXT_TO_LEVEL[text]
    raise ValueError(f"Unsupported level value: {raw_value}")

def edge_rule(edge_raw):
    if edge_raw in (None, ""):
        return "weak"
    low = str(edge_raw).strip().lower()
    if low in EDGE_BUCKETS:
        return low
    value = to_number(edge_raw)
    if value < 3: return "weak"
    if value < 6: return "acceptable"
    if value < 10: return "strong"
    return "very_strong"
