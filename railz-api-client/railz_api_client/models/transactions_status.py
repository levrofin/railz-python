from typing import Literal, Set, cast

TransactionsStatus = Literal["approved", "cancelled", "failed", "other", "pending", "scheduled", "success", "unknown"]

TRANSACTIONS_STATUS_VALUES: Set[TransactionsStatus] = {
    "approved",
    "cancelled",
    "failed",
    "other",
    "pending",
    "scheduled",
    "success",
    "unknown",
}


def check_transactions_status(value: str) -> TransactionsStatus:
    if value in TRANSACTIONS_STATUS_VALUES:
        return cast(TransactionsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTIONS_STATUS_VALUES!r}")
