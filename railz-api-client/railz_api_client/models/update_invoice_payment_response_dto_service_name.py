from typing import Literal, Set, cast

UpdateInvoicePaymentResponseDtoServiceName = Literal[
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

UPDATE_INVOICE_PAYMENT_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[UpdateInvoicePaymentResponseDtoServiceName] = {
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


def check_update_invoice_payment_response_dto_service_name(value: str) -> UpdateInvoicePaymentResponseDtoServiceName:
    if value in UPDATE_INVOICE_PAYMENT_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(UpdateInvoicePaymentResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INVOICE_PAYMENT_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
