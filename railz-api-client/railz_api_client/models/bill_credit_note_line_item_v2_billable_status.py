from typing import Literal, Set, cast

BillCreditNoteLineItemV2BillableStatus = Literal["billable", "hasBeenBilled", "notBillable"]

BILL_CREDIT_NOTE_LINE_ITEM_V2_BILLABLE_STATUS_VALUES: Set[BillCreditNoteLineItemV2BillableStatus] = {
    "billable",
    "hasBeenBilled",
    "notBillable",
}


def check_bill_credit_note_line_item_v2_billable_status(value: str) -> BillCreditNoteLineItemV2BillableStatus:
    if value in BILL_CREDIT_NOTE_LINE_ITEM_V2_BILLABLE_STATUS_VALUES:
        return cast(BillCreditNoteLineItemV2BillableStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BILL_CREDIT_NOTE_LINE_ITEM_V2_BILLABLE_STATUS_VALUES!r}"
    )
