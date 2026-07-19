from src.har.core.audio_frame import AudioFrame
from src.har.features.extractor import FeatureExtractor
from src.har.dsp.noise_floor_estimator import NoiseFloorEstimator
from src.har.dsp.event_detector import EventDetector

from src.har.pipeline.pipeline_result import PipelineResult


class AnalysisPipeline:
    """
    High-level DSP pipeline.

    AudioFrame
        ↓
    FeatureExtractor
        ↓
    NoiseFloorEstimator
        ↓
    EventDetector
        ↓
    PipelineResult
    """

    def __init__(
        self,
        extractor: FeatureExtractor | None = None,
        estimator: NoiseFloorEstimator | None = None,
        detector: EventDetector | None = None,
    ):

        self._extractor = extractor or FeatureExtractor()
        self._estimator = estimator or NoiseFloorEstimator()
        self._detector = detector or EventDetector()

    def process(
        self,
        frame: AudioFrame,
    ) -> PipelineResult:

        feature = self._extractor.extract(frame)

        self._estimator.update(feature.rms)

        noise_floor = self._estimator.noise_floor

        event = self._detector.update(
            feature,
            noise_floor,
        )

        return PipelineResult(
            feature=feature,
            noise_floor=noise_floor,
            event=event,
        )