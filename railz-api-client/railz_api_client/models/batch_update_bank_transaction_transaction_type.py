from typing import Literal, Set, cast

BatchUpdateBankTransactionTransactionType = Literal[
    "deposit",
    "depositFromOtherAccounts",
    "expense",
    "expenseRefund",
    "interestIncome",
    "otherIncome",
    "overPayment",
    "ownerDrawings",
    "ownersContribution",
    "payment",
    "refund",
    "salesReturn",
    "salesWithoutInvoices",
    "transfer",
    "unknown",
]

BATCH_UPDATE_BANK_TRANSACTION_TRANSACTION_TYPE_VALUES: Set[BatchUpdateBankTransactionTransactionType] = {
    "deposit",
    "depositFromOtherAccounts",
    "expense",
    "expenseRefund",
    "interestIncome",
    "otherIncome",
    "overPayment",
    "ownerDrawings",
    "ownersContribution",
    "payment",
    "refund",
    "salesReturn",
    "salesWithoutInvoices",
    "transfer",
    "unknown",
}


def check_batch_update_bank_transaction_transaction_type(value: str) -> BatchUpdateBankTransactionTransactionType:
    if value in BATCH_UPDATE_BANK_TRANSACTION_TRANSACTION_TYPE_VALUES:
        return cast(BatchUpdateBankTransactionTransactionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_UPDATE_BANK_TRANSACTION_TRANSACTION_TYPE_VALUES!r}"
    )
