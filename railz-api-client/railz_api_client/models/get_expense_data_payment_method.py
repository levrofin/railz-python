from typing import Literal

GetExpenseDataPaymentMethod = Literal[
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
]
