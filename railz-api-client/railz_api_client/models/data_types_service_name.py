from typing import Literal, Set, cast

DataTypesServiceName = Literal[
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

DATA_TYPES_SERVICE_NAME_VALUES: Set[DataTypesServiceName] = {
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


def check_data_types_service_name(value: str) -> DataTypesServiceName:
    if value in DATA_TYPES_SERVICE_NAME_VALUES:
        return cast(DataTypesServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_TYPES_SERVICE_NAME_VALUES!r}")
