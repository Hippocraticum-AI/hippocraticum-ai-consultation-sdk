from enum import Enum


class MedicalResponseFormat(str, Enum):
    DAR = "dar"
    PIE = "pie"
    SBAR = "sbar"
    SOAP = "soap"

    def __str__(self) -> str:
        return str(self.value)
