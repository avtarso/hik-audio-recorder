from __future__ import annotations

from collections import Counter
import time

import numpy as np

from src.har.core.audio_frame import AudioFrame
from src.har.core.processor import Processor


class FrameInspector(Processor):
    def __init__(self) -> None:
        self._frames = 0
        self._started = time.perf_counter()

        self._sample_rates = Counter()
        self._sizes = Counter()

        self._peak = 0.0
        self._rms_sum = 0.0

    def process(self, frame: AudioFrame) -> None:

        self._frames += 1

        self._sample_rates[frame.sample_rate] += 1
        self._sizes[len(frame.samples)] += 1

        rms = float(np.sqrt(np.mean(frame.samples ** 2)))

        self._rms_sum += rms
        self._peak = max(self._peak, float(np.max(np.abs(frame.samples))))

        elapsed = time.perf_counter() - self._started

        if elapsed >= 5:

            print("\n========== Frame Inspector ==========")
            print(f"Frames: {self._frames}")
            print(f"FPS: {self._frames / elapsed:.2f}")

            print(f"Sample rates: {dict(self._sample_rates)}")
            print(f"Frame sizes : {dict(self._sizes)}")

            print(f"Average RMS : {self._rms_sum / self._frames:.2f}")
            print(f"Peak sample : {self._peak:.2f}")
            print("=====================================\n")

            self._started = time.perf_counter()
            self._frames = 0
            self._sample_rates.clear()
            self._sizes.clear()
            self._rms_sum = 0.0
            self._peak = 0.0