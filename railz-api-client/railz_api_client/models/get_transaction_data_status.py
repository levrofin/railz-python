from typing import Literal, Set, cast

GetTransactionDataStatus = Literal[
    "approved", "cancelled", "failed", "other", "pending", "scheduled", "success", "unknown"
]

GET_TRANSACTION_DATA_STATUS_VALUES: Set[GetTransactionDataStatus] = {
    "approved",
    "cancelled",
    "failed",
    "other",
    "pending",
    "scheduled",
    "success",
    "unknown",
}


def check_get_transaction_data_status(value: str) -> GetTransactionDataStatus:
    if value in GET_TRANSACTION_DATA_STATUS_VALUES:
        return cast(GetTransactionDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_TRANSACTION_DATA_STATUS_VALUES!r}")
