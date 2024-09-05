from typing import Literal, Set, cast

RefundTrackingCategoryRefDtoType = Literal["class", "department", "location", "unknown"]

REFUND_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES: Set[RefundTrackingCategoryRefDtoType] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_refund_tracking_category_ref_dto_type(value: str) -> RefundTrackingCategoryRefDtoType:
    if value in REFUND_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES:
        return cast(RefundTrackingCategoryRefDtoType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REFUND_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES!r}")
