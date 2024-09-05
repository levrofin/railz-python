from typing import Literal, Set, cast

GetInvoiceCreditNoteDataV2Status = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

GET_INVOICE_CREDIT_NOTE_DATA_V2_STATUS_VALUES: Set[GetInvoiceCreditNoteDataV2Status] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_get_invoice_credit_note_data_v2_status(value: str) -> GetInvoiceCreditNoteDataV2Status:
    if value in GET_INVOICE_CREDIT_NOTE_DATA_V2_STATUS_VALUES:
        return cast(GetInvoiceCreditNoteDataV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INVOICE_CREDIT_NOTE_DATA_V2_STATUS_VALUES!r}")
