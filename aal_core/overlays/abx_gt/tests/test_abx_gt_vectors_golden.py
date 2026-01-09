import hashlib
import json
from pathlib import Path

from aal_core.overlays.abx_gt.runtime import abx_gt_runner


VECTORS_PATH = Path("aal_core/overlays/abx_gt/vectors/abx_gt_vectors.v0.1.jsonl")


def _hash_report(report):
    payload = json.dumps(report, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _load_vectors():
    return abx_gt_runner.load_vectors(VECTORS_PATH)


def test_determinism_12_run_invariance():
    vectors = _load_vectors()
    for vector in vectors:
        report = abx_gt_runner.evaluate_vector(vector)
        baseline_hash = _hash_report(report)
        for _ in range(12):
            rerun_hash = _hash_report(abx_gt_runner.evaluate_vector(vector))
            assert rerun_hash == baseline_hash


def test_bounds_no_nan():
    vectors = _load_vectors()
    reports = [abx_gt_runner.evaluate_vector(vector) for vector in vectors]
    for report in reports:
        for value in report["metrics"].values():
            assert 0.0 <= value <= 1.0
            assert value == value


def test_missing_input_not_computable():
    vector = {
        "id": "gtv-missing",
        "seed": 13,
        "players": ["alpha", "beta"],
    }
    report = abx_gt_runner.evaluate_vector(vector)
    assert report["not_computable"] is True
    assert "signals" in report["missing_fields"]


def test_rent_payment_gate():
    vectors = _load_vectors()
    for vector in vectors:
        report = abx_gt_runner.evaluate_vector(vector)
        baseline = report["rent_payment"]["baseline_unknown_strategy_rate"]
        post = report["rent_payment"]["post_unknown_strategy_rate"]
        if vector["game"]["rent_payment"]:
            assert post <= baseline
        else:
            assert post == baseline
