# UI Reuse Decision Policy

A UI prefere reutilizar snapshot protegido apenas quando o estado de freshness é `fresh`.
Quando o snapshot está `stale`, a bridge prefere refresh protegido. Se o refresh falhar, pode reutilizar stale snapshot com metadata explícita.
