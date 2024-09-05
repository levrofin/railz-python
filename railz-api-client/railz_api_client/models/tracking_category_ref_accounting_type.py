from typing import Literal, Set, cast

TrackingCategoryRefAccountingType = Literal["class", "department", "location", "unknown"]

TRACKING_CATEGORY_REF_ACCOUNTING_TYPE_VALUES: Set[TrackingCategoryRefAccountingType] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_tracking_category_ref_accounting_type(value: str) -> TrackingCategoryRefAccountingType:
    if value in TRACKING_CATEGORY_REF_ACCOUNTING_TYPE_VALUES:
        return cast(TrackingCategoryRefAccountingType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRACKING_CATEGORY_REF_ACCOUNTING_TYPE_VALUES!r}")
