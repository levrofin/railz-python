from typing import Literal, Set, cast

TrackingCategoryRefV2DtoType = Literal["class", "department", "location", "unknown"]

TRACKING_CATEGORY_REF_V2_DTO_TYPE_VALUES: Set[TrackingCategoryRefV2DtoType] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_tracking_category_ref_v2_dto_type(value: str) -> TrackingCategoryRefV2DtoType:
    if value in TRACKING_CATEGORY_REF_V2_DTO_TYPE_VALUES:
        return cast(TrackingCategoryRefV2DtoType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRACKING_CATEGORY_REF_V2_DTO_TYPE_VALUES!r}")
