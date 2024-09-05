from typing import Literal, Set, cast

UpdateInvoiceResponseV2DtoServiceName = Literal[
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

UPDATE_INVOICE_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[UpdateInvoiceResponseV2DtoServiceName] = {
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


def check_update_invoice_response_v2_dto_service_name(value: str) -> UpdateInvoiceResponseV2DtoServiceName:
    if value in UPDATE_INVOICE_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(UpdateInvoiceResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INVOICE_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
