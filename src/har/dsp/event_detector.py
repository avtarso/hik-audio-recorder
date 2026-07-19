from src.har.dsp.event import Event


class EventDetector:
    """
    Detects start and stop of sound events.

    State machine:

        IDLE
          │
          ├── attack_frames
          ▼
        ACTIVE
          │
          ├── release_frames
          ▼
        IDLE
    """

    def __init__(
        self,
        threshold: float = 1.8,
        attack_frames: int = 3,
        release_frames: int = 75,
    ):

        self._threshold = threshold
        self._attack_frames = attack_frames
        self._release_frames = release_frames

        self._active = False

        self._attack_counter = 0
        self._release_counter = 0

    def update(
        self,
        rms: float,
        noise_floor: float,
    ) -> Event:

        loud = rms > noise_floor * self._threshold

        if not self._active:

            if loud:

                self._attack_counter += 1

                if self._attack_counter >= self._attack_frames:

                    self._active = True
                    self._attack_counter = 0

                    return Event.START

            else:

                self._attack_counter = 0

            return Event.NONE

        #
        # ACTIVE
        #

        if loud:

            self._release_counter = 0
            return Event.NONE

        self._release_counter += 1

        if self._release_counter >= self._release_frames:

            self._active = False
            self._release_counter = 0

            return Event.STOP

        return Event.NONE