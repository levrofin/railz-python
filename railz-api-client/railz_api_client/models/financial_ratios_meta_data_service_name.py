from typing import Literal, Set, cast

FinancialRatiosMetaDataServiceName = Literal[
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

FINANCIAL_RATIOS_META_DATA_SERVICE_NAME_VALUES: Set[FinancialRatiosMetaDataServiceName] = {
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


def check_financial_ratios_meta_data_service_name(value: str) -> FinancialRatiosMetaDataServiceName:
    if value in FINANCIAL_RATIOS_META_DATA_SERVICE_NAME_VALUES:
        return cast(FinancialRatiosMetaDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FINANCIAL_RATIOS_META_DATA_SERVICE_NAME_VALUES!r}")
