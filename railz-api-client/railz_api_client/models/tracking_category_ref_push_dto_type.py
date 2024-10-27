from typing import Literal, Set, cast

TrackingCategoryRefPushDtoType = Literal["class", "department", "location", "unknown"]

TRACKING_CATEGORY_REF_PUSH_DTO_TYPE_VALUES: Set[TrackingCategoryRefPushDtoType] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_tracking_category_ref_push_dto_type(value: str) -> TrackingCategoryRefPushDtoType:
    if value in TRACKING_CATEGORY_REF_PUSH_DTO_TYPE_VALUES:
        return cast(TrackingCategoryRefPushDtoType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRACKING_CATEGORY_REF_PUSH_DTO_TYPE_VALUES!r}")
