from typing import Literal

ConnectionsStatus = Literal[
    "active",
    "disconnected",
    "expired",
    "invalid",
    "pending",
]
