from typing import Literal, Set, cast

BillCreditNotesStatus = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

BILL_CREDIT_NOTES_STATUS_VALUES: Set[BillCreditNotesStatus] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_bill_credit_notes_status(value: str) -> BillCreditNotesStatus:
    if value in BILL_CREDIT_NOTES_STATUS_VALUES:
        return cast(BillCreditNotesStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILL_CREDIT_NOTES_STATUS_VALUES!r}")
