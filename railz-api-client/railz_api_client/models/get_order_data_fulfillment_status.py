from typing import Literal

GetOrderDataFulfillmentStatus = Literal[
    "cancelled",
    "fulfilled",
    "partial",
    "unfulfilled",
    "unknown",
]
