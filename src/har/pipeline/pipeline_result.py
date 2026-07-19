from dataclasses import dataclass

from src.har.core.feature_frame import FeatureFrame
from src.har.dsp.event import Event


@dataclass(slots=True, frozen=True)
class PipelineResult:
    """
    Result of processing one audio frame.
    """

    feature: FeatureFrame
    noise_floor: float
    event: Event
