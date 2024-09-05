from typing import Literal, Set, cast

GetTransactionDataTransactionType = Literal[
    "dispute",
    "failedPayout",
    "order",
    "other",
    "payment",
    "paymentFee",
    "paymentFeeRefund",
    "payout",
    "refund",
    "transfer",
    "unknown",
]

GET_TRANSACTION_DATA_TRANSACTION_TYPE_VALUES: Set[GetTransactionDataTransactionType] = {
    "dispute",
    "failedPayout",
    "order",
    "other",
    "payment",
    "paymentFee",
    "paymentFeeRefund",
    "payout",
    "refund",
    "transfer",
    "unknown",
}


def check_get_transaction_data_transaction_type(value: str) -> GetTransactionDataTransactionType:
    if value in GET_TRANSACTION_DATA_TRANSACTION_TYPE_VALUES:
        return cast(GetTransactionDataTransactionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_TRANSACTION_DATA_TRANSACTION_TYPE_VALUES!r}")
