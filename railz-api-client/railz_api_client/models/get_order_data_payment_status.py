from typing import Literal

GetOrderDataPaymentStatus = Literal[
    "approved",
    "cancelled",
    "failed",
    "paid",
    "pending",
    "refunded",
    "unknown",
]
