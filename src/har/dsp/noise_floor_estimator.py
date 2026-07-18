from src.har.dsp.sliding_window import SlidingWindow


class NoiseFloorEstimator:
    """
    Estimates the current background noise level using
    a sliding window of RMS values.
    """

    def __init__(self, window_size: int = 125):

        self._window = SlidingWindow(window_size)

    def update(self, rms: float) -> None:
        """
        Add one RMS measurement.
        """

        self._window.append(rms)

    @property
    def noise_floor(self) -> float:
        """
        Current estimated background noise level.
        """

        return self._window.median

    @property
    def samples(self) -> int:
        return self._window.size