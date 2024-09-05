from typing import Literal, Set, cast

PushTrackingCategoriesV2Status = Literal["active", "inactive", "unknown"]

PUSH_TRACKING_CATEGORIES_V2_STATUS_VALUES: Set[PushTrackingCategoriesV2Status] = {
    "active",
    "inactive",
    "unknown",
}


def check_push_tracking_categories_v2_status(value: str) -> PushTrackingCategoriesV2Status:
    if value in PUSH_TRACKING_CATEGORIES_V2_STATUS_VALUES:
        return cast(PushTrackingCategoriesV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_TRACKING_CATEGORIES_V2_STATUS_VALUES!r}")
