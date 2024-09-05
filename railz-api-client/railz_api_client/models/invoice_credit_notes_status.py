from typing import Literal, Set, cast

InvoiceCreditNotesStatus = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

INVOICE_CREDIT_NOTES_STATUS_VALUES: Set[InvoiceCreditNotesStatus] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_invoice_credit_notes_status(value: str) -> InvoiceCreditNotesStatus:
    if value in INVOICE_CREDIT_NOTES_STATUS_VALUES:
        return cast(InvoiceCreditNotesStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_CREDIT_NOTES_STATUS_VALUES!r}")
