from typing import Literal, Set, cast

GetEstimateDataStatus = Literal["closed", "draft", "open", "unknown", "void"]

GET_ESTIMATE_DATA_STATUS_VALUES: Set[GetEstimateDataStatus] = {
    "closed",
    "draft",
    "open",
    "unknown",
    "void",
}


def check_get_estimate_data_status(value: str) -> GetEstimateDataStatus:
    if value in GET_ESTIMATE_DATA_STATUS_VALUES:
        return cast(GetEstimateDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ESTIMATE_DATA_STATUS_VALUES!r}")
