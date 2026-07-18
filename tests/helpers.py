import numpy as np

from src.har.core.audio_frame import AudioFrame


def make_frame(
    value: float = 0.0,
    timestamp: float = 0.0,
    sample_rate: int = 8000,
    size: int = 320,
) -> AudioFrame:
    return AudioFrame(
        samples=np.full(size, value, dtype=np.float32),
        sample_rate=sample_rate,
        timestamp=timestamp,
    )