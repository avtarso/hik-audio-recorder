from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class NoiseState:
    median: float
    mean: float
    std: float
    p95: float
    samples: int