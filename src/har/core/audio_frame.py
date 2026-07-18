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