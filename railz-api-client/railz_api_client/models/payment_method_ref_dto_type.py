from typing import Literal, Set, cast

PaymentMethodRefDtoType = Literal[
    "bankTransfer", "cash", "check", "creditCard", "debitCard", "giftCard", "other", "unknown"
]

PAYMENT_METHOD_REF_DTO_TYPE_VALUES: Set[PaymentMethodRefDtoType] = {
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
}


def check_payment_method_ref_dto_type(value: str) -> PaymentMethodRefDtoType:
    if value in PAYMENT_METHOD_REF_DTO_TYPE_VALUES:
        return cast(PaymentMethodRefDtoType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PAYMENT_METHOD_REF_DTO_TYPE_VALUES!r}")
