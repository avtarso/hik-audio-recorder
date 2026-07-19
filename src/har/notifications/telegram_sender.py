from __future__ import annotations

from pathlib import Path

import requests


class TelegramSender:
    """
    Sends recorded WAV files to a Telegram chat.
    """

    def __init__(
        self,
        token: str,
        chat_id: str,
    ) -> None:

        self._token = token
        self._chat_id = chat_id

    @property
    def api_url(self) -> str:

        return (
            f"https://api.telegram.org/bot"
            f"{self._token}/sendDocument"
        )

    def send(
        self,
        file: Path,
    ) -> None:

        with file.open("rb") as wav:

            response = requests.post(
                self.api_url,
                data={
                    "chat_id": self._chat_id,
                    "caption": file.name,
                },
                files={
                    "document": wav,
                },
                timeout=30,
            )

        response.raise_for_status()