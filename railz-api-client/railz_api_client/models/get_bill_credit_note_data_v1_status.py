from typing import Literal, Set, cast

GetBillCreditNoteDataV1Status = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

GET_BILL_CREDIT_NOTE_DATA_V1_STATUS_VALUES: Set[GetBillCreditNoteDataV1Status] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_get_bill_credit_note_data_v1_status(value: str) -> GetBillCreditNoteDataV1Status:
    if value in GET_BILL_CREDIT_NOTE_DATA_V1_STATUS_VALUES:
        return cast(GetBillCreditNoteDataV1Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BILL_CREDIT_NOTE_DATA_V1_STATUS_VALUES!r}")
