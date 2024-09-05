from typing import Literal, Set, cast

GetTransactionDataPaymentMethodType = Literal[
    "bank",
    "buyNowPayLater",
    "card",
    "cash",
    "cryptocurrency",
    "digital",
    "other",
    "paypal",
    "prepaid",
    "storeCredit",
    "unknown",
]

GET_TRANSACTION_DATA_PAYMENT_METHOD_TYPE_VALUES: Set[GetTransactionDataPaymentMethodType] = {
    "bank",
    "buyNowPayLater",
    "card",
    "cash",
    "cryptocurrency",
    "digital",
    "other",
    "paypal",
    "prepaid",
    "storeCredit",
    "unknown",
}


def check_get_transaction_data_payment_method_type(value: str) -> GetTransactionDataPaymentMethodType:
    if value in GET_TRANSACTION_DATA_PAYMENT_METHOD_TYPE_VALUES:
        return cast(GetTransactionDataPaymentMethodType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_TRANSACTION_DATA_PAYMENT_METHOD_TYPE_VALUES!r}")
