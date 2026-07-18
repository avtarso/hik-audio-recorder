from abc import ABC, abstractmethod

from src.har.core.audio_frame import AudioFrame

class Processor(ABC):

    @abstractmethod
    def process(self, frame: AudioFrame) -> None:
        pass