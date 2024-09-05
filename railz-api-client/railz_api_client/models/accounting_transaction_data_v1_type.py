from typing import Literal, Set, cast

AccountingTransactionDataV1Type = Literal[
    "bankTransaction",
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

ACCOUNTING_TRANSACTION_DATA_V1_TYPE_VALUES: Set[AccountingTransactionDataV1Type] = {
    "bankTransaction",
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


def check_accounting_transaction_data_v1_type(value: str) -> AccountingTransactionDataV1Type:
    if value in ACCOUNTING_TRANSACTION_DATA_V1_TYPE_VALUES:
        return cast(AccountingTransactionDataV1Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNTING_TRANSACTION_DATA_V1_TYPE_VALUES!r}")
