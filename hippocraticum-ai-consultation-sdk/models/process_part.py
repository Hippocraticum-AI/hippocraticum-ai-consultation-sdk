from enum import Enum


class ProcessPart(str, Enum):
    CONSULTATION_PROCESSING = "consultation_processing"
    END = "end"
    FAILED = "failed"
    INSIGHTS_PROCESSING = "insights_processing"
    NLP_PROCESSING = "nlp_processing"
    SPEECH_PROCESSING = "speech_processing"

    def __str__(self) -> str:
        return str(self.value)
