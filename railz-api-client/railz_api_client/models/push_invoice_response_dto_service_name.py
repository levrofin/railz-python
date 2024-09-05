from typing import Literal, Set, cast

PushInvoiceResponseDtoServiceName = Literal[
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

PUSH_INVOICE_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushInvoiceResponseDtoServiceName] = {
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


def check_push_invoice_response_dto_service_name(value: str) -> PushInvoiceResponseDtoServiceName:
    if value in PUSH_INVOICE_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushInvoiceResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
