from typing import Literal

TransactionsStatus = Literal[
    "approved",
    "cancelled",
    "failed",
    "other",
    "pending",
    "scheduled",
    "success",
    "unknown",
]
