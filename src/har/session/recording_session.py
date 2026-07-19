from pathlib import Path

from src.har.core.audio_frame import AudioFrame
from src.har.pipeline.processing_pipeline import ProcessingPipeline
from src.har.recording.recorder import Recorder
from src.har.dsp.event import Event


class RecordingSession:

    def __init__(
        self,
        output_dir: Path,
        pipeline: ProcessingPipeline | None = None,
        recorder: Recorder | None = None,
    ):

        self._output_dir = output_dir

        self._pipeline = pipeline or ProcessingPipeline()

        self._recorder = recorder or Recorder()

    def process(
        self,
        frame: AudioFrame,
    ) -> None:

        result = self._pipeline.process(frame)

        if result.event is Event.START:

            self._recorder.start(frame)

        elif self._recorder.is_recording:

            self._recorder.push(frame)

        if result.event is Event.STOP:

            self._recorder.stop()