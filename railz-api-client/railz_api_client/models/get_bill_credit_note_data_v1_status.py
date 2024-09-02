from typing import Literal

GetBillCreditNoteDataV1Status = Literal[
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
]
