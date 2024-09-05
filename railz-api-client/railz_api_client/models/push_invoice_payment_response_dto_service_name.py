from typing import Literal, Set, cast

PushInvoicePaymentResponseDtoServiceName = Literal[
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

PUSH_INVOICE_PAYMENT_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushInvoicePaymentResponseDtoServiceName] = {
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


def check_push_invoice_payment_response_dto_service_name(value: str) -> PushInvoicePaymentResponseDtoServiceName:
    if value in PUSH_INVOICE_PAYMENT_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushInvoicePaymentResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_PAYMENT_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
