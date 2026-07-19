from pathlib import Path
import os

from src.har.notifications.telegram_sender import TelegramSender

from src.har.session.recording_session import RecordingSession
from src.har.session.recording_session import RecordingSession
from src.har.sources.rtsp_audio_source import RtspAudioSource


URL = "rtsp://admin:1qaz2wsx@192.168.0.103:554/Streaming/Channels/102"


def main():

    source = RtspAudioSource(URL)

    session = RecordingSession(
        output_dir=Path("recordings"),
    )

    sender = TelegramSender(
        token=os.environ["HAR_TELEGRAM_TOKEN"],
        chat_id=os.environ["HAR_TELEGRAM_CHAT_ID"],
)

    print("Listening... Press Ctrl+C to stop.")

    try:

        for frame in source:

            result = session.process(frame)

            if result.file is not None:
                print(f"Saved: {result.file}")
                
                sender.send(result.file)

                result.file.unlink()

                print(f"Sent: {result.file.name}")

    except KeyboardInterrupt:

        print("\nStopped.")


if __name__ == "__main__":
    main()