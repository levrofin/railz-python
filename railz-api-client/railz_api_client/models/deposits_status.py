from typing import Literal, Set, cast

DepositsStatus = Literal["draft", "open", "paid", "unknown", "void"]

DEPOSITS_STATUS_VALUES: Set[DepositsStatus] = {
    "draft",
    "open",
    "paid",
    "unknown",
    "void",
}


def check_deposits_status(value: str) -> DepositsStatus:
    if value in DEPOSITS_STATUS_VALUES:
        return cast(DepositsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DEPOSITS_STATUS_VALUES!r}")
