from typing import Literal, Set, cast

ArAgingMetaDataV2ServiceName = Literal[
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

AR_AGING_META_DATA_V2_SERVICE_NAME_VALUES: Set[ArAgingMetaDataV2ServiceName] = {
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


def check_ar_aging_meta_data_v2_service_name(value: str) -> ArAgingMetaDataV2ServiceName:
    if value in AR_AGING_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(ArAgingMetaDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AR_AGING_META_DATA_V2_SERVICE_NAME_VALUES!r}")
