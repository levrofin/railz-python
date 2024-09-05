from typing import Literal, Set, cast

GetTrackingCategoryDataStatus = Literal["active", "archived", "unknown"]

GET_TRACKING_CATEGORY_DATA_STATUS_VALUES: Set[GetTrackingCategoryDataStatus] = {
    "active",
    "archived",
    "unknown",
}


def check_get_tracking_category_data_status(value: str) -> GetTrackingCategoryDataStatus:
    if value in GET_TRACKING_CATEGORY_DATA_STATUS_VALUES:
        return cast(GetTrackingCategoryDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_TRACKING_CATEGORY_DATA_STATUS_VALUES!r}")
