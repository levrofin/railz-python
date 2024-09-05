from typing import Literal, Set, cast

UpdateBillPaymentV2PaymentMethod = Literal[
    "bankTransfer", "cash", "check", "creditCard", "debitCard", "giftCard", "other", "unknown"
]

UPDATE_BILL_PAYMENT_V2_PAYMENT_METHOD_VALUES: Set[UpdateBillPaymentV2PaymentMethod] = {
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
}


def check_update_bill_payment_v2_payment_method(value: str) -> UpdateBillPaymentV2PaymentMethod:
    if value in UPDATE_BILL_PAYMENT_V2_PAYMENT_METHOD_VALUES:
        return cast(UpdateBillPaymentV2PaymentMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BILL_PAYMENT_V2_PAYMENT_METHOD_VALUES!r}")
