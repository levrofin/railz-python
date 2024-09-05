from typing import Literal, Set, cast

ApAgingMetaDataServiceName = Literal[
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

AP_AGING_META_DATA_SERVICE_NAME_VALUES: Set[ApAgingMetaDataServiceName] = {
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


def check_ap_aging_meta_data_service_name(value: str) -> ApAgingMetaDataServiceName:
    if value in AP_AGING_META_DATA_SERVICE_NAME_VALUES:
        return cast(ApAgingMetaDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AP_AGING_META_DATA_SERVICE_NAME_VALUES!r}")
