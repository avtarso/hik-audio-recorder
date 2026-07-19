from pathlib import Path

from src.har.session.recording_session import RecordingSession
from src.har.session.recording_session import RecordingSession
from src.har.sources.rtsp_audio_source import RtspAudioSource


URL = "rtsp://admin:1qaz2wsx@192.168.0.103:554/Streaming/Channels/102"


def main():

    source = RtspAudioSource(URL)

    session = RecordingSession(
        output_dir=Path("recordings"),
    )

    print("Listening... Press Ctrl+C to stop.")

    try:

        for frame in source:

            result = session.process(frame)

            if result.file is not None:
                print(f"Saved: {result.file}")

    except KeyboardInterrupt:

        print("\nStopped.")


if __name__ == "__main__":
    main()