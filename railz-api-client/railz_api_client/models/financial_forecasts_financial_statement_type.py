from typing import Literal, Set, cast

FinancialForecastsFinancialStatementType = Literal["balanceSheets", "cashflowStatements", "incomeStatements"]

FINANCIAL_FORECASTS_FINANCIAL_STATEMENT_TYPE_VALUES: Set[FinancialForecastsFinancialStatementType] = {
    "balanceSheets",
    "cashflowStatements",
    "incomeStatements",
}


def check_financial_forecasts_financial_statement_type(value: str) -> FinancialForecastsFinancialStatementType:
    if value in FINANCIAL_FORECASTS_FINANCIAL_STATEMENT_TYPE_VALUES:
        return cast(FinancialForecastsFinancialStatementType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_FORECASTS_FINANCIAL_STATEMENT_TYPE_VALUES!r}"
    )
