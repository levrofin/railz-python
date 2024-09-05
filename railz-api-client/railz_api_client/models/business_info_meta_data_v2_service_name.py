from typing import Literal, Set, cast

BusinessInfoMetaDataV2ServiceName = Literal[
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

BUSINESS_INFO_META_DATA_V2_SERVICE_NAME_VALUES: Set[BusinessInfoMetaDataV2ServiceName] = {
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


def check_business_info_meta_data_v2_service_name(value: str) -> BusinessInfoMetaDataV2ServiceName:
    if value in BUSINESS_INFO_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(BusinessInfoMetaDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUSINESS_INFO_META_DATA_V2_SERVICE_NAME_VALUES!r}")
