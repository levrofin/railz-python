from typing import Literal, Set, cast

GetBankTransactionsV2DataTransactionType = Literal[
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

GET_BANK_TRANSACTIONS_V2_DATA_TRANSACTION_TYPE_VALUES: Set[GetBankTransactionsV2DataTransactionType] = {
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


def check_get_bank_transactions_v2_data_transaction_type(value: str) -> GetBankTransactionsV2DataTransactionType:
    if value in GET_BANK_TRANSACTIONS_V2_DATA_TRANSACTION_TYPE_VALUES:
        return cast(GetBankTransactionsV2DataTransactionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_BANK_TRANSACTIONS_V2_DATA_TRANSACTION_TYPE_VALUES!r}"
    )
