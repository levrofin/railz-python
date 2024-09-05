from typing import Literal, Set, cast

PushInvoiceCreditNoteV1ResponseDtoServiceName = Literal[
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

PUSH_INVOICE_CREDIT_NOTE_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushInvoiceCreditNoteV1ResponseDtoServiceName] = {
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


def check_push_invoice_credit_note_v1_response_dto_service_name(
    value: str,
) -> PushInvoiceCreditNoteV1ResponseDtoServiceName:
    if value in PUSH_INVOICE_CREDIT_NOTE_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushInvoiceCreditNoteV1ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_CREDIT_NOTE_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
