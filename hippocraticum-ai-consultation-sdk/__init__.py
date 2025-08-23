"""A client library for accessing Hippocraticum AI Consultation API"""

from .client import AuthenticatedClient
from .client_public import ConsultationClient

__all__ = (
    "AuthenticatedClient",
    "ConsultationClient",
)
