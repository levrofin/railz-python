from typing import Literal, Set, cast

DataTypesResponseV2DtoServiceName = Literal[
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

DATA_TYPES_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[DataTypesResponseV2DtoServiceName] = {
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


def check_data_types_response_v2_dto_service_name(value: str) -> DataTypesResponseV2DtoServiceName:
    if value in DATA_TYPES_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(DataTypesResponseV2DtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_TYPES_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}")
