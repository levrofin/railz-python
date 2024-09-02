from typing import Literal

InvoicesStatus = Literal[
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
]
