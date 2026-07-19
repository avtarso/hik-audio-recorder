from pathlib import Path

from src.har.core.audio_frame import AudioFrame
from src.har.pipeline.processing_pipeline import ProcessingPipeline


class RecordingSession:

    def __init__(
        self,
        output_dir: Path,
        pipeline: ProcessingPipeline | None = None,
    ):

        self._output_dir = output_dir

        self._pipeline = pipeline or ProcessingPipeline()

    def process(
        self,
        frame: AudioFrame,
    ) -> None:

        self._pipeline.process(frame)