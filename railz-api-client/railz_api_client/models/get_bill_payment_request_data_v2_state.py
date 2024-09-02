from typing import Literal

GetBillPaymentRequestDataV2State = Literal[
    "approved",
    "draft",
    "open",
    "partiallyPaid",
    "posted",
    "unknown",
    "void",
]
