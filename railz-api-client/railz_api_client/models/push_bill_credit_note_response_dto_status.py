from typing import Literal, Set, cast

PushBillCreditNoteResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_BILL_CREDIT_NOTE_RESPONSE_DTO_STATUS_VALUES: Set[PushBillCreditNoteResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_bill_credit_note_response_dto_status(value: str) -> PushBillCreditNoteResponseDtoStatus:
    if value in PUSH_BILL_CREDIT_NOTE_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushBillCreditNoteResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BILL_CREDIT_NOTE_RESPONSE_DTO_STATUS_VALUES!r}")
