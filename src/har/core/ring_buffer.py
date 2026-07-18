from __future__ import annotations

from collections import deque
from typing import Iterable

from src.har.core.audio_frame import AudioFrame


class RingBuffer:

    def __init__(self, max_frames: int):

        if max_frames <= 0:
            raise ValueError("max_frames must be greater than zero")

        self._frames: deque[AudioFrame] = deque(maxlen=max_frames)

    @property
    def capacity(self) -> int:
        return self._frames.maxlen

    @property
    def size(self) -> int:
        return len(self._frames)

    @property
    def is_full(self) -> bool:
        return len(self._frames) == self._frames.maxlen

    def push(self, frame: AudioFrame) -> None:
        self._frames.append(frame)

    def clear(self) -> None:
        self._frames.clear()

    def get_all(self) -> list[AudioFrame]:
        return list(self._frames)

    def get_last(self, count: int) -> list[AudioFrame]:

        if count <= 0:
            return []

        return list(self._frames)[-count:]

    def extend(self, frames: Iterable[AudioFrame]) -> None:

        for frame in frames:
            self.push(frame)