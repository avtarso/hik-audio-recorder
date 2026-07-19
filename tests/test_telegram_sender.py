from pathlib import Path
from unittest.mock import MagicMock
from unittest.mock import mock_open
from unittest.mock import patch

from src.har.notifications.telegram_sender import TelegramSender


@patch("src.har.notifications.telegram_sender.requests.post")
def test_send_file(mock_post):

    response = MagicMock()
    mock_post.return_value = response

    sender = TelegramSender(
        token="TOKEN",
        chat_id="123456",
    )

    m = mock_open(read_data=b"wav-data")

    with patch.object(Path, "open", m):

        sender.send(
            Path("event.wav")
        )

    mock_post.assert_called_once()

    _, kwargs = mock_post.call_args

    assert kwargs["data"]["chat_id"] == "123456"
    assert kwargs["data"]["caption"] == "event.wav"

    response.raise_for_status.assert_called_once()