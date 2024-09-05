from typing import Literal, Set, cast

PurchaseOrderTrackingCategoryRefDtoType = Literal["class", "department", "location", "unknown"]

PURCHASE_ORDER_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES: Set[PurchaseOrderTrackingCategoryRefDtoType] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_purchase_order_tracking_category_ref_dto_type(value: str) -> PurchaseOrderTrackingCategoryRefDtoType:
    if value in PURCHASE_ORDER_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES:
        return cast(PurchaseOrderTrackingCategoryRefDtoType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_TRACKING_CATEGORY_REF_DTO_TYPE_VALUES!r}"
    )
