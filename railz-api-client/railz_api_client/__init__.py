"""A client library for accessing FIS® Accounting Data as a Service™ API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
