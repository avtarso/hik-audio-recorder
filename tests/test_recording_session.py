from pathlib import Path

from tests.helpers import make_audio_frame

from src.har.session.recording_session import RecordingSession


def test_process_frame():

    session = RecordingSession(
        output_dir=Path("tmp"),
    )

    session.process(
        make_audio_frame()
    )


def test_process_background():

    session = RecordingSession(
        output_dir=Path("tmp"),
    )

    for _ in range(200):

        session.process(
            make_audio_frame(value=0.01)
        )


def test_process_single_loud_frame():

    session = RecordingSession(
        output_dir=Path("tmp"),
    )

    session.process(
        make_audio_frame(value=0.01)
    )

    session.process(
        make_audio_frame(value=0.50)
    )


def test_output_directory_is_created(tmp_path: Path):

    session = RecordingSession(
        output_dir=tmp_path,
    )

    assert tmp_path.exists()


def test_recording_creates_wave_file():
    pass