from typing import Literal, Set, cast

PushBillPaymentResponseV2DtoServiceName = Literal[
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

PUSH_BILL_PAYMENT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PushBillPaymentResponseV2DtoServiceName] = {
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


def check_push_bill_payment_response_v2_dto_service_name(value: str) -> PushBillPaymentResponseV2DtoServiceName:
    if value in PUSH_BILL_PAYMENT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PushBillPaymentResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BILL_PAYMENT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
