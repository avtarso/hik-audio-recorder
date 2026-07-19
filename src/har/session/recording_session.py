from __future__ import annotations

from pathlib import Path

from src.har.core.audio_frame import AudioFrame
from src.har.dsp.event import Event
from src.har.io.wave_writer import WaveWriter
from src.har.pipeline.processing_pipeline import ProcessingPipeline
from src.har.recording.recorder import Recorder
from src.har.session.session_result import SessionResult


class RecordingSession:
    """
    High-level coordinator of the audio processing workflow.

    Responsibilities:

        AudioFrame
            ↓
        ProcessingPipeline
            ↓
        Recorder
            ↓
        WaveWriter
            ↓
        SessionResult

    This class contains no DSP logic and no audio processing
    algorithms. It only coordinates specialized components.
    """

    def __init__(
        self,
        output_dir: Path,
        pipeline: ProcessingPipeline | None = None,
        recorder: Recorder | None = None,
        writer: WaveWriter | None = None,
    ) -> None:

        self._output_dir = output_dir

        self._pipeline = pipeline or ProcessingPipeline()

        self._recorder = recorder or Recorder()

        self._writer = writer or WaveWriter()

        self._file_counter = 0

    def process(
        self,
        frame: AudioFrame,
    ) -> SessionResult:
        """
        Process one audio frame.

        Parameters
        ----------
        frame
            Audio frame to process.

        Returns
        -------
        SessionResult
            Processing result for this frame.
        """

        pipeline_result = self._pipeline.process(frame)

        self._update_recorder(
            frame,
            pipeline_result.event,
        )

        file = None

        if pipeline_result.event is Event.STOP:
            file = self._save_recording()

        return SessionResult(
            event=pipeline_result.event,
            file=file,
        )

    def _update_recorder(
        self,
        frame: AudioFrame,
        event: Event,
    ) -> None:
        """
        Update recorder state according to detected event.
        """

        if event is Event.START:

            self._recorder.start(frame)

            return

        if self._recorder.is_recording:

            self._recorder.push(frame)

    def _save_recording(self) -> Path:
        """
        Save completed recording and return output path.
        """

        frames = self._recorder.stop()

        path = self._next_output_path()

        self._writer.write(
            frames,
            path,
        )

        return path

    def _next_output_path(self) -> Path:
        """
        Generate next recording filename.
        """

        self._file_counter += 1

        return (
            self._output_dir
            / f"event_{self._file_counter:06d}.wav"
        )