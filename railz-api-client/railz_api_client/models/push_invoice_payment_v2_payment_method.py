from typing import Literal, Set, cast

PushInvoicePaymentV2PaymentMethod = Literal[
    "bankTransfer", "cash", "check", "creditCard", "debitCard", "giftCard", "other", "unknown"
]

PUSH_INVOICE_PAYMENT_V2_PAYMENT_METHOD_VALUES: Set[PushInvoicePaymentV2PaymentMethod] = {
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
}


def check_push_invoice_payment_v2_payment_method(value: str) -> PushInvoicePaymentV2PaymentMethod:
    if value in PUSH_INVOICE_PAYMENT_V2_PAYMENT_METHOD_VALUES:
        return cast(PushInvoicePaymentV2PaymentMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_PAYMENT_V2_PAYMENT_METHOD_VALUES!r}")
