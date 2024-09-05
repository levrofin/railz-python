from typing import Literal, Set, cast

FinancialForecastMetaDataFinancialStatementType = Literal["balanceSheets", "cashflowStatements", "incomeStatements"]

FINANCIAL_FORECAST_META_DATA_FINANCIAL_STATEMENT_TYPE_VALUES: Set[FinancialForecastMetaDataFinancialStatementType] = {
    "balanceSheets",
    "cashflowStatements",
    "incomeStatements",
}


def check_financial_forecast_meta_data_financial_statement_type(
    value: str,
) -> FinancialForecastMetaDataFinancialStatementType:
    if value in FINANCIAL_FORECAST_META_DATA_FINANCIAL_STATEMENT_TYPE_VALUES:
        return cast(FinancialForecastMetaDataFinancialStatementType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_FORECAST_META_DATA_FINANCIAL_STATEMENT_TYPE_VALUES!r}"
    )
