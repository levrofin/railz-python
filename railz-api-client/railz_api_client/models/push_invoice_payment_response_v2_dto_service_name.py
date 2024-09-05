from typing import Literal, Set, cast

PushInvoicePaymentResponseV2DtoServiceName = Literal[
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

PUSH_INVOICE_PAYMENT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PushInvoicePaymentResponseV2DtoServiceName] = {
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


def check_push_invoice_payment_response_v2_dto_service_name(value: str) -> PushInvoicePaymentResponseV2DtoServiceName:
    if value in PUSH_INVOICE_PAYMENT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PushInvoicePaymentResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_PAYMENT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
