from typing import Literal, Set, cast

DeleteStatusMetaDataV2ServiceName = Literal[
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

DELETE_STATUS_META_DATA_V2_SERVICE_NAME_VALUES: Set[DeleteStatusMetaDataV2ServiceName] = {
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


def check_delete_status_meta_data_v2_service_name(value: str) -> DeleteStatusMetaDataV2ServiceName:
    if value in DELETE_STATUS_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(DeleteStatusMetaDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELETE_STATUS_META_DATA_V2_SERVICE_NAME_VALUES!r}")
