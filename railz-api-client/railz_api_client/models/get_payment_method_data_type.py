from typing import Literal

GetPaymentMethodDataType = Literal[
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
]
