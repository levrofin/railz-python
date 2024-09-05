from typing import Literal, Set, cast

BusinessValuationMetaDataV2ServiceName = Literal[
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

BUSINESS_VALUATION_META_DATA_V2_SERVICE_NAME_VALUES: Set[BusinessValuationMetaDataV2ServiceName] = {
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


def check_business_valuation_meta_data_v2_service_name(value: str) -> BusinessValuationMetaDataV2ServiceName:
    if value in BUSINESS_VALUATION_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(BusinessValuationMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUSINESS_VALUATION_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
