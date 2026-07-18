from __future__ import annotations

import time

import numpy as np

from src.har.core.audio_frame import AudioFrame
from src.har.core.processor import Processor


class AcousticProfiler(Processor):
    REPORT_INTERVAL = 5.0

    def __init__(self):

        self.started = time.perf_counter()

        self.frames = 0

        self.rms_values = []

        self.peaks = []

        self.offsets = []

    def process(self, frame: AudioFrame):

        samples = frame.samples

        rms = float(np.sqrt(np.mean(samples ** 2)))

        peak = float(np.max(np.abs(samples)))

        offset = float(np.mean(samples))

        self.frames += 1

        self.rms_values.append(rms)

        self.peaks.append(peak)

        self.offsets.append(offset)

        elapsed = time.perf_counter() - self.started

        if elapsed >= self.REPORT_INTERVAL:

            self.report(elapsed)

            self.reset()

    def report(self, elapsed):

        rms = np.array(self.rms_values)

        peaks = np.array(self.peaks)

        offsets = np.array(self.offsets)

        print()

        print("=" * 55)

        print(f"Frames       : {self.frames}")

        print(f"FPS          : {self.frames / elapsed:.2f}")

        print()

        print(f"RMS avg      : {rms.mean():.6f}")

        print(f"RMS min      : {rms.min():.6f}")

        print(f"RMS max      : {rms.max():.6f}")

        print()

        print(f"Peak max     : {peaks.max():.6f}")

        print()

        print(f"DC Offset    : {offsets.mean():.6f}")

        print("=" * 55)

        print()

    def reset(self):

        self.started = time.perf_counter()

        self.frames = 0

        self.rms_values.clear()

        self.peaks.clear()

        self.offsets.clear()