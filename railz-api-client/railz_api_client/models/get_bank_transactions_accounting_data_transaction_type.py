from typing import Literal, Set, cast

GetBankTransactionsAccountingDataTransactionType = Literal[
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

GET_BANK_TRANSACTIONS_ACCOUNTING_DATA_TRANSACTION_TYPE_VALUES: Set[GetBankTransactionsAccountingDataTransactionType] = {
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


def check_get_bank_transactions_accounting_data_transaction_type(
    value: str,
) -> GetBankTransactionsAccountingDataTransactionType:
    if value in GET_BANK_TRANSACTIONS_ACCOUNTING_DATA_TRANSACTION_TYPE_VALUES:
        return cast(GetBankTransactionsAccountingDataTransactionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_BANK_TRANSACTIONS_ACCOUNTING_DATA_TRANSACTION_TYPE_VALUES!r}"
    )
