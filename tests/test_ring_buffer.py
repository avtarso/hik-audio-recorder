import numpy as np

from src.har.core.audio_frame import AudioFrame
from src.har.core.ring_buffer import RingBuffer

from tests.helpers import make_audio_frame


def test_ring_buffer():

    buffer = RingBuffer(max_frames=3)

    assert buffer.size == 0
    assert not buffer.is_full

    buffer.push(make_audio_frame(
        value=1.0, 
        timestamp=0.00))
    buffer.push(make_audio_frame(
        value=2.0, 
        timestamp=0.04))
    buffer.push(make_audio_frame(
        value=3.0, 
        timestamp=0.08))

    assert buffer.size == 3
    assert buffer.is_full

    frames = buffer.get_all()

    assert frames[0].timestamp == 0.00
    assert frames[1].timestamp == 0.04
    assert frames[2].timestamp == 0.08

    buffer.push(make_audio_frame(
        value=4.0, 
        timestamp=0.12))

    assert buffer.size == 3

    frames = buffer.get_all()

    assert frames[0].timestamp == 0.04
    assert frames[1].timestamp == 0.08
    assert frames[2].timestamp == 0.12

    last = buffer.get_last(2)

    assert len(last) == 2
    assert last[0].timestamp == 0.08
    assert last[1].timestamp == 0.12

    buffer.clear()

    assert buffer.size == 0
    assert not buffer.is_full