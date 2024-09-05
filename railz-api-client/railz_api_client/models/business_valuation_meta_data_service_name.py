from typing import Literal, Set, cast

BusinessValuationMetaDataServiceName = Literal[
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

BUSINESS_VALUATION_META_DATA_SERVICE_NAME_VALUES: Set[BusinessValuationMetaDataServiceName] = {
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


def check_business_valuation_meta_data_service_name(value: str) -> BusinessValuationMetaDataServiceName:
    if value in BUSINESS_VALUATION_META_DATA_SERVICE_NAME_VALUES:
        return cast(BusinessValuationMetaDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUSINESS_VALUATION_META_DATA_SERVICE_NAME_VALUES!r}")
