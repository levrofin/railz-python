from typing import Literal, Set, cast

PushInvoiceTrackingCategoryRefType = Literal["class", "department", "location", "unknown"]

PUSH_INVOICE_TRACKING_CATEGORY_REF_TYPE_VALUES: Set[PushInvoiceTrackingCategoryRefType] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_push_invoice_tracking_category_ref_type(value: str) -> PushInvoiceTrackingCategoryRefType:
    if value in PUSH_INVOICE_TRACKING_CATEGORY_REF_TYPE_VALUES:
        return cast(PushInvoiceTrackingCategoryRefType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_TRACKING_CATEGORY_REF_TYPE_VALUES!r}")
