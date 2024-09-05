from typing import Literal, Set, cast

GetBillCreditNoteDataV2Status = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

GET_BILL_CREDIT_NOTE_DATA_V2_STATUS_VALUES: Set[GetBillCreditNoteDataV2Status] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_get_bill_credit_note_data_v2_status(value: str) -> GetBillCreditNoteDataV2Status:
    if value in GET_BILL_CREDIT_NOTE_DATA_V2_STATUS_VALUES:
        return cast(GetBillCreditNoteDataV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BILL_CREDIT_NOTE_DATA_V2_STATUS_VALUES!r}")
