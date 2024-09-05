from typing import Literal, Set, cast

PutCustomerV1ResponseDtoServiceName = Literal[
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

PUT_CUSTOMER_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PutCustomerV1ResponseDtoServiceName] = {
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


def check_put_customer_v1_response_dto_service_name(value: str) -> PutCustomerV1ResponseDtoServiceName:
    if value in PUT_CUSTOMER_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PutCustomerV1ResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUT_CUSTOMER_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
