from typing import Literal, Set, cast

GetDepositV2DataStatus = Literal["draft", "open", "paid", "unknown", "void"]

GET_DEPOSIT_V2_DATA_STATUS_VALUES: Set[GetDepositV2DataStatus] = {
    "draft",
    "open",
    "paid",
    "unknown",
    "void",
}


def check_get_deposit_v2_data_status(value: str) -> GetDepositV2DataStatus:
    if value in GET_DEPOSIT_V2_DATA_STATUS_VALUES:
        return cast(GetDepositV2DataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_DEPOSIT_V2_DATA_STATUS_VALUES!r}")
