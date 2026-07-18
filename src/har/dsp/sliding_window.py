from __future__ import annotations

from collections import deque

import numpy as np


class SlidingWindow:

    def __init__(self, max_size: int):

        if max_size <= 0:
            raise ValueError("max_size must be positive")

        self._values: deque[float] = deque(maxlen=max_size)

    def _require_not_empty(self) -> None:
        if self.size == 0:
            raise ValueError("SlidingWindow is empty")

    def append(self, value: float) -> None:
        self._values.append(float(value))

    def clear(self) -> None:
        self._values.clear()

    @property
    def size(self) -> int:
        return len(self._values)

    @property
    def capacity(self) -> int:
        return self._values.maxlen

    @property
    def is_full(self) -> bool:
        return self.size == self.capacity

    @property
    def values(self) -> np.ndarray:
        return np.asarray(self._values, dtype=np.float32)

    @property
    def mean(self) -> float:
        self._require_not_empty()
        return float(np.mean(self.values))

    @property
    def median(self) -> float:
        self._require_not_empty()
        return float(np.median(self.values))

    @property
    def std(self) -> float:
        self._require_not_empty()
        return float(np.std(self.values))

    @property
    def min(self) -> float:
        self._require_not_empty()
        return float(np.min(self.values))

    @property
    def max(self) -> float:
        self._require_not_empty()
        return float(np.max(self.values))

    @property
    def p95(self) -> float:
        self._require_not_empty()
        return float(np.percentile(self.values, 95))