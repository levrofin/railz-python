from typing import Literal, Set, cast

PushInvoiceCreditNoteV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_INVOICE_CREDIT_NOTE_V1_RESPONSE_DTO_STATUS_VALUES: Set[PushInvoiceCreditNoteV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_invoice_credit_note_v1_response_dto_status(value: str) -> PushInvoiceCreditNoteV1ResponseDtoStatus:
    if value in PUSH_INVOICE_CREDIT_NOTE_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushInvoiceCreditNoteV1ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_CREDIT_NOTE_V1_RESPONSE_DTO_STATUS_VALUES!r}"
    )
