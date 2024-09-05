from typing import Literal, Set, cast

PushInvoiceResponseV2DtoServiceName = Literal[
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

PUSH_INVOICE_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PushInvoiceResponseV2DtoServiceName] = {
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


def check_push_invoice_response_v2_dto_service_name(value: str) -> PushInvoiceResponseV2DtoServiceName:
    if value in PUSH_INVOICE_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PushInvoiceResponseV2DtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}")
