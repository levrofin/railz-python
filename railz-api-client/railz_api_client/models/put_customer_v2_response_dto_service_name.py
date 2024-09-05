from typing import Literal, Set, cast

PutCustomerV2ResponseDtoServiceName = Literal[
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

PUT_CUSTOMER_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PutCustomerV2ResponseDtoServiceName] = {
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


def check_put_customer_v2_response_dto_service_name(value: str) -> PutCustomerV2ResponseDtoServiceName:
    if value in PUT_CUSTOMER_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PutCustomerV2ResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUT_CUSTOMER_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
