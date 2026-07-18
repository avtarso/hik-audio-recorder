from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .dataset import CsvDataset


@dataclass(slots=True)
class AnalysisResult:
    frames: int
    duration: float
    fps: float

    sample_rate: int
    frame_size: int

    rms_mean: float
    rms_median: float
    rms_std: float
    rms_min: float
    rms_max: float
    rms_p95: float
    rms_p99: float

    peak_mean: float
    peak_max: float

    zero_crossings_mean: float
    zero_crossings_std: float


class Analyzer:

    def analyze(self, dataset: CsvDataset) -> AnalysisResult:

        rms = dataset.rms
        peak = dataset.peak
        zc = dataset.zero_crossings

        return AnalysisResult(
            frames=dataset.frames,
            duration=dataset.duration,
            fps=dataset.fps,

            sample_rate=dataset.sample_rate,
            frame_size=dataset.frame_size,

            rms_mean=float(np.mean(rms)),
            rms_median=float(np.median(rms)),
            rms_std=float(np.std(rms)),
            rms_min=float(np.min(rms)),
            rms_max=float(np.max(rms)),
            rms_p95=float(np.percentile(rms, 95)),
            rms_p99=float(np.percentile(rms, 99)),

            peak_mean=float(np.mean(peak)),
            peak_max=float(np.max(peak)),

            zero_crossings_mean=float(np.mean(zc)),
            zero_crossings_std=float(np.std(zc)),
        )