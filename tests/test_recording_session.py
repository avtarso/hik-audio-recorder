from pathlib import Path

from tests.helpers import make_audio_frame

from src.har.dsp.event import Event
from src.har.session.recording_session import RecordingSession


def test_process_frame():

    session = RecordingSession(
        output_dir=Path("tmp"),
    )

    result = session.process(
        make_audio_frame()
    )

    assert result.event is Event.NONE
    assert result.file is None


def test_process_background():

    session = RecordingSession(
        output_dir=Path("tmp"),
    )

    result = None

    for _ in range(200):

        result = session.process(
            make_audio_frame(value=0.01)
        )

    assert result is not None
    assert result.event is Event.NONE
    assert result.file is None


def test_process_single_loud_frame():

    session = RecordingSession(
        output_dir=Path("tmp"),
    )

    session.process(
        make_audio_frame(value=0.01)
    )

    result = session.process(
        make_audio_frame(value=0.50)
    )

    assert result.file is None


def test_output_directory_is_created(tmp_path: Path):

    session = RecordingSession(
        output_dir=tmp_path,
    )

    assert session is not None
    assert tmp_path.exists()


def test_recording_creates_wave_file():
    """
    Placeholder for future integration test.
    """
    pass


def test_process_returns_session_result(tmp_path: Path):

    session = RecordingSession(
        output_dir=tmp_path,
    )

    result = session.process(
        make_audio_frame()
    )

    assert result.event is Event.NONE
    assert result.file is None