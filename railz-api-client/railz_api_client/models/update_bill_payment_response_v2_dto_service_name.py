from typing import Literal, Set, cast

UpdateBillPaymentResponseV2DtoServiceName = Literal[
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

UPDATE_BILL_PAYMENT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[UpdateBillPaymentResponseV2DtoServiceName] = {
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


def check_update_bill_payment_response_v2_dto_service_name(value: str) -> UpdateBillPaymentResponseV2DtoServiceName:
    if value in UPDATE_BILL_PAYMENT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(UpdateBillPaymentResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_BILL_PAYMENT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
