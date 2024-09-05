from typing import Literal, Set, cast

PushBillPaymentResponseDtoServiceName = Literal[
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

PUSH_BILL_PAYMENT_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushBillPaymentResponseDtoServiceName] = {
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


def check_push_bill_payment_response_dto_service_name(value: str) -> PushBillPaymentResponseDtoServiceName:
    if value in PUSH_BILL_PAYMENT_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushBillPaymentResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BILL_PAYMENT_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
