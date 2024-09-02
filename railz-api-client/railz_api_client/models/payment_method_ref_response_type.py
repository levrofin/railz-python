from typing import Literal

PaymentMethodRefResponseType = Literal[
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
]
