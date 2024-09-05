from typing import Literal, Set, cast

TransactionKeywordsType = Literal[
    "bill",
    "billPayment",
    "creditNote",
    "deposit",
    "estimate",
    "expense",
    "inventoryAdjustment",
    "invoice",
    "journalEntry",
    "other",
    "payment",
    "payroll",
    "purchaseOrder",
    "refund",
    "taxAdjustment",
    "taxPayment",
    "taxRefund",
    "taxReversal",
    "transfer",
    "unknown",
    "vendorCreditNote",
]

TRANSACTION_KEYWORDS_TYPE_VALUES: Set[TransactionKeywordsType] = {
    "bill",
    "billPayment",
    "creditNote",
    "deposit",
    "estimate",
    "expense",
    "inventoryAdjustment",
    "invoice",
    "journalEntry",
    "other",
    "payment",
    "payroll",
    "purchaseOrder",
    "refund",
    "taxAdjustment",
    "taxPayment",
    "taxRefund",
    "taxReversal",
    "transfer",
    "unknown",
    "vendorCreditNote",
}


def check_transaction_keywords_type(value: str) -> TransactionKeywordsType:
    if value in TRANSACTION_KEYWORDS_TYPE_VALUES:
        return cast(TransactionKeywordsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTION_KEYWORDS_TYPE_VALUES!r}")
