from typing import Literal, Set, cast

BillCreditNoteLineItemBillableStatus = Literal["billable", "hasBeenBilled", "notBillable"]

BILL_CREDIT_NOTE_LINE_ITEM_BILLABLE_STATUS_VALUES: Set[BillCreditNoteLineItemBillableStatus] = {
    "billable",
    "hasBeenBilled",
    "notBillable",
}


def check_bill_credit_note_line_item_billable_status(value: str) -> BillCreditNoteLineItemBillableStatus:
    if value in BILL_CREDIT_NOTE_LINE_ITEM_BILLABLE_STATUS_VALUES:
        return cast(BillCreditNoteLineItemBillableStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BILL_CREDIT_NOTE_LINE_ITEM_BILLABLE_STATUS_VALUES!r}"
    )
