from typing import Literal, Set, cast

GetEstimateDataV2Status = Literal["closed", "draft", "open", "unknown", "void"]

GET_ESTIMATE_DATA_V2_STATUS_VALUES: Set[GetEstimateDataV2Status] = {
    "closed",
    "draft",
    "open",
    "unknown",
    "void",
}


def check_get_estimate_data_v2_status(value: str) -> GetEstimateDataV2Status:
    if value in GET_ESTIMATE_DATA_V2_STATUS_VALUES:
        return cast(GetEstimateDataV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ESTIMATE_DATA_V2_STATUS_VALUES!r}")
