from typing import Literal, Set, cast

AccountingTransactionDataV2Type = Literal[
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

ACCOUNTING_TRANSACTION_DATA_V2_TYPE_VALUES: Set[AccountingTransactionDataV2Type] = {
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


def check_accounting_transaction_data_v2_type(value: str) -> AccountingTransactionDataV2Type:
    if value in ACCOUNTING_TRANSACTION_DATA_V2_TYPE_VALUES:
        return cast(AccountingTransactionDataV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNTING_TRANSACTION_DATA_V2_TYPE_VALUES!r}")
