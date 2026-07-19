import pytest

from src.har.sources.rtsp_audio_source import RtspAudioSource


def test_create_source():

    source = RtspAudioSource(
        "rtsp://camera"
    )

    assert source.url == "rtsp://camera"


from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from src.har.sources.rtsp_audio_source import RtspAudioSource


@patch.object(RtspAudioSource, "_open")
def test_iterator_closes_container_when_not_implemented(mock_open):

    container = MagicMock()
    mock_open.return_value = container

    source = RtspAudioSource(
        "rtsp://camera"
    )

    with pytest.raises(NotImplementedError):
        next(iter(source))

    mock_open.assert_called_once()

    container.close.assert_called_once()