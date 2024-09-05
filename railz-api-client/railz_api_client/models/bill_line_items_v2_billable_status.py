from typing import Literal, Set, cast

BillLineItemsV2BillableStatus = Literal["billable", "hasBeenBilled", "notBillable"]

BILL_LINE_ITEMS_V2_BILLABLE_STATUS_VALUES: Set[BillLineItemsV2BillableStatus] = {
    "billable",
    "hasBeenBilled",
    "notBillable",
}


def check_bill_line_items_v2_billable_status(value: str) -> BillLineItemsV2BillableStatus:
    if value in BILL_LINE_ITEMS_V2_BILLABLE_STATUS_VALUES:
        return cast(BillLineItemsV2BillableStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILL_LINE_ITEMS_V2_BILLABLE_STATUS_VALUES!r}")
