from typing import Literal, Set, cast

BillLineItemsBillableStatus = Literal["billable", "hasBeenBilled", "notBillable"]

BILL_LINE_ITEMS_BILLABLE_STATUS_VALUES: Set[BillLineItemsBillableStatus] = {
    "billable",
    "hasBeenBilled",
    "notBillable",
}


def check_bill_line_items_billable_status(value: str) -> BillLineItemsBillableStatus:
    if value in BILL_LINE_ITEMS_BILLABLE_STATUS_VALUES:
        return cast(BillLineItemsBillableStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILL_LINE_ITEMS_BILLABLE_STATUS_VALUES!r}")
