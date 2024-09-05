from typing import Literal, Set, cast

BusinessInfoMetaDataServiceName = Literal[
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

BUSINESS_INFO_META_DATA_SERVICE_NAME_VALUES: Set[BusinessInfoMetaDataServiceName] = {
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


def check_business_info_meta_data_service_name(value: str) -> BusinessInfoMetaDataServiceName:
    if value in BUSINESS_INFO_META_DATA_SERVICE_NAME_VALUES:
        return cast(BusinessInfoMetaDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUSINESS_INFO_META_DATA_SERVICE_NAME_VALUES!r}")
