from typing import Literal, Set, cast

ReconciledBankTransactionsAccountingTransactionType = Literal[
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

RECONCILED_BANK_TRANSACTIONS_ACCOUNTING_TRANSACTION_TYPE_VALUES: Set[
    ReconciledBankTransactionsAccountingTransactionType
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


def check_reconciled_bank_transactions_accounting_transaction_type(
    value: str,
) -> ReconciledBankTransactionsAccountingTransactionType:
    if value in RECONCILED_BANK_TRANSACTIONS_ACCOUNTING_TRANSACTION_TYPE_VALUES:
        return cast(ReconciledBankTransactionsAccountingTransactionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECONCILED_BANK_TRANSACTIONS_ACCOUNTING_TRANSACTION_TYPE_VALUES!r}"
    )
