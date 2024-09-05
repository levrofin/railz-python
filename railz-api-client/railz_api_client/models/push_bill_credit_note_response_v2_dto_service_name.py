from typing import Literal, Set, cast

PushBillCreditNoteResponseV2DtoServiceName = Literal[
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

PUSH_BILL_CREDIT_NOTE_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PushBillCreditNoteResponseV2DtoServiceName] = {
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


def check_push_bill_credit_note_response_v2_dto_service_name(value: str) -> PushBillCreditNoteResponseV2DtoServiceName:
    if value in PUSH_BILL_CREDIT_NOTE_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PushBillCreditNoteResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BILL_CREDIT_NOTE_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
