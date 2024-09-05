from typing import Literal, Set, cast

DataSyncMetaServiceName = Literal[
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

DATA_SYNC_META_SERVICE_NAME_VALUES: Set[DataSyncMetaServiceName] = {
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


def check_data_sync_meta_service_name(value: str) -> DataSyncMetaServiceName:
    if value in DATA_SYNC_META_SERVICE_NAME_VALUES:
        return cast(DataSyncMetaServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SYNC_META_SERVICE_NAME_VALUES!r}")
