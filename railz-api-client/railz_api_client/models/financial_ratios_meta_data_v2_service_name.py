from typing import Literal, Set, cast

FinancialRatiosMetaDataV2ServiceName = Literal[
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

FINANCIAL_RATIOS_META_DATA_V2_SERVICE_NAME_VALUES: Set[FinancialRatiosMetaDataV2ServiceName] = {
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


def check_financial_ratios_meta_data_v2_service_name(value: str) -> FinancialRatiosMetaDataV2ServiceName:
    if value in FINANCIAL_RATIOS_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(FinancialRatiosMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_RATIOS_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
