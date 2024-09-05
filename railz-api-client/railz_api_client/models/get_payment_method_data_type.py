from typing import Literal, Set, cast

GetPaymentMethodDataType = Literal[
    "bankTransfer", "cash", "check", "creditCard", "debitCard", "giftCard", "other", "unknown"
]

GET_PAYMENT_METHOD_DATA_TYPE_VALUES: Set[GetPaymentMethodDataType] = {
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
}


def check_get_payment_method_data_type(value: str) -> GetPaymentMethodDataType:
    if value in GET_PAYMENT_METHOD_DATA_TYPE_VALUES:
        return cast(GetPaymentMethodDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_PAYMENT_METHOD_DATA_TYPE_VALUES!r}")
