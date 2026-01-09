"""ABX-GT deterministic runner (shadow-only)."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List


METRIC_KEYS = [
    "coordination_pressure",
    "defection_risk",
    "equilibrium_stability",
    "hidden_player_likelihood",
    "payoff_opacity_index",
    "signal_cost_ratio",
    "credibility_decay_rate",
]

REQUIRED_FIELDS = {
    "id",
    "seed",
    "players",
    "game",
    "actions",
    "payoffs",
    "signals",
    "shocks",
    "expected_ranges",
}


def _hash_to_unit(value: str, offset: int) -> float:
    digest = hashlib.sha256(f"{value}:{offset}".encode("utf-8")).digest()
    as_int = int.from_bytes(digest[:8], "big")
    return (as_int % 10_000) / 10_000.0


def _normalize_vector(vector: Dict[str, Any]) -> str:
    return json.dumps(vector, sort_keys=True, separators=(",", ":"))


def _missing_fields(vector: Dict[str, Any]) -> List[str]:
    return sorted(field for field in REQUIRED_FIELDS if field not in vector)


def load_vectors(path: Path) -> List[Dict[str, Any]]:
    vectors: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            vectors.append(json.loads(line))
    return vectors


def evaluate_vector(vector: Dict[str, Any]) -> Dict[str, Any]:
    missing = _missing_fields(vector)
    vector_id = vector.get("id", "unknown")
    seed = vector.get("seed", 0)
    if missing:
        return _build_envelope(
            vector_id=vector_id,
            seed=seed,
            metrics={},
            not_computable=True,
            missing_fields=missing,
            baseline_unknown_strategy_rate=0.0,
            post_unknown_strategy_rate=0.0,
        )

    normalized = _normalize_vector(vector)
    metrics = {}
    for idx, key in enumerate(METRIC_KEYS):
        metrics[key] = _hash_to_unit(normalized, idx)

    baseline_unknown_strategy_rate = _unknown_strategy_rate(vector)
    rent_payment_active = bool(vector.get("game", {}).get("rent_payment"))
    post_unknown_strategy_rate = _apply_rent_payment(
        baseline_unknown_strategy_rate,
        rent_payment_active,
    )

    return _build_envelope(
        vector_id=vector_id,
        seed=seed,
        metrics=metrics,
        not_computable=False,
        missing_fields=[],
        baseline_unknown_strategy_rate=baseline_unknown_strategy_rate,
        post_unknown_strategy_rate=post_unknown_strategy_rate,
    )


def _unknown_strategy_rate(vector: Dict[str, Any]) -> float:
    signals = vector.get("signals", [])
    if not signals:
        return 0.0
    unknown = sum(1 for signal in signals if signal.get("tag") == "unknown_strategy")
    return unknown / float(len(signals))


def _apply_rent_payment(baseline: float, rent_payment_active: bool) -> float:
    if not rent_payment_active:
        return baseline
    return max(0.0, baseline * 0.8)


def _build_envelope(
    *,
    vector_id: str,
    seed: int,
    metrics: Dict[str, float],
    not_computable: bool,
    missing_fields: List[str],
    baseline_unknown_strategy_rate: float,
    post_unknown_strategy_rate: float,
) -> Dict[str, Any]:
    return {
        "rune": "abx_gt",
        "lane": "shadow",
        "input_schema": "GTVector.v0",
        "output_schema": "ABXGTReport.v0",
        "vector_id": vector_id,
        "seed": seed,
        "not_computable": not_computable,
        "missing_fields": missing_fields,
        "metrics": metrics,
        "rent_payment": {
            "baseline_unknown_strategy_rate": baseline_unknown_strategy_rate,
            "post_unknown_strategy_rate": post_unknown_strategy_rate,
        },
    }


def run(vectors: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [evaluate_vector(vector) for vector in vectors]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run ABX-GT vectors (shadow-only).")
    parser.add_argument(
        "--vectors",
        type=Path,
        required=True,
        help="Path to ABX-GT vector JSONL file.",
    )
    args = parser.parse_args()

    vectors = load_vectors(args.vectors)
    reports = run(vectors)
    for report in reports:
        print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
