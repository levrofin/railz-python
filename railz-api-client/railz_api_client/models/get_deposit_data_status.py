from typing import Literal, Set, cast

GetDepositDataStatus = Literal["draft", "open", "paid", "unknown", "void"]

GET_DEPOSIT_DATA_STATUS_VALUES: Set[GetDepositDataStatus] = {
    "draft",
    "open",
    "paid",
    "unknown",
    "void",
}


def check_get_deposit_data_status(value: str) -> GetDepositDataStatus:
    if value in GET_DEPOSIT_DATA_STATUS_VALUES:
        return cast(GetDepositDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_DEPOSIT_DATA_STATUS_VALUES!r}")
