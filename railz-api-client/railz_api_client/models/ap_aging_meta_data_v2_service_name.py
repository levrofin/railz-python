from typing import Literal, Set, cast

ApAgingMetaDataV2ServiceName = Literal[
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

AP_AGING_META_DATA_V2_SERVICE_NAME_VALUES: Set[ApAgingMetaDataV2ServiceName] = {
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


def check_ap_aging_meta_data_v2_service_name(value: str) -> ApAgingMetaDataV2ServiceName:
    if value in AP_AGING_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(ApAgingMetaDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AP_AGING_META_DATA_V2_SERVICE_NAME_VALUES!r}")
