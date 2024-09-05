from typing import Literal, Set, cast

PushExpensePaymentMethod = Literal[
    "bankTransfer", "cash", "check", "creditCard", "debitCard", "giftCard", "other", "unknown"
]

PUSH_EXPENSE_PAYMENT_METHOD_VALUES: Set[PushExpensePaymentMethod] = {
    "bankTransfer",
    "cash",
    "check",
    "creditCard",
    "debitCard",
    "giftCard",
    "other",
    "unknown",
}


def check_push_expense_payment_method(value: str) -> PushExpensePaymentMethod:
    if value in PUSH_EXPENSE_PAYMENT_METHOD_VALUES:
        return cast(PushExpensePaymentMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_EXPENSE_PAYMENT_METHOD_VALUES!r}")
