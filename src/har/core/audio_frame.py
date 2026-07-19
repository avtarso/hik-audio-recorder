from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


@dataclass(slots=True, frozen=True)
class AudioFrame:
    """
    Internal representation of one decoded audio frame.

    This class isolates the rest of the application
    from PyAV internals.
    """

    samples: NDArray[np.float32]
    sample_rate: int
    timestamp: float

    @classmethod
    def from_av_frame(
        cls,
        frame,
    ) -> "AudioFrame":

        samples = frame.to_ndarray()

        if samples.ndim > 1:
            samples = samples.reshape(-1)

        if np.issubdtype(samples.dtype, np.integer):
            info = np.iinfo(samples.dtype)
            samples = samples.astype(np.float32)
            samples /= max(abs(info.min), info.max)
        else:
            samples = samples.astype(np.float32)

        return cls(
            samples=samples,
            sample_rate=frame.sample_rate,
            timestamp=frame.time,
        )