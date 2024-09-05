from typing import Literal, Set, cast

PaymentRequestPaymentMethodRefDtoType = Literal[
    "automatedClearingHouse",
    "bankTransfer",
    "cash",
    "creditCard",
    "debitCard",
    "giftCard",
    "manualCheck",
    "other",
    "printedCheck",
    "unknown",
]

PAYMENT_REQUEST_PAYMENT_METHOD_REF_DTO_TYPE_VALUES: Set[PaymentRequestPaymentMethodRefDtoType] = {
    "automatedClearingHouse",
    "bankTransfer",
    "cash",
    "creditCard",
    "debitCard",
    "giftCard",
    "manualCheck",
    "other",
    "printedCheck",
    "unknown",
}


def check_payment_request_payment_method_ref_dto_type(value: str) -> PaymentRequestPaymentMethodRefDtoType:
    if value in PAYMENT_REQUEST_PAYMENT_METHOD_REF_DTO_TYPE_VALUES:
        return cast(PaymentRequestPaymentMethodRefDtoType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAYMENT_REQUEST_PAYMENT_METHOD_REF_DTO_TYPE_VALUES!r}"
    )
