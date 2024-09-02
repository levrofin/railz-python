from typing import Literal

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
