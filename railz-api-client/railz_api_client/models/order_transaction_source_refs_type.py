from typing import Literal, Set, cast

OrderTransactionSourceRefsType = Literal[
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

ORDER_TRANSACTION_SOURCE_REFS_TYPE_VALUES: Set[OrderTransactionSourceRefsType] = {
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


def check_order_transaction_source_refs_type(value: str) -> OrderTransactionSourceRefsType:
    if value in ORDER_TRANSACTION_SOURCE_REFS_TYPE_VALUES:
        return cast(OrderTransactionSourceRefsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORDER_TRANSACTION_SOURCE_REFS_TYPE_VALUES!r}")
