from src.har.dsp.event import Event
from src.har.dsp.event_detector import EventDetector
from src.har.core.feature_frame import FeatureFrame


def make_feature(rms: float) -> FeatureFrame:

    return FeatureFrame(
        timestamp=0.0,
        sample_rate=8000,
        frame_size=320,
        rms=rms,
        peak=rms,
        mean=0.0,
        std=0.0,
        zero_crossings=50,
    )


def test_no_event():

    detector = EventDetector()

    for _ in range(20):

        event = detector.update(
            feature=make_feature(0.012),
            noise_floor=0.010,
        )

        assert event is Event.NONE


def test_start_event():

    detector = EventDetector(
        threshold=2.0,
        attack_frames=3,
    )

    assert detector.update(make_feature(0.010), 0.010) is Event.NONE

    assert detector.update(make_feature(0.030), 0.010) is Event.NONE
    assert detector.update(make_feature(0.030), 0.010) is Event.NONE

    assert detector.update(make_feature(0.030), 0.010) is Event.START


def test_active_event():

    detector = EventDetector(
        threshold=2.0,
        attack_frames=1,
    )

    assert detector.update(make_feature(0.030), 0.010) is Event.START

    for _ in range(10):

        assert detector.update(
            make_feature(0.030),
            0.010,
        ) is Event.NONE


def test_stop_event():

    detector = EventDetector(
        threshold=2.0,
        attack_frames=1,
        release_frames=3,
    )

    assert detector.update(
        make_feature(0.030),
        0.010,
    ) is Event.START

    assert detector.update(
        make_feature(0.010),
        0.010,
    ) is Event.NONE

    assert detector.update(
        make_feature(0.010),
        0.010,
    ) is Event.NONE

    assert detector.update(
        make_feature(0.010),
        0.010,
    ) is Event.STOP