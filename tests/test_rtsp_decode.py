from unittest.mock import MagicMock

from src.har.sources.rtsp_audio_source import RtspAudioSource


def test_decoded_frames():

    source = RtspAudioSource(
        "rtsp://camera"
    )

    frame1 = MagicMock()
    frame2 = MagicMock()

    packet = MagicMock()
    packet.decode.return_value = [
        frame1,
        frame2,
    ]

    container = MagicMock()
    container.demux.return_value = [
        packet,
    ]

    frames = list(
        source._decoded_frames(
            container,
            MagicMock(),
        )
    )

    assert frames == [
        frame1,
        frame2,
    ]

    container.demux.assert_called_once()


from unittest.mock import MagicMock

from src.har.sources.rtsp_audio_source import RtspAudioSource


def test_audio_stream_returns_audio_stream():

    source = RtspAudioSource("rtsp://camera")

    video_stream = MagicMock()
    video_stream.type = "video"

    audio_stream = MagicMock()
    audio_stream.type = "audio"

    container = MagicMock()
    container.streams = [
        video_stream,
        audio_stream,
    ]

    result = source._audio_stream(container)

    assert result is audio_stream


import pytest


def test_audio_stream_raises_if_audio_missing():

    source = RtspAudioSource("rtsp://camera")

    video_stream = MagicMock()
    video_stream.type = "video"

    container = MagicMock()
    container.streams = [
        video_stream,
    ]

    with pytest.raises(
        RuntimeError,
        match="RTSP stream contains no audio stream",
    ):
        source._audio_stream(container)