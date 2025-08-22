from enum import Enum


class ConsultationState(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    REQUESTED = "requested"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
