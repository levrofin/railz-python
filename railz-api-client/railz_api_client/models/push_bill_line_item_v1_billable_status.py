from typing import Literal, Set, cast

PushBillLineItemV1BillableStatus = Literal["billable", "hasBeenBilled", "notBillable"]

PUSH_BILL_LINE_ITEM_V1_BILLABLE_STATUS_VALUES: Set[PushBillLineItemV1BillableStatus] = {
    "billable",
    "hasBeenBilled",
    "notBillable",
}


def check_push_bill_line_item_v1_billable_status(value: str) -> PushBillLineItemV1BillableStatus:
    if value in PUSH_BILL_LINE_ITEM_V1_BILLABLE_STATUS_VALUES:
        return cast(PushBillLineItemV1BillableStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BILL_LINE_ITEM_V1_BILLABLE_STATUS_VALUES!r}")
