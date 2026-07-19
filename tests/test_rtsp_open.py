from unittest.mock import patch

from src.har.sources.rtsp_audio_source import RtspAudioSource


@patch("src.har.sources.rtsp_audio_source.av.open")
def test_open_stream(mock_open):

    source = RtspAudioSource(
        "rtsp://camera"
    )

    source._open()

    mock_open.assert_called_once()

    mock_open.assert_called_once_with(
    "rtsp://camera",
    mode="r",
)