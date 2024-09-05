from typing import Literal, Set, cast

PushBillCreditNoteResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_BILL_CREDIT_NOTE_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushBillCreditNoteResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_bill_credit_note_response_v2_dto_status(value: str) -> PushBillCreditNoteResponseV2DtoStatus:
    if value in PUSH_BILL_CREDIT_NOTE_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushBillCreditNoteResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BILL_CREDIT_NOTE_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
