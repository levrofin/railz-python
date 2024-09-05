from typing import Literal, Set, cast

PushTrackingCategoriesV2Type = Literal["class", "department", "location", "unknown"]

PUSH_TRACKING_CATEGORIES_V2_TYPE_VALUES: Set[PushTrackingCategoriesV2Type] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_push_tracking_categories_v2_type(value: str) -> PushTrackingCategoriesV2Type:
    if value in PUSH_TRACKING_CATEGORIES_V2_TYPE_VALUES:
        return cast(PushTrackingCategoriesV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_TRACKING_CATEGORIES_V2_TYPE_VALUES!r}")
