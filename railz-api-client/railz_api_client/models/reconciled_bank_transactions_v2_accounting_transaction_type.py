from typing import Literal, Set, cast

ReconciledBankTransactionsV2AccountingTransactionType = Literal[
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

RECONCILED_BANK_TRANSACTIONS_V2_ACCOUNTING_TRANSACTION_TYPE_VALUES: Set[
    ReconciledBankTransactionsV2AccountingTransactionType
] = {
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


def check_reconciled_bank_transactions_v2_accounting_transaction_type(
    value: str,
) -> ReconciledBankTransactionsV2AccountingTransactionType:
    if value in RECONCILED_BANK_TRANSACTIONS_V2_ACCOUNTING_TRANSACTION_TYPE_VALUES:
        return cast(ReconciledBankTransactionsV2AccountingTransactionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECONCILED_BANK_TRANSACTIONS_V2_ACCOUNTING_TRANSACTION_TYPE_VALUES!r}"
    )
