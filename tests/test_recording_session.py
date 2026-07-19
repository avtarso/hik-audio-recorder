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