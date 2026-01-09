# ABX-GT Overlay v0.1 (Canon-Shadow)

ABX-GT is a deterministic game-theory instrumentation overlay for shadow observation. It runs deterministic simulation vectors (GTVector.v0) and emits shadow-only metrics for diagnostic and oracle annotation flows.

## Lane
- **SHADOW only**. ABX-GT output must never alter forecasts, routing, or weights.

## ABXGTReport.v0 (minimal)
ABX-GT emits a standardized ABX-Runes envelope with a `report` payload:

```json
{
  "rune": "abx_gt",
  "lane": "shadow",
  "input_schema": "GTVector.v0",
  "output_schema": "ABXGTReport.v0",
  "vector_id": "gtv-001",
  "seed": 401,
  "not_computable": false,
  "missing_fields": [],
  "metrics": {
    "coordination_pressure": 0.62,
    "defection_risk": 0.38,
    "equilibrium_stability": 0.71,
    "hidden_player_likelihood": 0.11,
    "payoff_opacity_index": 0.44,
    "signal_cost_ratio": 0.29,
    "credibility_decay_rate": 0.53
  },
  "rent_payment": {
    "baseline_unknown_strategy_rate": 0.3,
    "post_unknown_strategy_rate": 0.24
  }
}
```

## Running vectors

```bash
python -m aal_core.overlays.abx_gt.runtime.abx_gt_runner \
  --vectors aal_core/overlays/abx_gt/vectors/abx_gt_vectors.v0.1.jsonl
```

## ABX-Runes coupling
ABX-GT output is emitted as an ABX-Runes envelope (`rune: abx_gt`) and is eligible only for **shadow** attachment under `oracle.shadow.abx_gt`.
