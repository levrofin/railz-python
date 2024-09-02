from typing import Literal

GetBillV2DataStatus = Literal[
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
]
