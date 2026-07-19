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


# @patch.object(RtspAudioSource, "_open")
# def test_iterator_closes_container_when_not_implemented(mock_open):

#     container = MagicMock()
#     mock_open.return_value = container

#     source = RtspAudioSource(
#         "rtsp://camera"
#     )

#     with pytest.raises(NotImplementedError):
#         next(iter(source))

#     mock_open.assert_called_once()

#     container.close.assert_called_once()


from unittest.mock import MagicMock, patch

from src.har.sources.rtsp_audio_source import RtspAudioSource
from src.har.core.audio_frame import AudioFrame


@patch.object(AudioFrame, "from_av_frame")
@patch.object(RtspAudioSource, "_decoded_frames")
@patch.object(RtspAudioSource, "_audio_stream")
@patch.object(RtspAudioSource, "_open")
def test_iterator_yields_audio_frames(
    mock_open,
    mock_audio_stream,
    mock_decoded_frames,
    mock_from_av_frame,
):

    container = MagicMock()
    stream = MagicMock()

    decoded1 = MagicMock()
    decoded2 = MagicMock()

    audio1 = MagicMock()
    audio2 = MagicMock()

    mock_open.return_value = container
    mock_audio_stream.return_value = stream
    mock_decoded_frames.return_value = [
        decoded1,
        decoded2,
    ]
    mock_from_av_frame.side_effect = [
        audio1,
        audio2,
    ]

    source = RtspAudioSource("rtsp://camera")

    result = list(source)

    assert result == [
        audio1,
        audio2,
    ]

    mock_audio_stream.assert_called_once_with(container)
    mock_decoded_frames.assert_called_once_with(
        container,
        stream,
    )

    assert mock_from_av_frame.call_count == 2
    container.close.assert_called_once()



from unittest.mock import MagicMock, patch

import pytest

from src.har.sources.rtsp_audio_source import RtspAudioSource


@patch.object(RtspAudioSource, "_decoded_frames")
@patch.object(RtspAudioSource, "_audio_stream")
@patch.object(RtspAudioSource, "_open")
def test_iterator_closes_container_on_error(
    mock_open,
    mock_audio_stream,
    mock_decoded_frames,
):

    container = MagicMock()

    mock_open.return_value = container
    mock_audio_stream.return_value = MagicMock()
    mock_decoded_frames.side_effect = RuntimeError("boom")

    source = RtspAudioSource("rtsp://camera")

    with pytest.raises(RuntimeError, match="boom"):
        list(source)

    container.close.assert_called_once()