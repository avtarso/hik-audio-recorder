from __future__ import annotations

from src.har.core.audio_frame import AudioFrame
from src.har.core.ring_buffer import RingBuffer


class Recorder:
    """
    Collects AudioFrame objects belonging to one sound event.

    Recorder is responsible only for buffering frames.

    It does NOT know anything about:

    - RTSP
    - WAV
    - EventDetector
    - files
    """

    def __init__(self, pre_buffer_frames: int = 125):

        self._buffer = RingBuffer(pre_buffer_frames)

        self._recording = False

        self._frames: list[AudioFrame] = []

    @property
    def is_recording(self) -> bool:
        return self._recording

    def push(self, frame: AudioFrame) -> None:

        self._buffer.push(frame)

        if self._recording:
            self._frames.append(frame)

    def start(self) -> None:

        if self._recording:
            return

        self._recording = True

        self._frames = self._buffer.get_all()

    def stop(self) -> list[AudioFrame]:

        if not self._recording:
            return []

        frames = self._frames

        self._frames = []

        self._recording = False

        return frames

    def reset(self) -> None:

        self._frames.clear()

        self._recording = False

        self._buffer.clear()