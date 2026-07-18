from __future__ import annotations

from typing import Iterable

from har.core.audio_frame import AudioFrame
from har.core.processor import Processor


class Pipeline:

    def __init__(self, processors: Iterable[Processor]):

        self._processors = list(processors)

    def process(self, frame: AudioFrame) -> None:

        for processor in self._processors:

            processor.process(frame)