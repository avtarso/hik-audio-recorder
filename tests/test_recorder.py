import numpy as np

from src.har.core.audio_frame import AudioFrame
from src.har.recording.recorder import Recorder


def make_frame(timestamp: float) -> AudioFrame:

    return AudioFrame(
        samples=np.zeros(320, dtype=np.float32),
        sample_rate=8000,
        timestamp=timestamp,
    )


def test_stop_without_start():

    recorder = Recorder()

    assert recorder.stop() == []


def test_recording_collects_frames():

    recorder = Recorder(pre_buffer_frames=3)

    recorder.push(make_frame(1))
    recorder.push(make_frame(2))
    recorder.push(make_frame(3))

    recorder.start()

    recorder.push(make_frame(4))
    recorder.push(make_frame(5))

    frames = recorder.stop()

    assert [f.timestamp for f in frames] == [
        1,
        2,
        3,
        4,
        5,
    ]


def test_pre_buffer_capacity():

    recorder = Recorder(pre_buffer_frames=3)

    recorder.push(make_frame(1))
    recorder.push(make_frame(2))
    recorder.push(make_frame(3))
    recorder.push(make_frame(4))
    recorder.push(make_frame(5))

    recorder.start()

    frames = recorder.stop()

    assert [f.timestamp for f in frames] == [
        3,
        4,
        5,
    ]


def test_second_recording_is_clean():

    recorder = Recorder(pre_buffer_frames=2)

    recorder.push(make_frame(1))

    recorder.start()

    recorder.push(make_frame(2))

    recorder.stop()

    recorder.push(make_frame(10))
    recorder.push(make_frame(11))

    recorder.start()

    recorder.push(make_frame(12))

    frames = recorder.stop()

    assert [f.timestamp for f in frames] == [
        10,
        11,
        12,
    ]