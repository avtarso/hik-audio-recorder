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