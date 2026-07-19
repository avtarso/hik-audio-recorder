from unittest.mock import MagicMock

import numpy as np

from src.har.core.audio_frame import AudioFrame


def test_from_av_frame():

    av_frame = MagicMock()

    av_frame.to_ndarray.return_value = np.array(
        [[32767, 0, -32768]],
        dtype=np.int16,
    )

    av_frame.sample_rate = 16000
    av_frame.time = 1.25

    frame = AudioFrame.from_av_frame(av_frame)

    np.testing.assert_allclose(
        frame.samples,
        np.array(
            [1.0, 0.0, -1.0],
            dtype=np.float32,
        ),
        atol=1e-4,
)

    assert frame.sample_rate == 16000
    assert frame.timestamp == 1.25