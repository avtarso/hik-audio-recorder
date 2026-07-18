from src.har.dsp.sliding_window import SlidingWindow


def test_empty_window():
    window = SlidingWindow(10)

    assert window.size == 0
    assert not window.is_full
    assert window.capacity == 10

def test_append():

    window = SlidingWindow(3)

    window.append(1)

    assert window.size == 1

    window.append(2)

    assert window.size == 2

    window.append(3)

    assert window.size == 3

    assert window.is_full

def test_overflow():

    window = SlidingWindow(3)

    window.append(1)
    window.append(2)
    window.append(3)
    window.append(4)

    assert window.size == 3

import pytest

def test_empty_mean():

    window = SlidingWindow(10)

    with pytest.raises(ValueError):
        _ = window.mean

def test_empty_median():

    window = SlidingWindow(10)

    with pytest.raises(ValueError):
        _ = window.median