"""A client library for accessing Hippocraticum AI Consultation API"""

from .client_public import ConsultationClient
from .client_public_async import AsyncConsultationClient

__all__ = (
    "ConsultationClient",
    "AsyncConsultationClient",
)
