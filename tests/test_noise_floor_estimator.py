import pytest

from src.har.dsp.noise_floor_estimator import NoiseFloorEstimator


def test_empty_estimator():

    estimator = NoiseFloorEstimator()

    with pytest.raises(ValueError):
        _ = estimator.noise_floor


def test_single_value():

    estimator = NoiseFloorEstimator()

    estimator.update(0.012)

    assert estimator.noise_floor == pytest.approx(0.012)


def test_median():

    estimator = NoiseFloorEstimator()

    estimator.update(0.010)
    estimator.update(0.011)
    estimator.update(0.012)

    assert estimator.noise_floor == pytest.approx(0.011)


def test_outlier():

    estimator = NoiseFloorEstimator()

    estimator.update(0.010)
    estimator.update(0.011)
    estimator.update(0.012)
    estimator.update(0.013)
    estimator.update(0.500)

    assert estimator.noise_floor == pytest.approx(0.012)


def test_window_overflow():

    estimator = NoiseFloorEstimator(window_size=3)

    estimator.update(1.0)
    estimator.update(2.0)
    estimator.update(3.0)
    estimator.update(100.0)

    assert estimator.samples == 3

    # окно содержит:
    # 2.0
    # 3.0
    # 100.0

    assert estimator.noise_floor == pytest.approx(3.0)