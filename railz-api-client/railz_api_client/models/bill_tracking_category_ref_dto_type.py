from typing import Literal, Set, cast

BillTrackingCategoryRefDtoType = Literal["class", "department", "location", "unknown"]

BILL_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES: Set[BillTrackingCategoryRefDtoType] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_bill_tracking_category_ref_dto_type(value: str) -> BillTrackingCategoryRefDtoType:
    if value in BILL_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES:
        return cast(BillTrackingCategoryRefDtoType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILL_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES!r}")
