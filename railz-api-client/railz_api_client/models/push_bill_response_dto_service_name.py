from typing import Literal, Set, cast

PushBillResponseDtoServiceName = Literal[
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

PUSH_BILL_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushBillResponseDtoServiceName] = {
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


def check_push_bill_response_dto_service_name(value: str) -> PushBillResponseDtoServiceName:
    if value in PUSH_BILL_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushBillResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BILL_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
