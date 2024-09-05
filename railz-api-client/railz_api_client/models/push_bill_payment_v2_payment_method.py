from typing import Literal, Set, cast

PushBillPaymentV2PaymentMethod = Literal[
    "bankTransfer", "cash", "check", "creditCard", "debitCard", "giftCard", "other", "unknown"
]

PUSH_BILL_PAYMENT_V2_PAYMENT_METHOD_VALUES: Set[PushBillPaymentV2PaymentMethod] = {
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
}


def check_push_bill_payment_v2_payment_method(value: str) -> PushBillPaymentV2PaymentMethod:
    if value in PUSH_BILL_PAYMENT_V2_PAYMENT_METHOD_VALUES:
        return cast(PushBillPaymentV2PaymentMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BILL_PAYMENT_V2_PAYMENT_METHOD_VALUES!r}")
