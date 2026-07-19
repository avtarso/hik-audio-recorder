from unittest.mock import MagicMock

import pytest

from src.har.sources.rtsp_audio_source import RtspAudioSource


def test_audio_stream_found():

    source = RtspAudioSource(
        "rtsp://camera"
    )

    audio_stream = MagicMock()
    audio_stream.type = "audio"

    video_stream = MagicMock()
    video_stream.type = "video"

    container = MagicMock()
    container.streams = [
        video_stream,
        audio_stream,
    ]

    stream = source._audio_stream(container)

    assert stream is audio_stream


def test_audio_stream_not_found():

    source = RtspAudioSource(
        "rtsp://camera"
    )

    video_stream = MagicMock()
    video_stream.type = "video"

    container = MagicMock()
    container.streams = [
        video_stream,
    ]

    with pytest.raises(RuntimeError):
        source._audio_stream(container)