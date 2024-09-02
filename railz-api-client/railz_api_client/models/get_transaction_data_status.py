from typing import Literal

GetTransactionDataStatus = Literal[
    "approved",
    "cancelled",
    "failed",
    "other",
    "pending",
    "scheduled",
    "success",
    "unknown",
]
