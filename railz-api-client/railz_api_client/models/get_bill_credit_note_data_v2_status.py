from typing import Literal

GetBillCreditNoteDataV2Status = Literal[
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
]
