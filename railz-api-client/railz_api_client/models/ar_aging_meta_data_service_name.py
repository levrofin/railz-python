from typing import Literal, Set, cast

ArAgingMetaDataServiceName = Literal[
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

AR_AGING_META_DATA_SERVICE_NAME_VALUES: Set[ArAgingMetaDataServiceName] = {
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


def check_ar_aging_meta_data_service_name(value: str) -> ArAgingMetaDataServiceName:
    if value in AR_AGING_META_DATA_SERVICE_NAME_VALUES:
        return cast(ArAgingMetaDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AR_AGING_META_DATA_SERVICE_NAME_VALUES!r}")
