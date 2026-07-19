from dataclasses import dataclass
from pathlib import Path

from src.har.dsp.event import Event


@dataclass(slots=True, frozen=True)
class SessionResult:
    """
    Result of processing a single AudioFrame.
    """

    event: Event
    file: Path | None = None