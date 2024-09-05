from typing import Literal, Set, cast

GetTrackingCategoryDataV2Type = Literal["class", "department", "location", "unknown"]

GET_TRACKING_CATEGORY_DATA_V2_TYPE_VALUES: Set[GetTrackingCategoryDataV2Type] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_get_tracking_category_data_v2_type(value: str) -> GetTrackingCategoryDataV2Type:
    if value in GET_TRACKING_CATEGORY_DATA_V2_TYPE_VALUES:
        return cast(GetTrackingCategoryDataV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_TRACKING_CATEGORY_DATA_V2_TYPE_VALUES!r}")
