from typing import Literal

GetInvoicePaymentDataV2PaymentMethod = Literal[
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
]
