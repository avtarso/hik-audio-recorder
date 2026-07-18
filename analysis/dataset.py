from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

import numpy as np


@dataclass(slots=True)
class CsvDataset:
    """
    Dataset loaded from CSV produced by CsvRecorder.
    """

    timestamps: np.ndarray
    rms: np.ndarray
    peak: np.ndarray
    mean: np.ndarray
    std: np.ndarray
    zero_crossings: np.ndarray

    sample_rate: int
    frame_size: int

    @classmethod
    def load(cls, filename: str | Path) -> "CsvDataset":

        filename = Path(filename)

        timestamps = []
        rms = []
        peak = []
        mean = []
        std = []
        zero = []

        sample_rate = None
        frame_size = None

        with filename.open(newline="") as f:

            reader = csv.DictReader(f)

            for row in reader:

                timestamps.append(float(row["timestamp"]))

                rms.append(float(row["rms"]))
                peak.append(float(row["peak"]))
                mean.append(float(row["mean"]))
                std.append(float(row["std"]))
                zero.append(int(row["zero_crossings"]))

                if sample_rate is None:
                    sample_rate = int(row["sample_rate"])

                if frame_size is None:
                    frame_size = int(row["frame_size"])

        return cls(
            timestamps=np.asarray(timestamps, dtype=np.float64),
            rms=np.asarray(rms, dtype=np.float32),
            peak=np.asarray(peak, dtype=np.float32),
            mean=np.asarray(mean, dtype=np.float32),
            std=np.asarray(std, dtype=np.float32),
            zero_crossings=np.asarray(zero, dtype=np.int32),
            sample_rate=sample_rate,
            frame_size=frame_size,
        )

    @property
    def frames(self) -> int:
        return len(self.timestamps)

    @property
    def duration(self) -> float:

        if self.frames < 2:
            return 0.0

        return float(self.timestamps[-1] - self.timestamps[0])

    @property
    def fps(self) -> float:

        if self.duration <= 0:
            return 0.0

        return self.frames / self.duration