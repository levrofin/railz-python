from typing import Literal

OrderPaymentStatus = Literal[
    "approved",
    "cancelled",
    "failed",
    "paid",
    "pending",
    "refunded",
    "unknown",
]
