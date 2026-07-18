from __future__ import annotations

from typing import Iterator

import av
import numpy as np

from src.har.core.audio_frame import AudioFrame


class RTSPReader:
    """
    Reads audio frames from an RTSP source and yields AudioFrame objects.
    """

    def __init__(self, url: str):
        self.url = url

    def __iter__(self) -> Iterator[AudioFrame]:

        container = av.open(
            self.url,
            options={
                "rtsp_transport": "tcp",
            },
        )

        audio_stream = next(
            s
            for s in container.streams
            if s.type == "audio"
        )

        for packet in container.demux(audio_stream):

            for frame in packet.decode():

                samples = frame.to_ndarray()

                # stereo -> mono
                if samples.ndim == 2:
                    samples = samples.mean(axis=0)

                samples = samples.astype(np.float32)

                # Нормализация для int16/μ-law после декодирования
                samples /= 32768.0

                yield AudioFrame(
                    samples=samples,
                    sample_rate=frame.sample_rate,
                    timestamp=float(frame.time or 0.0),
                )