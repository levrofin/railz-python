from typing import Literal, Set, cast

UpdateBillLineItemV1BillableStatus = Literal["billable", "hasBeenBilled", "notBillable"]

UPDATE_BILL_LINE_ITEM_V1_BILLABLE_STATUS_VALUES: Set[UpdateBillLineItemV1BillableStatus] = {
    "billable",
    "hasBeenBilled",
    "notBillable",
}


def check_update_bill_line_item_v1_billable_status(value: str) -> UpdateBillLineItemV1BillableStatus:
    if value in UPDATE_BILL_LINE_ITEM_V1_BILLABLE_STATUS_VALUES:
        return cast(UpdateBillLineItemV1BillableStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BILL_LINE_ITEM_V1_BILLABLE_STATUS_VALUES!r}")
