from typing import Literal, Set, cast

TrackingCategoryResponseType = Literal["class", "department", "location", "unknown"]

TRACKING_CATEGORY_RESPONSE_TYPE_VALUES: Set[TrackingCategoryResponseType] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_tracking_category_response_type(value: str) -> TrackingCategoryResponseType:
    if value in TRACKING_CATEGORY_RESPONSE_TYPE_VALUES:
        return cast(TrackingCategoryResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRACKING_CATEGORY_RESPONSE_TYPE_VALUES!r}")
