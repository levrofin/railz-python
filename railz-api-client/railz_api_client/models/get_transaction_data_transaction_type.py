from typing import Literal

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
