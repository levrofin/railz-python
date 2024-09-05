from typing import Literal, Set, cast

DataSyncResponseDtoServiceName = Literal[
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

DATA_SYNC_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[DataSyncResponseDtoServiceName] = {
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


def check_data_sync_response_dto_service_name(value: str) -> DataSyncResponseDtoServiceName:
    if value in DATA_SYNC_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(DataSyncResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SYNC_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
