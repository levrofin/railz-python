from typing import Literal

OrderFulfillmentStatus = Literal[
    "cancelled",
    "fulfilled",
    "partial",
    "unfulfilled",
    "unknown",
]
