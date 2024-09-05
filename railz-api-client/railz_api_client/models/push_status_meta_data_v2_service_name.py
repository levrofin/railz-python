from typing import Literal, Set, cast

PushStatusMetaDataV2ServiceName = Literal[
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

PUSH_STATUS_META_DATA_V2_SERVICE_NAME_VALUES: Set[PushStatusMetaDataV2ServiceName] = {
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


def check_push_status_meta_data_v2_service_name(value: str) -> PushStatusMetaDataV2ServiceName:
    if value in PUSH_STATUS_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(PushStatusMetaDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_STATUS_META_DATA_V2_SERVICE_NAME_VALUES!r}")
