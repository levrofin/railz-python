from typing import Literal, Set, cast

AccountingTransactionTrackingCategoryRefV2Type = Literal["class", "department", "location", "unknown"]

ACCOUNTING_TRANSACTION_TRACKING_CATEGORY_REF_V2_TYPE_VALUES: Set[AccountingTransactionTrackingCategoryRefV2Type] = {
    "class",
    "department",
    "location",
    "unknown",
}


def check_accounting_transaction_tracking_category_ref_v2_type(
    value: str,
) -> AccountingTransactionTrackingCategoryRefV2Type:
    if value in ACCOUNTING_TRANSACTION_TRACKING_CATEGORY_REF_V2_TYPE_VALUES:
        return cast(AccountingTransactionTrackingCategoryRefV2Type, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACCOUNTING_TRANSACTION_TRACKING_CATEGORY_REF_V2_TYPE_VALUES!r}"
    )
