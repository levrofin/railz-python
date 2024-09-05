from typing import Literal, Set, cast

InvoiceTrackingCategoryRefType = Literal["class", "department", "location", "unknown"]

INVOICE_TRACKING_CATEGORY_REF_TYPE_VALUES: Set[InvoiceTrackingCategoryRefType] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_invoice_tracking_category_ref_type(value: str) -> InvoiceTrackingCategoryRefType:
    if value in INVOICE_TRACKING_CATEGORY_REF_TYPE_VALUES:
        return cast(InvoiceTrackingCategoryRefType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_TRACKING_CATEGORY_REF_TYPE_VALUES!r}")
