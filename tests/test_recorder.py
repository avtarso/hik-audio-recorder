import numpy as np

from src.har.core.audio_frame import AudioFrame
from src.har.recording.recorder import Recorder
from tests.helpers import make_audio_frame


def test_stop_without_start():

    recorder = Recorder()

    assert recorder.stop() == []


def test_recording_collects_frames():

    recorder = Recorder(pre_buffer_frames=3)

    recorder.push(make_audio_frame(timestamp=1))
    recorder.push(make_audio_frame(timestamp=2))
    recorder.push(make_audio_frame(timestamp=3))

    recorder.start(make_audio_frame(timestamp=4))

    recorder.push(make_audio_frame(timestamp=5))

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

    recorder.push(make_audio_frame(timestamp=1))
    recorder.push(make_audio_frame(timestamp=2))
    recorder.push(make_audio_frame(timestamp=3))
    recorder.push(make_audio_frame(timestamp=4))
    recorder.push(make_audio_frame(timestamp=5))

    recorder.start(make_audio_frame(timestamp=6))

    frames = recorder.stop()

    assert [f.timestamp for f in frames] == [
        3,
        4,
        5,
        6,
    ]


def test_second_recording_is_clean():

    recorder = Recorder(pre_buffer_frames=2)

    recorder.push(make_audio_frame(timestamp=1))

    recorder.start(make_audio_frame(timestamp=2))

    recorder.stop()

    recorder.push(make_audio_frame(timestamp=10))
    recorder.push(make_audio_frame(timestamp=11))

    recorder.start(make_audio_frame(timestamp=12))

    frames = recorder.stop()

    assert [f.timestamp for f in frames] == [
        10,
        11,
        12,
    ]


def test_start_frame_is_not_duplicated():

    recorder = Recorder(pre_buffer_frames=3)

    recorder.push(make_audio_frame(timestamp=1))
    recorder.push(make_audio_frame(timestamp=2))
    recorder.push(make_audio_frame(timestamp=3))

    recorder.start(make_audio_frame(timestamp=4))

    frames = recorder.stop()

    assert [f.timestamp for f in frames] == [
        1,
        2,
        3,
        4,
    ]