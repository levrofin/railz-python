from typing import Literal, Set, cast

TrackingCategoryRefV2Type = Literal["class", "department", "location", "unknown"]

TRACKING_CATEGORY_REF_V2_TYPE_VALUES: Set[TrackingCategoryRefV2Type] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_tracking_category_ref_v2_type(value: str) -> TrackingCategoryRefV2Type:
    if value in TRACKING_CATEGORY_REF_V2_TYPE_VALUES:
        return cast(TrackingCategoryRefV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRACKING_CATEGORY_REF_V2_TYPE_VALUES!r}")
