from typing import Literal, Set, cast

PushInvoiceCreditNoteV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_INVOICE_CREDIT_NOTE_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushInvoiceCreditNoteV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_invoice_credit_note_v2_response_dto_status(value: str) -> PushInvoiceCreditNoteV2ResponseDtoStatus:
    if value in PUSH_INVOICE_CREDIT_NOTE_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushInvoiceCreditNoteV2ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_CREDIT_NOTE_V2_RESPONSE_DTO_STATUS_VALUES!r}"
    )
