# Target Tree BTTS

Árvore técnica-alvo recomendada para o módulo quando passar de `migration_workspace/btts/...` para `modules/btts/`.

```text
modules/
  btts/
    README.md
    __init__.py
    config/
      contract_v1_1.py
      weights.py
      thresholds.py
    engine/
      engine.py
      market_result.py
      flags.py
    indicators/
      bos.py
      bvs.py
      sbi.py
      ami_bilateral.py
      fgt_btts.py
      tsi_bilateral.py
      xg_gap_aggregated.py
    penalties/
      dominance.py
      under.py
      underdog_dead.py
      dci_proxy.py
    exporters/
      market_pick_v1_1.py
    data/
      parsers/
      builders/
      adapters/
    tests/
      autonomous/
      validation/
      semi_real/
```

## Núcleo mínimo funcional
Para uma primeira integração técnica, o mínimo recomendado é:
- `engine/engine.py`
- `engine/market_result.py`
- `indicators/bos.py`
- `indicators/bvs.py`
- `indicators/sbi.py`
- `exporters/market_pick_v1_1.py`
- `config/contract_v1_1.py`

## Fase seguinte
Depois entram os afinadores e validações:
- `ami_bilateral.py`
- `fgt_btts.py`
- `tsi_bilateral.py`
- `xg_gap_aggregated.py`
- `penalties/*`
- testes semi-reais e validation suite
