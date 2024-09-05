from typing import Literal, Set, cast

PushBillLineItemV2BillableStatus = Literal["billable", "hasBeenBilled", "notBillable"]

PUSH_BILL_LINE_ITEM_V2_BILLABLE_STATUS_VALUES: Set[PushBillLineItemV2BillableStatus] = {
    "billable",
    "hasBeenBilled",
    "notBillable",
}


def check_push_bill_line_item_v2_billable_status(value: str) -> PushBillLineItemV2BillableStatus:
    if value in PUSH_BILL_LINE_ITEM_V2_BILLABLE_STATUS_VALUES:
        return cast(PushBillLineItemV2BillableStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BILL_LINE_ITEM_V2_BILLABLE_STATUS_VALUES!r}")
