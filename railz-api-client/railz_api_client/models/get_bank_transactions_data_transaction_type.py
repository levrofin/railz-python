from typing import Literal, Set, cast

GetBankTransactionsDataTransactionType = Literal[
    "adjustment",
    "atm",
    "bankCharge",
    "billPayment",
    "cash",
    "cashback",
    "cheque",
    "directDebit",
    "interest",
    "purchase",
    "standingOrder",
    "transfer",
]

GET_BANK_TRANSACTIONS_DATA_TRANSACTION_TYPE_VALUES: Set[GetBankTransactionsDataTransactionType] = {
    "adjustment",
    "atm",
    "bankCharge",
    "billPayment",
    "cash",
    "cashback",
    "cheque",
    "directDebit",
    "interest",
    "purchase",
    "standingOrder",
    "transfer",
}


def check_get_bank_transactions_data_transaction_type(value: str) -> GetBankTransactionsDataTransactionType:
    if value in GET_BANK_TRANSACTIONS_DATA_TRANSACTION_TYPE_VALUES:
        return cast(GetBankTransactionsDataTransactionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_BANK_TRANSACTIONS_DATA_TRANSACTION_TYPE_VALUES!r}"
    )
