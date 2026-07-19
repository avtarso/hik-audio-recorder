from __future__ import annotations

from collections.abc import Iterator

from src.har.core.audio_frame import AudioFrame

import av
from av.container import InputContainer
from av.stream import Stream


class RtspAudioSource:
    """
    Audio source reading decoded audio frames
    from an RTSP stream.

    This class is responsible only for obtaining
    AudioFrame objects.

    It performs no DSP processing and contains
    no recording logic.
    """

    def __init__(
        self,
        url: str,
    ) -> None:

        self._url = url

    @property
    def url(self) -> str:

        return self._url

    def __iter__(self) -> Iterator[AudioFrame]:

        container = self._open()

        try:
            stream = self._audio_stream(container)

            for frame in self._decoded_frames(
                container,
                stream,
            ):
                yield AudioFrame.from_av_frame(frame)

        finally:
            container.close()
    

    def _open(self) -> av.container.InputContainer:
        """
        Open RTSP stream.
        """

        return av.open(
            self._url,
            mode="r",
            options={
                "rtsp_transport": "tcp",
            },
        )
    

    def _audio_stream(
        self,
        container: InputContainer,
    ) -> Stream:

        for stream in container.streams:

            if stream.type == "audio":
                return stream

        raise RuntimeError("RTSP stream contains no audio stream")
    

    def _decoded_frames(
        self,
        container,
        stream,
    ):
        """
        Yield decoded PyAV audio frames.
        """

        for packet in container.demux(stream):

            for frame in packet.decode():

                yield frame