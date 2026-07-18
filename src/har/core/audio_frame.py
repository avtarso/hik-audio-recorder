from dataclasses import dataclass

import numpy as np


@dataclass(slots=True, frozen=True)
class AudioFrame:
    """
    Internal representation of one decoded audio frame.

    This class isolates the rest of the application
    from PyAV internals.
    """

    samples: np.ndarray
    sample_rate: int
    timestamp: float