from enum import Enum


class ConsultationType(str, Enum):
    DEMO = "demo"
    IN_PERSON = "in-person"
    RECORDING = "recording"
    TELEHEALTH = "telehealth"

    def __str__(self) -> str:
        return str(self.value)
