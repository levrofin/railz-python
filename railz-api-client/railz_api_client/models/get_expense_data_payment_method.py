from typing import Literal, Set, cast

GetExpenseDataPaymentMethod = Literal[
    "bankTransfer", "cash", "check", "creditCard", "debitCard", "giftCard", "other", "unknown"
]

GET_EXPENSE_DATA_PAYMENT_METHOD_VALUES: Set[GetExpenseDataPaymentMethod] = {
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
}


def check_get_expense_data_payment_method(value: str) -> GetExpenseDataPaymentMethod:
    if value in GET_EXPENSE_DATA_PAYMENT_METHOD_VALUES:
        return cast(GetExpenseDataPaymentMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_EXPENSE_DATA_PAYMENT_METHOD_VALUES!r}")
