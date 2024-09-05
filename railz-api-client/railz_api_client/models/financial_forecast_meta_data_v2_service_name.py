from typing import Literal, Set, cast

FinancialForecastMetaDataV2ServiceName = Literal[
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

FINANCIAL_FORECAST_META_DATA_V2_SERVICE_NAME_VALUES: Set[FinancialForecastMetaDataV2ServiceName] = {
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


def check_financial_forecast_meta_data_v2_service_name(value: str) -> FinancialForecastMetaDataV2ServiceName:
    if value in FINANCIAL_FORECAST_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(FinancialForecastMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_FORECAST_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
