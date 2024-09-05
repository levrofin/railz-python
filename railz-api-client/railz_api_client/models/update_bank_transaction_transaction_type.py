from typing import Literal, Set, cast

UpdateBankTransactionTransactionType = Literal[
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

UPDATE_BANK_TRANSACTION_TRANSACTION_TYPE_VALUES: Set[UpdateBankTransactionTransactionType] = {
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


def check_update_bank_transaction_transaction_type(value: str) -> UpdateBankTransactionTransactionType:
    if value in UPDATE_BANK_TRANSACTION_TRANSACTION_TYPE_VALUES:
        return cast(UpdateBankTransactionTransactionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BANK_TRANSACTION_TRANSACTION_TYPE_VALUES!r}")
