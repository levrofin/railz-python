from typing import Literal, Set, cast

PushInvoiceCreditNoteV2ResponseDtoServiceName = Literal[
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

PUSH_INVOICE_CREDIT_NOTE_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushInvoiceCreditNoteV2ResponseDtoServiceName] = {
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


def check_push_invoice_credit_note_v2_response_dto_service_name(
    value: str,
) -> PushInvoiceCreditNoteV2ResponseDtoServiceName:
    if value in PUSH_INVOICE_CREDIT_NOTE_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushInvoiceCreditNoteV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_CREDIT_NOTE_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
