from src.har.pipeline.pipeline import Pipeline
from src.har.processors.csv_recorder import CsvRecorder
from src.har.sources.rtsp_audio_source import RtspAudioSource


URL = "rtsp://admin:1qaz2wsx@192.168.0.103:554/Streaming/Channels/102"


def main():

    source = RtspAudioSource(URL)

    pipeline = Pipeline()

    recorder = CsvRecorder(
        "data/experiments/background.csv"
    )

    pipeline.add(recorder)

    try:
        for frame in source:
            pipeline.process(frame)

    except KeyboardInterrupt:
        print("\nОстановка...")

    finally:
        recorder.close()


if __name__ == "__main__":
    main()