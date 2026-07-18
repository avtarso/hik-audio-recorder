from src.har.io.rtsp_reader import RTSPReader
from src.har.pipeline.pipeline import Pipeline
from src.har.processors.frame_inspector import FrameInspector
from src.har.processors.acoustic_profiler import AcousticProfiler
from src.har.processors.csv_recorder import CsvRecorder

URL = "rtsp://admin:1qaz2wsx@192.168.0.103:554/Streaming/Channels/102"


def main():

    reader = RTSPReader(URL)

    pipeline = Pipeline()

    recorder = CsvRecorder(
        "data/experiments/background.csv"
    )

    pipeline.add(recorder)

    try:
        for frame in reader:
            pipeline.process(frame)

    except KeyboardInterrupt:
        print("\nОстановка...")

    finally:
        recorder.close()


if __name__ == "__main__":
    main()