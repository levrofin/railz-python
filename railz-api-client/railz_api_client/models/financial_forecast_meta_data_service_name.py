from typing import Literal, Set, cast

FinancialForecastMetaDataServiceName = Literal[
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

FINANCIAL_FORECAST_META_DATA_SERVICE_NAME_VALUES: Set[FinancialForecastMetaDataServiceName] = {
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


def check_financial_forecast_meta_data_service_name(value: str) -> FinancialForecastMetaDataServiceName:
    if value in FINANCIAL_FORECAST_META_DATA_SERVICE_NAME_VALUES:
        return cast(FinancialForecastMetaDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FINANCIAL_FORECAST_META_DATA_SERVICE_NAME_VALUES!r}")
