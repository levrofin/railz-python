from typing import Literal, Set, cast

GetTrackingCategoryDataV2Status = Literal["active", "archived", "unknown"]

GET_TRACKING_CATEGORY_DATA_V2_STATUS_VALUES: Set[GetTrackingCategoryDataV2Status] = {
    "active",
    "archived",
    "unknown",
}


def check_get_tracking_category_data_v2_status(value: str) -> GetTrackingCategoryDataV2Status:
    if value in GET_TRACKING_CATEGORY_DATA_V2_STATUS_VALUES:
        return cast(GetTrackingCategoryDataV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_TRACKING_CATEGORY_DATA_V2_STATUS_VALUES!r}")
