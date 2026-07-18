from __future__ import annotations

import numpy as np

from src.har.core.audio_frame import AudioFrame
from src.har.core.feature_frame import FeatureFrame


class FeatureExtractor:

    @staticmethod
    def extract(frame: AudioFrame) -> FeatureFrame:

        samples = frame.samples

        rms = float(np.sqrt(np.mean(samples ** 2)))

        peak = float(np.max(np.abs(samples)))

        mean = float(np.mean(samples))

        std = float(np.std(samples))

        zero_crossings = int(
            np.count_nonzero(
                np.diff(np.signbit(samples))
            )
        )

        return FeatureFrame(
            timestamp=frame.timestamp,
            sample_rate=frame.sample_rate,
            frame_size=len(samples),
            rms=rms,
            peak=peak,
            mean=mean,
            std=std,
            zero_crossings=zero_crossings,
        )