from typing import Literal, Set, cast

GetBillPaymentV2DataPaymentMethod = Literal[
    "bankTransfer", "cash", "check", "creditCard", "debitCard", "giftCard", "other", "unknown"
]

GET_BILL_PAYMENT_V2_DATA_PAYMENT_METHOD_VALUES: Set[GetBillPaymentV2DataPaymentMethod] = {
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
}


def check_get_bill_payment_v2_data_payment_method(value: str) -> GetBillPaymentV2DataPaymentMethod:
    if value in GET_BILL_PAYMENT_V2_DATA_PAYMENT_METHOD_VALUES:
        return cast(GetBillPaymentV2DataPaymentMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BILL_PAYMENT_V2_DATA_PAYMENT_METHOD_VALUES!r}")
