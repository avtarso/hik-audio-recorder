from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class FeatureFrame:

    timestamp: float

    sample_rate: int

    frame_size: int

    rms: float

    peak: float

    mean: float

    std: float

    zero_crossings: int