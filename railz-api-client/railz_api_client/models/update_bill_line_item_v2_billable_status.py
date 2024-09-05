from typing import Literal, Set, cast

UpdateBillLineItemV2BillableStatus = Literal["billable", "hasBeenBilled", "notBillable"]

UPDATE_BILL_LINE_ITEM_V2_BILLABLE_STATUS_VALUES: Set[UpdateBillLineItemV2BillableStatus] = {
    "billable",
    "hasBeenBilled",
    "notBillable",
}


def check_update_bill_line_item_v2_billable_status(value: str) -> UpdateBillLineItemV2BillableStatus:
    if value in UPDATE_BILL_LINE_ITEM_V2_BILLABLE_STATUS_VALUES:
        return cast(UpdateBillLineItemV2BillableStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BILL_LINE_ITEM_V2_BILLABLE_STATUS_VALUES!r}")
