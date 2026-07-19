from pathlib import Path
import wave

import numpy as np

from src.har.core.audio_frame import AudioFrame
from src.har.io.wave_writer import WaveWriter

from tests.helpers import make_audio_frame


def test_wave_writer():

    frames = [
        make_audio_frame(
            value=0.2, 
            timestamp=0.0),
        make_audio_frame(
            value=-0.2, 
            timestamp=0.04),
        make_audio_frame(
            value=0.2, 
            timestamp=0.08),
    ]

    output = Path("test.wav")

    WaveWriter().write(
        frames,
        output,
    )

    assert output.exists()

    with wave.open(str(output), "rb") as wav:

        assert wav.getframerate() == 8000
        assert wav.getnchannels() == 1
        assert wav.getsampwidth() == 2

    output.unlink()