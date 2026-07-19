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


from unittest.mock import MagicMock

from src.har.dsp.event import Event
from src.har.pipeline.pipeline_result import PipelineResult
from src.har.session.recording_session import RecordingSession

from tests.helpers import make_audio_frame


def test_start_event_starts_recorder(tmp_path):

    pipeline = MagicMock()
    recorder = MagicMock()

    pipeline.process.return_value = PipelineResult(
        feature=MagicMock(),
        noise_floor=0.0,
        event=Event.START,
    )

    session = RecordingSession(
        output_dir=tmp_path,
        pipeline=pipeline,
        recorder=recorder,
    )

    frame = make_audio_frame()

    session.process(frame)

    recorder.start.assert_called_once_with(frame)


from unittest.mock import MagicMock

from src.har.dsp.event import Event
from src.har.pipeline.pipeline_result import PipelineResult
from src.har.session.recording_session import RecordingSession

from tests.helpers import make_audio_frame


def test_none_event_pushes_frame_while_recording(tmp_path):

    pipeline = MagicMock()
    recorder = MagicMock()

    recorder.is_recording = True

    pipeline.process.return_value = PipelineResult(
        feature=MagicMock(),
        noise_floor=0.0,
        event=Event.NONE,
    )

    session = RecordingSession(
        output_dir=tmp_path,
        pipeline=pipeline,
        recorder=recorder,
    )

    frame = make_audio_frame()

    session.process(frame)

    recorder.push.assert_called_once_with(frame)


from unittest.mock import MagicMock

from src.har.dsp.event import Event
from src.har.pipeline.pipeline_result import PipelineResult
from src.har.session.recording_session import RecordingSession

from tests.helpers import make_audio_frame


def test_stop_event_saves_recording(tmp_path):

    pipeline = MagicMock()
    recorder = MagicMock()
    writer = MagicMock()

    recorder.is_recording = True

    frames = [make_audio_frame()]
    recorder.stop.return_value = frames

    pipeline.process.return_value = PipelineResult(
        feature=MagicMock(),
        noise_floor=0.0,
        event=Event.STOP,
    )

    session = RecordingSession(
        output_dir=tmp_path,
        pipeline=pipeline,
        recorder=recorder,
        writer=writer,
    )

    result = session.process(
        make_audio_frame()
    )

    recorder.stop.assert_called_once()

    writer.write.assert_called_once()

    written_frames, written_path = writer.write.call_args.args

    assert written_frames == frames
    assert written_path == result.file
    assert result.file is not None