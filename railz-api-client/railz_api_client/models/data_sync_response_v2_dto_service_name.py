from typing import Literal, Set, cast

DataSyncResponseV2DtoServiceName = Literal[
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

DATA_SYNC_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[DataSyncResponseV2DtoServiceName] = {
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


def check_data_sync_response_v2_dto_service_name(value: str) -> DataSyncResponseV2DtoServiceName:
    if value in DATA_SYNC_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(DataSyncResponseV2DtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SYNC_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}")
