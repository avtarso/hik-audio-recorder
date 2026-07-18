from pathlib import Path
import wave

import numpy as np

from src.har.core.audio_frame import AudioFrame
from src.har.io.wave_writer import WaveWriter

from tests.helpers import make_frame


def test_wave_writer():

    frames = [
        make_frame(0.2, 0.0),
        make_frame(-0.2, 0.04),
        make_frame(0.2, 0.08),
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