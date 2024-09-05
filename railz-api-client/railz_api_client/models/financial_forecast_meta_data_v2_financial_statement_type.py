from typing import Literal, Set, cast

FinancialForecastMetaDataV2FinancialStatementType = Literal["balanceSheets", "cashflowStatements", "incomeStatements"]

FINANCIAL_FORECAST_META_DATA_V2_FINANCIAL_STATEMENT_TYPE_VALUES: Set[
    FinancialForecastMetaDataV2FinancialStatementType
] = {
    "balanceSheets",
    "cashflowStatements",
    "incomeStatements",
}


def check_financial_forecast_meta_data_v2_financial_statement_type(
    value: str,
) -> FinancialForecastMetaDataV2FinancialStatementType:
    if value in FINANCIAL_FORECAST_META_DATA_V2_FINANCIAL_STATEMENT_TYPE_VALUES:
        return cast(FinancialForecastMetaDataV2FinancialStatementType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_FORECAST_META_DATA_V2_FINANCIAL_STATEMENT_TYPE_VALUES!r}"
    )
