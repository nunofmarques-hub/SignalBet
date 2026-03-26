# UI Refresh Control Flow

1. Verificar snapshot persistido.
2. Se estiver fresh, reutilizar.
3. Se estiver stale, tentar refresh protegido.
4. Se o refresh falhar, reutilizar stale snapshot ou cair para fallback, conforme disponibilidade.
