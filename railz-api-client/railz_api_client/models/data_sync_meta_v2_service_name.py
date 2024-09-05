from typing import Literal, Set, cast

DataSyncMetaV2ServiceName = Literal[
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

DATA_SYNC_META_V2_SERVICE_NAME_VALUES: Set[DataSyncMetaV2ServiceName] = {
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


def check_data_sync_meta_v2_service_name(value: str) -> DataSyncMetaV2ServiceName:
    if value in DATA_SYNC_META_V2_SERVICE_NAME_VALUES:
        return cast(DataSyncMetaV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SYNC_META_V2_SERVICE_NAME_VALUES!r}")
