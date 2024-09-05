from typing import Literal, Set, cast

TransactionSourceRefsType = Literal[
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

TRANSACTION_SOURCE_REFS_TYPE_VALUES: Set[TransactionSourceRefsType] = {
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


def check_transaction_source_refs_type(value: str) -> TransactionSourceRefsType:
    if value in TRANSACTION_SOURCE_REFS_TYPE_VALUES:
        return cast(TransactionSourceRefsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTION_SOURCE_REFS_TYPE_VALUES!r}")
