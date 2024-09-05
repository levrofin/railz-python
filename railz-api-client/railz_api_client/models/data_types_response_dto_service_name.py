from typing import Literal, Set, cast

DataTypesResponseDtoServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "plaid",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "shopify",
    "square",
    "wave",
    "xero",
    "zohoBooks",
]

DATA_TYPES_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[DataTypesResponseDtoServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "plaid",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "shopify",
    "square",
    "wave",
    "xero",
    "zohoBooks",
}


def check_data_types_response_dto_service_name(value: str) -> DataTypesResponseDtoServiceName:
    if value in DATA_TYPES_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(DataTypesResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_TYPES_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
