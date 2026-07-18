from __future__ import annotations

import wave
from pathlib import Path

import numpy as np

from src.har.core.audio_frame import AudioFrame


class WaveWriter:
    """
    Writes AudioFrame sequences to a standard PCM WAV file.
    """

    def write(
        self,
        frames: list[AudioFrame],
        path: Path,
    ) -> None:

        if not frames:
            raise ValueError("frames is empty")

        sample_rates = {
            frame.sample_rate
            for frame in frames
        }

        if len(sample_rates) != 1:
            raise ValueError("frames have different sample rates")

        sample_rate = sample_rates.pop()

        samples = np.concatenate(
            [frame.samples for frame in frames]
        )

        samples = np.clip(samples, -1.0, 1.0)

        pcm = (samples * 32767).astype(np.int16)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with wave.open(str(path), "wb") as wav:

            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(sample_rate)

            wav.writeframes(
                pcm.tobytes()
            )