from typing import Literal, Set, cast

PushCustomerV1ResponseDtoServiceName = Literal[
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

PUSH_CUSTOMER_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushCustomerV1ResponseDtoServiceName] = {
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


def check_push_customer_v1_response_dto_service_name(value: str) -> PushCustomerV1ResponseDtoServiceName:
    if value in PUSH_CUSTOMER_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushCustomerV1ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_CUSTOMER_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
