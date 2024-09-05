from typing import Literal, Set, cast

PaymentMethodRefResponseType = Literal[
    "bankTransfer", "cash", "check", "creditCard", "debitCard", "giftCard", "other", "unknown"
]

PAYMENT_METHOD_REF_RESPONSE_TYPE_VALUES: Set[PaymentMethodRefResponseType] = {
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
}


def check_payment_method_ref_response_type(value: str) -> PaymentMethodRefResponseType:
    if value in PAYMENT_METHOD_REF_RESPONSE_TYPE_VALUES:
        return cast(PaymentMethodRefResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PAYMENT_METHOD_REF_RESPONSE_TYPE_VALUES!r}")
