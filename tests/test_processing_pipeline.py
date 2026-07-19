import numpy as np

from src.har.core.audio_frame import AudioFrame
from src.har.pipeline.processing_pipeline import ProcessingPipeline
from src.har.pipeline.pipeline_result import PipelineResult


def test_process_returns_pipeline_result():

    frame = AudioFrame(
        samples=np.zeros(320, dtype=np.float32),
        sample_rate=8000,
        timestamp=0.0,
    )

    pipeline = ProcessingPipeline()

    result = pipeline.process(frame)

    assert isinstance(result, PipelineResult)