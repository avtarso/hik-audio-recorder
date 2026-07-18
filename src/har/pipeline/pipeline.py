from src.har.core.audio_frame import AudioFrame
from src.har.core.processor import Processor


class Pipeline:
    def __init__(self) -> None:
        self._processors: list[Processor] = []

    def add(self, processor: Processor) -> None:
        self._processors.append(processor)

    def process(self, frame: AudioFrame) -> None:
        for processor in self._processors:
            processor.process(frame)