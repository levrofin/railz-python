from typing import Literal

GetInvoiceV2DataStatus = Literal[
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
]
