from typing import Literal

PaymentMethodRefDtoType = Literal[
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
]
