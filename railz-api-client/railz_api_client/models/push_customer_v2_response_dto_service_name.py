from typing import Literal, Set, cast

PushCustomerV2ResponseDtoServiceName = Literal[
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

PUSH_CUSTOMER_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushCustomerV2ResponseDtoServiceName] = {
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


def check_push_customer_v2_response_dto_service_name(value: str) -> PushCustomerV2ResponseDtoServiceName:
    if value in PUSH_CUSTOMER_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushCustomerV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_CUSTOMER_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
