from typing import Literal, Set, cast

PushBankTransactionTransactionType = Literal["deposit", "expense", "overpayment", "payment"]

PUSH_BANK_TRANSACTION_TRANSACTION_TYPE_VALUES: Set[PushBankTransactionTransactionType] = {
    "deposit",
    "expense",
    "overpayment",
    "payment",
}


def check_push_bank_transaction_transaction_type(value: str) -> PushBankTransactionTransactionType:
    if value in PUSH_BANK_TRANSACTION_TRANSACTION_TYPE_VALUES:
        return cast(PushBankTransactionTransactionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSACTION_TRANSACTION_TYPE_VALUES!r}")
