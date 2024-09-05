from typing import Literal, Set, cast

PushBillCreditNoteResponseDtoServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
]

PUSH_BILL_CREDIT_NOTE_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushBillCreditNoteResponseDtoServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
}


def check_push_bill_credit_note_response_dto_service_name(value: str) -> PushBillCreditNoteResponseDtoServiceName:
    if value in PUSH_BILL_CREDIT_NOTE_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushBillCreditNoteResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BILL_CREDIT_NOTE_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
