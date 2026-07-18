from __future__ import annotations

import csv
from pathlib import Path

from src.har.core.audio_frame import AudioFrame
from src.har.core.processor import Processor
from src.har.features.extractor import FeatureExtractor


class CsvRecorder(Processor):

    def __init__(self, filename: str):

        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)

        self.file = path.open(
            "w",
            newline="",
            encoding="utf-8",
        )

        self.writer = csv.writer(self.file)

        self.writer.writerow(
            [
                "timestamp",
                "sample_rate",
                "frame_size",
                "rms",
                "peak",
                "mean",
                "std",
                "zero_crossings",
            ]
        )

        self.rows = 0

    def process(self, frame: AudioFrame):

        feature = FeatureExtractor.extract(frame)

        self.writer.writerow(
            [
                feature.timestamp,
                feature.sample_rate,
                feature.frame_size,
                feature.rms,
                feature.peak,
                feature.mean,
                feature.std,
                feature.zero_crossings,
            ]
        )

        self.rows += 1

        if self.rows % 100 == 0:
            self.file.flush()

    def close(self):
        self.file.flush()
        self.file.close()