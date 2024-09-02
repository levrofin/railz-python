from typing import Literal

InvoiceCreditNotesStatus = Literal[
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
]
