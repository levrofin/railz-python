from typing import Literal, Set, cast

DataSyncDtoServiceName = Literal[
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

DATA_SYNC_DTO_SERVICE_NAME_VALUES: Set[DataSyncDtoServiceName] = {
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


def check_data_sync_dto_service_name(value: str) -> DataSyncDtoServiceName:
    if value in DATA_SYNC_DTO_SERVICE_NAME_VALUES:
        return cast(DataSyncDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SYNC_DTO_SERVICE_NAME_VALUES!r}")
